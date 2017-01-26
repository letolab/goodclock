import requests
import os
import tempfile
import time
# import pyglet

import goodclock_spotify
import settings
from settings import logger
import light


def save_audio_file_for_track_data(track_data):
    """Download the audio file for a given track.

    """
    url = track_data
    resp = requests.get(url)
    fd, path = tempfile.mkstemp(prefix='goodclock-', suffix='.mp3')
    f = open(path, 'wb')
    f.write(resp.content)
    return path


# def play_audio_file(path):
#     """Util function - play an audio file without stopping."""
#     source = pyglet.media.load(path)
#     source.play()
#     return source


def run_alarm_with_audio_file(path):
    """Execute alarm with a given track. This plays the track and listens for a stop
    event.

    """
    import vlc
    path = os.path.abspath(path)
    logger.info("MEDIA PATH: {}".format(path))
    p = vlc.MediaPlayer("file://{}".format(path))
    p.play()
    if listen_for_alarm_stop_event():
        p.pause()


def listen_for_alarm_stop_event():
    """Stub method - should listen for button press event"""
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            light.off()
            print 'Button Pressed'
            return True
        time.sleep(0.2)

    return True


def execute_alarm():
    logger.info('Executing alarm...')
    username = goodclock_spotify.get_current_username()
    playlist_uri = goodclock_spotify.get_or_create_goodclock_playlist(username)
    track_url = goodclock_spotify.get_random_playlist_track_preview_url(username, playlist_uri)
    if track_url:
        path = save_audio_file_for_track_data(track_url)
    else:
        path = settings.DEFAULT_TRACK_PATH
    light.on()
    run_alarm_with_audio_file(path)
    return True
