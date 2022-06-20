from RAS_Conversions import activity_type

class MinRunTime:
    def __init__(self, link_start_node: str, link_end_node: str, start_activity_front: activity_type, end_activity_front: activity_type, start_activity_behind: activity_type, end_activity_behind: activity_type,min_headway_seconds: int):
        self._link_start_node = link_start_node
        self._link_end_node = link_end_node
        self._start_activity_front = start_activity_front
        self._end_activity_front = end_activity_front
        self._start_activity_behind = start_activity_behind
        self._end_activity_behind = end_activity_behind
        self._min_headway_seconds = min_headway_seconds