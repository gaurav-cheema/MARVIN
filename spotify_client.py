import os
import sys
from credentials import SPOTIFY_AUTH_TOKENS
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import json
from json.decoder import JSONDecodeError

SCOPE = 'user-read-private user-read-playback-state user-modify-playback-state'
SPOTIPY_CLIENT_ID = SPOTIFY_AUTH_TOKENS["Client ID"]
SPOTIPY_CLIENT_SECRET = SPOTIFY_AUTH_TOKENS["Client Secret"]
SPOTIPY_REDIRECT_URI = SPOTIFY_AUTH_TOKENS["Redirect URI"]
USERNAME = "atomicknight002"

UID = 26816222

# try:
#     token = util.prompt_for_user_token(UID, scope)
# except:
#     os.remove(f".cache-{UID}")
#     token = util.prompt_for_user_token(UID, scope)

token = util.prompt_for_user_token(username=USERNAME,
                                   scope=SCOPE,
                                   client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(token)

devices = sp.devices()
print(devices)

def next_song():
    sp.next_track()

def previous_song():
    sp.previous_track()

def pause():
    sp.pause_playback()

def play():
    sp.start_playback

def mute():
    sp.volume(0)

def unmute():
    sp.volume(50)

def fullVolume():
    sp.volume(100)