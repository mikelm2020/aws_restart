import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys


authorizaton_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=authorizaton_manager)


if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
response = sp.artist_top_tracks(urn)

for track in response['tracks']:
    print(track['name'])