# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import json
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff


pl = '0o6uIt2nSackwliyEdngAT'  # https://api.spotify.com/v1/playlists/
track = 'https://api.spotify.com/v1/tracks/4SE4yewyGpOYfxfx59Yjc5'
scope = 'user-library-read'


if __name__ == '__main__':
    username = 'dbc23910'

    # array of dicts of arrays??
    graphs = []
    names = []
    added_dates = []
    pop = []


    token = util.prompt_for_user_token(username, scope=scope, client_id='b838401b0db04a85933513f481841e98', client_secret='43d18dd2ce414b7598c4a2ea531fb52b', redirect_uri='http://localhost:8888/callback/')
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)['items']
        for playlist in playlists:
            graph = {
                'names': [],
                'artists': [],
                'album': [],
                'added_dates': [],
                'release_dates': [],
                'duration': [],
                'pop': [],
                'explicit': []
            }

            plid = playlist['id']
            tracks = sp.user_playlist_tracks(username, playlist_id=plid, fields='items')['items']
            for track in tracks:
                graph['names'].append(track['track']['name'])
                graph['added_dates'].append(track['added_at'])
                graph['pop'].append(track['track']['popularity'])
                graph['artists'].append(track['track']['artists'][0]['name'])
                graph['album'].append(track['track']['album']['name'])
                graph['release_date'].append(track['track']['album']['release_date'])
                graph['duration'].append(track['track']['duration_ms'])
                graph['explicit'].append(track['track']['explicit'])
            graphs.append(graph)

    else:
        print("Can't get token for", username)


adding_activity = []
for g in graphs:
    adding_activity.append(go.Scatter(
        x=g['added_dates'],
        y=g['pop'],
        hoverinfo="x+y",
        mode='markers'
    ))
py.plot(adding_activity, filename='hackPSU')
