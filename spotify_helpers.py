import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth


key_mappings = {
    -1: "Not Specified",
    0: "C",
    1: "C#/Db",
    2: "D",
    3: "D#/Eb",
    4: "E",
    5: "F",
    6: "F#/Gb",
    7: "G",
    8: "G#, Ab",
    9: "A",
    10: "A#/Bb",
    11: "B"
}

mode_mappings = {
    0: "Minor",
    1: "Major"
}



def create_spotify_client(scope):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                     client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                                                     client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                                                     redirect_uri="http://localhost:8080"))


def get_playlist_tracks(spotify_client, playlist_id, limit=10, offset=0):
    tracks = spotify_client.playlist_items(
        playlist_id, limit=limit, offset=offset)
    return [track["track"] for track in tracks["items"]]


def get_audio_features_of_track(spotify_client, track_id):
    return spotify_client.audio_features([track_id])[0]


def make_playlist_dictionary(client, tracks):
    track_dictionary_list = list()
    for track in tracks:
        temp_track_id = track["id"]
        track_audio_features = get_audio_features_of_track(
            client, temp_track_id)
        track_dictionary = {
            "track_id": temp_track_id,
            "name": track["name"],
            "danceability": track_audio_features["danceability"],
            "energy": track_audio_features["energy"],
            "key": key_mappings[track_audio_features["key"]],
            "loudness": track_audio_features["loudness"],
            "mode": mode_mappings[track_audio_features["mode"]],
            "speechiness": track_audio_features["speechiness"],
            "acousticness": track_audio_features["acousticness"],
            "instrumentalness": track_audio_features["instrumentalness"],
            "liveness": track_audio_features["liveness"],
            "valence": track_audio_features["valence"],
            "tempo": track_audio_features["tempo"],
            "duration_ms": track_audio_features["duration_ms"],
            "time_signature": track_audio_features["time_signature"]
        }
        track_dictionary_list.append(track_dictionary)
    return track_dictionary_list
