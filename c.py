
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import json
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff


if __name__ == '__main__':
    username = 'dbc23910'
    scope = 'user-library-read'

    # array of dicts of arrays??
    graphs = []
    names = []


    token = util.prompt_for_user_token(username, scope=scope, client_id='b838401b0db04a85933513f481841e98', client_secret='43d18dd2ce414b7598c4a2ea531fb52b', redirect_uri='http://localhost:8888/callback/')
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)['items']
        for playlist in playlists:
            names.append(playlist['name'])
            print(names[-1])
            graph = {
                'names': [],
                'artists': [],
                'albums': [],
                'added_dates': [],
                'release_dates': [],
                'durations': [],
                'pops': [],
                'explicits': []
            }

            plid = playlist['id']
            tracks = sp.user_playlist_tracks(username, playlist_id=plid, fields='items')['items']
            for track in tracks:
                graph['names'].append(track['track']['name'])
                graph['added_dates'].append(track['added_at'])
                graph['pops'].append(track['track']['popularity'])
                graph['artists'].append(track['track']['artists'][0]['name'])
                graph['albums'].append(track['track']['album']['name'])
                graph['release_dates'].append(track['track']['album']['release_date'])
                graph['durations'].append(datetime.datetime.fromtimestamp(track['track']['duration_ms'] / 1000.0))
                graph['explicits'].append(track['track']['explicit'])
            graphs.append(graph)

    else:
        print("Can't get token for", username)


adding_activity = []
for g, name in zip(graphs, names):
    adding_activity.append(go.Scatter(
        x=g['added_dates'],
        y=g['pops'],
        name=name,
        text=g['names'],
        mode='markers'
    ))


era_pref = []
for g, name in zip(graphs, names):
    era_pref.append(go.Histogram(
        x=g['release_dates'],
        name=name,
        text=g['names']
    ))
era_pref_fig = go.Figure(
    data=era_pref,
    layout=go.Layout(
        barmode='stack',
        xaxis=dict(
            title='Release Date'
        ),
        yaxis=dict(
            title='Commonality'
        )
    ))

duration_pref = []
for g, name in zip(graphs, names):
    duration_pref.append(go.Histogram(
        x=g['durations'],
        name=name,
        text=g['names']
    ))
duration_pref_fig = go.Figure(
    data=duration_pref,
    layout=go.Layout(
        barmode='stack',
        xaxis=dict(
            title='Song Duration'
        ),
        yaxis=dict(
            title='Commonality'
        )
    ))

# explicitness = []
# for g, name in zip(graphs, names):
#     explicitness.append(ff.create_distplot(
#         g['added_dates'],
#         g['explicits'],
#         show_hist=False,
#         show_rug=False
# #     ))
# explicitness = ff.create_distplot(
#         graphs[1]['added_dates'],
#         graphs[1]['explicits'],
# )

# py.plot(adding_activity, filename='hackPSU-basicness')
# py.plot(era_pref_fig, filename='hackPSU-musicEra')
# py.plot(duration_pref_fig, filename='hackPSU-musicDuration')
# py.plot(explicitness, filename='hackPSU-explicitness')
