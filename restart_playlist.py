import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Convierte los segundos a un formato de HH:mm:ss
def convert_time(seconds):
    hours = int(seconds / 3600)
    seconds -= hours * 3600
    minutes = int(seconds / 60)
    seconds -= minutes * 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def user_credentials():
    scope = "playlist-modify-private"
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def find_artist(sp, search_query):
    # Obtiene los resultados de la busqueda
    search_results = sp.search(search_query, 1, 0, "artist")

    # Detalles del artista
    artist = search_results["artists"]["items"][0]
    print(f"Artista:  {artist['name']}")
    print(f"Seguidores: {artist['followers']['total']}")
    print(f"Genero: {artist['genres'][0]}")
    artist_ID = artist["id"]
    return artist_ID


def find_top_10_tracks(sp, artist_ID):
    artist_top_10_tracks = sp.artist_top_tracks(artist_ID, "MX")
    i = 0
    for track in artist_top_10_tracks["tracks"]:
        track_number = i + 1
        name = track["name"]
        popularity = track["popularity"]
        duration = track["duration_ms"]
        track_ID = track["id"]

        print(f" {track_number} - {name[:50]} - {popularity} ")
        i += 1

    return artist_top_10_tracks


# def create_playlist(sp, user_id, list_track_id, playlist_name):
#     # Crea la playlist en Spotify
#     playlist_id = sp.user_playlist_create(
#         user_id, playlist_name, False, False
#     )
#     list_track_id = ", ".join("\'" + str(track) + "\'" for track in list_track_id)
#     list_track_id = '\"' + list_track_id + '\"'
#     print(list_track_id)
#     # list_track_id = "'4nrPB8O7Y7wsOCJdgXkthe', '0DWdj2oZMBFSzRsi2Cvfzf', '6G12ZafqofSq7YtrMqUm76'"
#     # Agrega los tracks a la playlist recien creada
#     sp.playlist_add_items(playlist_id["id"], list_track_id)

def main():
    """ 
    Para ejecutar el programa se requiere exportar mediante variables de entorno
    SPOTIPY_CLIENT_ID
    SPOTIPY_CLIENT_SECRET
    SPOTIPY_REDIRECT_URI, aquí se puede agregar la url de Google (http://google.com/)
    """

    # Creamos nuestro objeto spotify
    spotify_object = user_credentials()

    # print(json.dumps(VARIABLE, sort_keys=True, indent=4))

    # Obtenemos el usuario actual
    user = spotify_object.current_user()

    display_name = user["display_name"]
    followers = user["followers"]["total"]
    user_ID = user["id"]

    while True:
        print()
        print(f">>> Bienvenido a Restart Playlist {display_name}! <<<")
        print(f">>> Tu tienes {str(followers)} seguidores <<<")
        print()
        print("0 - Busqueda por un artista")
        print("1 - Salir")
        print()
        choice = input("Selecciona tu opción: ")

        # Busca por un artista
        if choice == "0":
            print()
            search_query = input("¿Cúal es su nombre?: ")
            print()
            artist_ID = find_artist(spotify_object, search_query)
            print("*" * 30, end="TOP 10" + ("*" * 44) + "\n")
            # Obtiene el top 10 del artista capturado
            artist_top_10_tracks = find_top_10_tracks(spotify_object, artist_ID)
            print()
            print("*" * 80)
            print("Crear playlist")

            # Pide número de canción para agregar sus datos en listas
            # Declaración de listas
            list_track_ID = []
            list_track_name = []
            list_track_duration = []

            while True:
                song_selection = input("Captura el número de una canción (x para salir): ")
                if song_selection == "x":
                    break

                # Almacena la información de la canción seleccionada en listas
                store_track_ID = artist_top_10_tracks["tracks"][int(song_selection) - 1][
                    "id"
                ]
                list_track_ID.append(store_track_ID)

                store_track_name = artist_top_10_tracks["tracks"][int(song_selection) - 1][
                    "name"
                ]
                list_track_name.append(store_track_name)

                store_track_duration = artist_top_10_tracks["tracks"][
                    int(song_selection) - 1
                ]["duration_ms"]
                list_track_duration.append(store_track_duration)

                print("*" * 80)
                print("La canción que seleccionaste fue:")
                print(f"Canción: {store_track_name}")
                print(f"Duración: {convert_time(int(store_track_duration/1000))}")

            if len(list_track_ID) >= 2:
                playlist_duration = sum(list_track_duration)
                print(
                    f"El tiempo total de tu playlist es: {convert_time(int(playlist_duration/1000))}"
                )
                # while True:
                #     option = input("Desea crear la playlist S/N: ?")
                #     if option.upper() == "S":
                #         playlist_name = input("Nombre de la playlist: ")
                #         create_playlist(spotify_object, user_ID, list_track_ID, playlist_name)
                #         print("Playlist creada satisfactoriamente!!!")
                #         break

                #     elif option.upper() == "N":
                #         break
                #     else:
                #         print("Opción invalida")

        # Fin del programa
        if choice == "1":
            break


if __name__ == "__main__":
    main()
