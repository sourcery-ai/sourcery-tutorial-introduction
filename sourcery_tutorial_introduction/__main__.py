import random
from .playlist import Playlist
from .tracks import fetch_tracks


def create_playlist(starting_tracks = []):
    tracks_all = list(fetch_tracks())
    list = starting_tracks
    duration_seconds_remaining = 1800

    while duration_seconds_remaining > 0:
        tracks_which_fit = []
        for track in tracks_all:
            if track.duration_seconds < duration_seconds_remaining:
                tracks_which_fit.append(track)
        if len(tracks_which_fit) == 0:
            break
        track_selected = random.choice(tracks_which_fit)
        if track_selected in list:
            continue
        duration_seconds_remaining = duration_seconds_remaining - track_selected.duration_seconds
        list.append(track_selected)

    return Playlist(list)


if __name__ == "__main__":
    playlist = create_playlist()
    print(playlist)
