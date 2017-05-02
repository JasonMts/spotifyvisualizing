import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = 'f06e7fa5003a485db5ab5334777a9c8a'
SPOTIPY_CLIENT_SECRET = '8b5c1744d7944157b516b6c4384af1e2'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

#Show tracks function
def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

#Generate an authorization token
token = SpotifyClientCredentials('f06e7fa5003a485db5ab5334777a9c8a', '8b5c1744d7944157b516b6c4384af1e2')
#Create a spotipy object using the credentials
sp = spotipy.Spotify(client_credentials_manager = token)

#Playlists Get
#User information
spotify = spotipy.Spotify()
username = '1266146616'
scope = None

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
            results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            count = count + 1
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
        else:
            count = count + 1
            continue
else:
    print("Can't get token for", username)
