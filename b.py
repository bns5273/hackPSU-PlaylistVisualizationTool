import json
from urllib.request import urlopen
import sys
import os
import spotipy
import spotipy.util as util

# os.environ['SPOTIPY_CLIENT_ID'] = 'b838401b0db04a85933513f481841e98'
# os.environ['SPOTIPY_CLIENT_SECRET'] = '43d18dd2ce414b7598c4a2ea531fb52b'
# os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback/'
scope = 'user-library-read'

username = '12121378058'
url = 'https://api.spotify.com/v1/playlists/1pgLsez1dIeBMBYWGBINUd'

urlopen('https://accounts.spotify.com/authorize/?'
        'client_id={}'
        '&response_type=code'
        '&redirect_uri={}'.format('b838401b0db04a85933513f481841e98', 'www.google.com'))
'''
GET https://accounts.spotify.com/authorize/?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09

'''


def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))


token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)
playlists = sp.user_playlists(username)
for playlist in playlists['items']:
    if playlist['owner']['id'] == username:
        print()
        print(playlist['name'])
        print('total tracks', playlist['tracks']['total'])
        results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)