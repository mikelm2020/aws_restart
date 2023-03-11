import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Obtiene el username desde la terminal
username = sys.argv[1]

# Borra el cache y pide permiso al usuario
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Creamos nuestro objeto spotify
spotify_object = spotipy.Spotify(auth=token)

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

# Obtenemos el usuario actual
user = spotify_object.current_user()

display_name = user["display_name"]
followers = user["followers"]["total"]

while True:
    print()
    print(f">>> Bienvenido a Restart Playlist {display_name} !")
    print(f">>> Tu tienes {str(followers)} seguidores")
    print()
    print("0 - Busqueda por un artista")
    print("1 - Salir")
    print()
    choice = input("Tu opción: ")

    # Busca por un artista
    if choice == "0":
        print()
        search_query = input("¿Cúal es su nombre?: ")
        print()

        # Obtiene los resultados de la busqueda
        search_results = spotify_object.search(search_query, 1, 0, "artist")

        # Detalles del artista
        artist = search_results["artists"]["items"][0]
        print(artist["name"])
        print(f"{str(artist['followers']['total'])} followers")
        print(artist["genres"][0])
        print()
        webbrowser.open(artist["images"][0]["url"])
        artist_ID = artist["id"]

        # Detalles del Album y pistas
        track_URIs = []
        track_art = []
        i = 0

        # Extrae datos del Album
        album_results = spotify_object.artist_albums(artist_ID)
        album_results = album_results["items"]
        for item in album_results:
            print(f"ALBUM {item['name']}")
            album_ID = item["id"]
            album_art = item["images"][0]["url"]

        # Extrae datos de la pista
        track_results = spotify_object.album_tracks(album_ID)
        track_results = track_results["items"]

        for item in track_results:
            print(f"{str(i)} : {item['name']}")
            track_URIs.append(item["uri"])
            track_art.append(album_art)
            i += 1
        print()

        # Ver arte del Album
        while True:
            song_selection = input(
                "Captura eel número de una canción para ver el arte del album asociado (x para salir): "
            )
            if song_selection == "x":
                break
            webbrowser.open(track_art[int(song_selection)])

    # Fin del programa
    if choice == "1":
        break

