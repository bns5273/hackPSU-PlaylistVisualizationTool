import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# '12121378058', 'user-library-read',

client_credentials_manager = SpotifyClientCredentials(client_id='b838401b0db04a85933513f481841e98', client_secret='43d18dd2ce414b7598c4a2ea531fb52b', )
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None