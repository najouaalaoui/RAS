from RAS_Conversions import node_category


class Node:
    def __init__(self, name: str, code: str, node_category: node_category, EB_tracks: list[str], WB_tracks: list[str], latitude: float, longitude: float):
        self._name = name
        self._code = code
        self._node_category = node_category
        self._EB_tracks = EB_tracks
        self._WB_tracks = WB_tracks
        self._latitude = latitude
        self._longitude = longitude