from RAS_Conversions import direction

class Link:
    def __init__(self, start_node: str, end_node: str, direction: direction, distance_meters: int):
        self._start_node = start_node
        self._end_node = end_node
        self._direction = direction
        self._distance_meters = distance_meters
