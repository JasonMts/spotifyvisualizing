import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
from json import JSONDecoder
from functools import partial

SPOTIPY_CLIENT_ID = 'f06e7fa5003a485db5ab5334777a9c8a'
SPOTIPY_CLIENT_SECRET = '8b5c1744d7944157b516b6c4384af1e2'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

#Generate an authorization token
token = SpotifyClientCredentials('f06e7fa5003a485db5ab5334777a9c8a', '8b5c1744d7944157b516b6c4384af1e2')
#Create a spotipy object using the credentials
sp = spotipy.Spotify(client_credentials_manager = token)

#User information
spotify = spotipy.Spotify()
username = '1266146616'
scope = None

#Json parse function for parsing object from object, is not currently used
def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
         buffer += chunk
         while buffer:
             try:
                 result, index = decoder.raw_decode(buffer)
                 yield result
                 buffer = buffer[index:]
             except ValueError:
                 # Not enough data to decode, read more
                 break

#Show tracks function
def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

#Play function for spotify client
def play_spot():
    scope = 'user-modify-playback-state'
    a = SpotifyOAuth.get_cached_token
    if (a != None):
        c_token = SpotifyOAuth.get_cached_token
    else:
        c_token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    data = []
    with open('.cache-1266146616') as f:
        for line in f:
            data.append(json.loads(line))

    Play_URL = "https://api.spotify.com/v1/me/player/play"
    payload = {'access_token': 'token goes here',
               'grant_type': 'access_token'}

    auth_header = base64.b64encode(str(SPOTIPY_CLIENT_ID + ':' + SPOTIPY_CLIENT_SECRET).encode())
    header = {'Authorization': 'Bearer %s' % auth_header.decode()}

    r = requests.post(Play_URL, data=payload, headers=header)
    print(r.status_code)
    print(r.content)

#Pause function for spotify client
def pause_spot():
    scope = 'user-modify-playback-state'
    a = SpotifyOAuth.get_cached_token
    if (a != None):
        c_token = SpotifyOAuth.get_cached_token
    else:
        c_token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    data = []
    with open('.cache-1266146616') as f:
        for line in f:
            data.append(json.loads(line))

    Play_URL = "https://api.spotify.com/v1/me/player/pause"
    payload = {'access_token': 'token goes here',
               'grant_type': 'access_token'}

    auth_header = base64.b64encode(str(SPOTIPY_CLIENT_ID + ':' + SPOTIPY_CLIENT_SECRET).encode())
    header = {'Authorization': 'Bearer %s' % auth_header.decode()}

    r = requests.post(Play_URL, data=payload, headers=header)
    print(r.status_code)
    print(r.content)

#Play next song function for spotify client
def next_spot():
    scope = 'user-modify-playback-state'
    a = SpotifyOAuth.get_cached_token
    if (a != None):
        c_token = SpotifyOAuth.get_cached_token
    else:
        c_token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    data = []
    with open('.cache-1266146616') as f:
        for line in f:
            data.append(json.loads(line))

    Play_URL = "https://api.spotify.com/v1/me/player/next"
    payload = {'access_token': 'token goes here',
               'grant_type': 'access_token'}

    auth_header = base64.b64encode(str(SPOTIPY_CLIENT_ID + ':' + SPOTIPY_CLIENT_SECRET).encode())
    header = {'Authorization': 'Bearer %s' % auth_header.decode()}

    r = requests.post(Play_URL, data=payload, headers=header)
    print(r.status_code)
    print(r.content)

#Previous function for spotify client
def previous_spot():
    scope = 'user-modify-playback-state'
    a = SpotifyOAuth.get_cached_token
    if (a != None):
        c_token = SpotifyOAuth.get_cached_token
    else:
        c_token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    data = []
    with open('.cache-1266146616') as f:
        for line in f:
            data.append(json.loads(line))

    Play_URL = "https://api.spotify.com/v1/me/player/previous"
    payload = {'access_token': 'token goes here',
               'grant_type': 'access_token'}

    auth_header = base64.b64encode(str(SPOTIPY_CLIENT_ID + ':' + SPOTIPY_CLIENT_SECRET).encode())
    header = {'Authorization': 'Bearer %s' % auth_header.decode()}

    r = requests.post(Play_URL, data=payload, headers=header)
    print(r.status_code)
    print(r.content)

def playlist_get():
    #Cached token check, otherwise generate new token
    a = SpotifyOAuth.get_cached_token
    if (a != None):
        c_token = SpotifyOAuth.get_cached_token
    else:
        c_token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    #if token exists print all user playlists
    if token:
        playlists = sp.user_playlists(username)
        p_num = 1
        for playlist in playlists['items']:
                print("  %d %s" % (p_num, playlist['name']))
                p_num = p_num + 1
        #allow user to choose which playlist to print
        playlist_choice = input()

        if (int(playlist_choice) > (p_num - 1) | int(playlist_choice) < (p_num - 1)):
            print("Playlist number is not applicable.")
            sys.exit()

        #playlist print
        count = 1
        for playlist in playlists['items']:
            if (int(playlist_choice) == count and playlist['owner']['id'] == username):
                print()
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                #results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                #tracks = results['tracks']
                # show_tracks(tracks)
                count = count + 1
                # while tracks['next']:
                #     tracks = sp.next(tracks)
                #     show_tracks(tracks)
            else:
                count = count + 1
                continue
    else:
        print("Can't get token for", username)
