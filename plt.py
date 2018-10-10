
import sys
import spotipy
import spotipy.util as util
from datetime import datetime
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # username = sys.argv[1]
    # username = 'dbc23910'
    # username = 'noacolvin'
    # username = 'spevacus'
    username = '12121378058'

    scope = 'user-library-read'
    client_id = 'b838401b0db04a85933513f481841e98'
    client_secret = '43d18dd2ce414b7598c4a2ea531fb52b'
    redirect_uri = 'http://localhost:8888/callback/'

    graphs = []
    names = []

    token = util.prompt_for_user_token(
        username,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)

    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)['items']
    for playlist in playlists:
        names.append(playlist['name'])
        print(len(names)-1, names[-1])
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
            graph['added_dates'].append(datetime.strptime(track['added_at'][:7], '%Y-%m'))
            graph['pops'].append(track['track']['popularity'])
            graph['release_dates'].append(datetime.strptime(track['track']['album']['release_date'][:4], '%Y'))

            # graph['names'].append(track['track']['name'])
            # graph['durations'].append(datetime.datetime.fromtimestamp(track['track']['duration_ms'] / 1000.0))
            # graph['explicits'].append(track['track']['explicit'])
            # graph['artists'].append(track['track']['artists'][0]['name'])
            # graph['albums'].append(track['track']['album']['name'])
        graphs.append(graph)


plt.figure()
plt.hist([g['release_dates'] for g in graphs], stacked=True)
plt.figlegend(names)
plt.xlabel('Date')
plt.xticks(rotation=50)
plt.ylabel('Occ.')
plt.show()

plt.figure()
plt.hist([g['pops'] for g in graphs], stacked=True)
plt.figlegend(names)
plt.xlabel('Popularity')
plt.xticks(rotation=50)
plt.ylabel('Occ.')
plt.show()

plt.figure()
plt.scatter(graphs[9]['added_dates'], graphs[9]['release_dates'])
plt.xlabel('Added Date')
plt.xticks(rotation=50)
plt.ylabel('Release Date')
plt.show()

# explicitness = []
# for g, name in zip(graphs, names):
#     explicitness.append(ff.create_distplot(
#         g['added_dates'],
#         g['explicits'],
#         show_hist=False,
#         show_rug=False
#       ))
# explicitness = ff.create_distplot(
#         graphs[1]['added_dates'],
#         graphs[1]['explicits'],
# )
