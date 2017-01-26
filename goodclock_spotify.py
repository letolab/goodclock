import random
import spotipy
from spotipy import oauth2

import settings
from settings import logger
from db import DB


sp_oauth = oauth2.SpotifyOAuth(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET,
    redirect_uri=settings.SPOTIFY_REDIRECT_URL,
    scope=settings.SPOTIFY_SCOPE,
    state=None,
    cache_path=settings.SPOTIFY_CACHE_PATH,
)


def get_oauth_authorize_url():
    """" Create URL that we need to redirect user to when they need to authenticate
    with Spotify.

    """
    return sp_oauth.get_authorize_url()


def get_access_token(code):
    """Request access token based on auth code. Should be called in the callback view.

    """
    return sp_oauth.get_access_token(code)


def get_spotify_client():
    """Return Spotify API client. If stored token exists it will be authenticated.

    """
    # TODO - check if access token exists. If so return client with that token.
    # If not, return unauthenticated client.
    auth = sp_oauth.get_cached_token()
    token = auth['access_token'] if auth else None
    sp = spotipy.Spotify(auth=token)
    return sp


def get_current_username():
    """Return username of currently authenticated Spotify user.

    """
    sp = get_spotify_client()
    username = None
    try:
        user = sp.current_user()
        logger.info('Current logged in user: {}'.format(user))
        username = user['id']
    except spotipy.client.SpotifyException:
        logger.debug('No Spotify user logged in')
    return username


def get_goodclock_playlist(username):
    """Search for goodlist playlist belonging to user, and return it.

    """
    sp = get_spotify_client()
    playlists = sp.user_playlists(username)
    playlist_names = [(playlist['name'], playlist['uri']) for playlist in playlists['items']]
    nxt = sp.next(playlists)
    while nxt:
        next_playlist_names = [(playlist['name'], playlist['uri']) for playlist in nxt['items']]
        playlist_names += next_playlist_names
        nxt = sp.next(nxt)

    goodclock_playlist = None
    for name, uri in playlist_names:
        if name == settings.SPOTIFY_GOODCLOCK_PLAYLIST_NAME:
            goodclock_playlist = uri
            break
    return goodclock_playlist


def get_or_create_goodclock_playlist(username):
    """Search for goodlist playlist belonging to user and return it. If it doesn't
    exist, create one.

    """
    sp = get_spotify_client()
    logger.info('Getting goodclock playlist for user: {}...'.format(username))
    pl = get_goodclock_playlist(username)
    if pl:
        logger.info('Goodclock playlist found.')
        return pl

    logger.info('Goodclock playlist not found. Creating...')
    pl = sp.user_playlist_create(
        username,
        settings.SPOTIFY_GOODCLOCK_PLAYLIST_NAME,
        public=False
    )
    logger.info('Playlist created: {}'.format(pl))
    return pl['uri']


def get_all_playlist_track_data(username, playlist_uri):
    """Get all tracks belonging to playlist_uri.

    track_data is currently just a list of preview_urls.

    """
    sp = get_spotify_client()
    logger.debug('Getting all track data for playlist: {}'.format(playlist_uri))
    tracks = sp.user_playlist_tracks(
        username,
        playlist_id=playlist_uri,
    )
    track_data = []
    for track in tracks['items']:
        track = track['track']
        preview_url = track.get('preview_url')
        if preview_url:
            track_data.append(track)
        else:
            logger.warning("No preview available for track: {}".format(track['name']))

    return track_data


def get_random_playlist_track_preview_url(username, playlist_uri):
    """Get data for a random track belonging to playlist_uri.

    """
    track_data = get_all_playlist_track_data(username, playlist_uri)
    if not track_data:
        return None
    rand_track = random.choice(track_data)
    return rand_track['preview_url']


def get_random_playlist_track_uri(username, playlist_uri):
    """Get data for a random track belonging to playlist_uri.

    """
    track_data = get_all_playlist_track_data(username, playlist_uri)
    if not track_data:
        return None
    rand_track = random.choice(track_data)
    return rand_track['uri']


