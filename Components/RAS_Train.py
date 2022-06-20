from RAS_Conversions import direction
from RAS_Conversions import train_category
from RAS_Event import Event


class Train(Event):
    def __init__(self, course_id: str, direction: direction, train_category: train_category, start_seconds: int, end_seconds: int, start_node: str, end_node: str):
        super(Train, self).__init__(direction, start_seconds, end_seconds, start_node, end_node)
        self._course_id = course_id
        self._train_category = train_category
    