from RAS_Conversions import activity_type

class MinRunTime:
    def __init__(self, link_start_node: str, link_end_node: str, start_activity: activity_type, end_activity: activity_type, min_run_time_seconds: int):
        self._link_start_node = link_start_node
        self._link_end_node = link_end_node
        self._start_activity = start_activity
        self._end_activity = end_activity
        self._min_run_time_seconds = min_run_time_seconds
