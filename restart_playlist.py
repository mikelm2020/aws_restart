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
    print("1 - Busqueda por canción")
    print("2 - Salir")
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
        print(f"{str(artist['followers']['total'])} seguidores")
        print(artist["genres"][0])
        artist_ID = artist["id"]
        print()

        # Obtiene el top 10 del artista capturado
        artist_top_10_tracks = spotify_object.artist_top_tracks(artist_ID, "MX")

        # print(json.dumps(artist_top_10_tracks, sort_keys=True, indent=4))
        print()
        i = 0
        for track in artist_top_10_tracks["tracks"]:
            track_number = i + 1
            name = track["name"]
            popularity = track["popularity"]
            duration = track["duration_ms"]
            track_ID = track["id"]

            print(f" {track_number} - {name} - {popularity} ")
            i += 1

        print("*" * 80)
        print("Crear playlist")

        # Pide número de canción para agregarla a un diccionario
        # Declaración de variables
        playlist_dict = {}
        list_playlist_dict = []
        list_track_ID = []
        list_track_name = []
        list_track_duration = []
        while True:
            song_selection = input("Captura el número de una canción (x para salir): ")
            if song_selection == "x":
                break

            # Almacena la información de la canción seleccionada en listas
            store_track_ID = artist_top_10_tracks["tracks"][
                int(song_selection) - 1
            ]["id"]
            list_track_ID.append(store_track_ID)

            store_track_name = artist_top_10_tracks["tracks"][
                int(song_selection) - 1
            ]["name"]
            list_track_name.append(store_track_name)

            store_track_duration = artist_top_10_tracks["tracks"][
                int(song_selection) - 1
            ]["duration_ms"]
            list_track_duration.append(store_track_duration)

            print("*" * 80)
            print("La canción que seleccionaste fue:")
            print(f"Canción: {store_track_name}")
            print(f"Duración: {store_track_duration/60000}")

        print(list_track_ID)
        print(list_track_name)
        print(list_track_duration)


        # # Detalles del Album y pistas
        # track_URIs = []
        # track_art = []
        # i = 0

        # # Extrae datos del Album
        # album_results = spotify_object.artist_albums(artist_ID)
        # album_results = album_results["items"]
        # for item in album_results:
        #     print(f"ALBUM {item['name']}")
        #     album_ID = item["id"]
        #     album_art = item["images"][0]["url"]

        # # Extrae datos de la pista
        # track_results = spotify_object.album_tracks(album_ID)
        # track_results = track_results["items"]

        # for item in track_results:
        #     print(f"{str(i)} : {item['name']}")
        #     track_URIs.append(item["uri"])
        #     track_art.append(album_art)
        #     i += 1
        # print()

        # # Ver arte del Album
        # while True:
        #     song_selection = input(
        #         "Captura eel número de una canción para ver el arte del album asociado (x para salir): "
        #     )
        #     if song_selection == "x":
        #         break
        #     webbrowser.open(track_art[int(song_selection)])

    # Busqueda por canción
    if choice == "1":
        pass

    # Fin del programa
    if choice == "2":
        break
