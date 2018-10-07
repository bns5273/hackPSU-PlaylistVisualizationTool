# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


pl = '0o6uIt2nSackwliyEdngAT'  # https://api.spotify.com/v1/playlists/
track = 'https://api.spotify.com/v1/tracks/4SE4yewyGpOYfxfx59Yjc5'
scope = 'user-library-read'


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        # print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))
        print('   ', track['href'])


if __name__ == '__main__':
    username = 'dbc23910'

    token = util.prompt_for_user_token(username, scope=scope, client_id='b838401b0db04a85933513f481841e98', client_secret='43d18dd2ce414b7598c4a2ea531fb52b', redirect_uri='http://localhost:8888/callback/')
    print(token)
    if token:
        sp = spotipy.Spotify(auth=token)
        # playlists = sp.user_playlists(username)
        tracks = sp.user_playlist_tracks(username, playlist_id=pl, fields='items', limit=100, offset=0, market=None)['items']
        for track in tracks:
            name = track['track']['name']
            artist = track['track']['artists'][0]['name']
            album = track['track']['album']['name']
            release_date = track['track']['album']['release_date']
            added_date = track['added_at']
            duration = track['track']['duration_ms']
            pop = track['track']['popularity']
            explicit = track['track']['explicit']



        # for playlist in playlists['items']:
        #     if playlist['owner']['id'] == username:
        #         print()
        #         print(playlist['href'])
        #         # print('  total tracks', playlist['tracks']['total'])
        #         results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
        #         tracks = results['tracks']
        #         show_tracks(tracks)
        #         while tracks['next']:
        #             tracks = sp.next(tracks)
        #             show_tracks(tracks)
    else:
        print("Can't get token for", username)
