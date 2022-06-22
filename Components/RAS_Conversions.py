from enum import Enum

#


class node_category(str, Enum):
    STATION = 'STATION'
    JUNCTION = 'JUNCTION'
    CONTRIL_POINT = 'CONTROL_POINT'

class activity_type(str, Enum):
    PASS = 'PASS'
    STOP = 'STOP'

class direction(str, Enum):
    WB = 'WB'
    EB = 'EB'
    BOTH = 'BOTH'

class train_category(str, Enum):
    OO = 'OO'
    EE = 'EE'
