#!/usr/bin/env python
import datetime
import spotipy
from flask import Flask
from flask import render_template, redirect, request, send_from_directory

import settings
import goodclock_spotify
from settings import logger
from db import DB
import alarm
import light


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_view():
    """Main app view - shows status and lets user control settings.

    """
    current_time = datetime.datetime.now().strftime("%H:%M")
    user_playlist = None
    username = None
    try:
        username = goodclock_spotify.get_current_username()
    except spotipy.client.SpotifyException:
        logger.warning('Spotify exception getting username')

    if username:
        try:
            user_playlist = goodclock_spotify.get_or_create_goodclock_playlist(username)
        except spotipy.client.SpotifyException:
            logger.warning('Spotify exception getting/creating playlist')

    alarm_time = DB.get_alarm_time()

    return render_template(
        'home.html',
        username=username,
        current_time=current_time,
        user_playlist=user_playlist,
        alarm_time=alarm_time,
    )


@app.route('/spotify-oauth/login', methods=['GET'])
def spotify_oauth_redirect():
    """Button that redirects to the Spotify auth page.

    """
    auth_url = goodclock_spotify.get_oauth_authorize_url()
    logger.debug('Redirecting to auth_url: {}'.format(auth_url))
    return redirect(auth_url)


@app.route('/spotify-oauth/callback', methods=['GET'])
def spotify_oauth_callback():
    """Spotify will redirect to this page, providing the oauth code.

    NOTE: The Spotify API account must be configured to redirect to this URL.

    """
    logger.debug('Spotify callback endpoint with query_string: {}'.format(request.query_string))
    code = request.args.get('code')

    if not code:
        logger.warning("Didn't receive Spotify code! Redirecting to /")
        return redirect('/')

    logger.debug('Parsed Spotify auth code: {}'.format(code))
    token_info = goodclock_spotify.get_access_token(code)
    if token_info:
        logger.info('Successfully authenticated Spotify user')
    else:
        logger.warning('Failed to authenticate Spotify user')

    # Ensure playlist exists
    username = goodclock_spotify.get_current_username()
    return redirect('/')


@app.route('/alarm/set', methods=['POST'])
def alarm_set():
    """Handling for the alarm-set form.

    """
    logger.info("ALARM FORM: {}".format(request.form))
    alarm_time = request.form.get("time")
    if not alarm_time:
        logger.warning("Time not received")
        return redirect('/')

    hour, minute = alarm_time.split(":")
    DB.set_alarm_time(int(hour), int(minute))

    return redirect('/')


@app.route('/alarm/simulate', methods=['POST'])
def alarm_simulate():
    """Execute the alarm now.

    """
    logger.info('Simulating alarm...')
    alarm.execute_alarm()
    return redirect('/')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    light.off()
    app.run(host=settings.SERVER_HOST, port=settings.SERVER_PORT)
