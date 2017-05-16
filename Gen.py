## This file can be used to force generate a new auth token for use with the spotify API

import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import requests
import json

SPOTIPY_CLIENT_ID = 'f06e7fa5003a485db5ab5334777a9c8a'
SPOTIPY_CLIENT_SECRET = '8b5c1744d7944157b516b6c4384af1e2'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

#Generate an authorization token
token = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
#Create a spotipy object using the credentials
sp = spotipy.Spotify(client_credentials_manager = token)

#User information
spotify = spotipy.Spotify()
username = 'username'   #username goes here
scope = 'user-modify-playback-state'

c_token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
#c_token = SpotifyOAuth.get_access_token
#These two function calls can be used to generate auth tokens, use the first one primarily

if token:
    playlists = sp.user_playlists(username)
    p_num = 1
    for playlist in playlists['items']:
            print("  %d %s" % (p_num, playlist['name']))
            p_num = p_num + 1
