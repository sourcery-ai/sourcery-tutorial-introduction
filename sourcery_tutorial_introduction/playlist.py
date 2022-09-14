import dataclasses
import typing

from tracks import Track


@dataclasses.dataclass
class Playlist:
    tracks: typing.List[Track]
