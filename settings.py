import logging
import sys
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler(sys.stdout)
h.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
h.setFormatter(formatter)
logger.addHandler(h)

SERVER_HOST = "0.0.0.0"
SERVER_PORT = "8080"

SPOTIFY_CLIENT_ID = os.environ.get("GOODCLOCK_SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.environ.get("GOODCLOCK_CLIENT_SECRET", "")
SPOTIFY_REDIRECT_URL = "http://localhost:{}/spotify-oauth/callback".format(SERVER_PORT)
SPOTIFY_CACHE_PATH = "/tmp/goodclock-spotify.cache"

SPOTIFY_SCOPE = " ".join([
    "playlist-read-private",
    "playlist-modify-private",
    "playlist-modify-public",
    "user-top-read",
    "user-read-private",
    "streaming",
])

DEFAULT_TRACK_PATH = "default.mp3"

DB_PATH = os.environ.get("GOODCLOCK_DB_PATH", ".goodclock.db")

SPOTIFY_GOODCLOCK_PLAYLIST_NAME = "GOODCLOCK"

try:
    from settings_local import *
except ImportError:
    pass
