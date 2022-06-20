from RAS_Conversions import direction


class Event:
    def __init__(self, direction: direction, start_seconds: int, end_seconds: int, start_node: str, end_node: str):
        self._direction = direction
        self._start_seconds = start_seconds
        self._end_seconds = end_seconds
        self._start_node = start_node
        self._end_node = end_node
