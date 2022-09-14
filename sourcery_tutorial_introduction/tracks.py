import dataclasses
import typing


@dataclasses.dataclass
class Track:
    title: str
    artist: str
    duration_seconds: int


def fetch_tracks() -> typing.Iterator[Track]:
    ...
