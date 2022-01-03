import tabulate
from dotenv import load_dotenv

import spotify_helpers as sph

load_dotenv()


def main():
    scope = ['playlist-read-private', 'playlist-read-collaborative']
    client = sph.create_spotify_client(scope)
    tracks = sph.get_playlist_tracks(client, "5OzKJPLVbJwRGnr67insFM", 10, 0)
    track_dictionary_list = sph.make_playlist_dictionary(client, tracks)

    header = track_dictionary_list[0].keys()
    rows = [track.values() for track in track_dictionary_list]
    print(sph.tabulate_tracks(rows, tablefmt='grid'))

if __name__ == "__main__":
    main()
