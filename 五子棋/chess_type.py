from enum import IntEnum
class Chess_type(IntEnum):  # 棋型类
    Non = 0,
    Sleep_Two = 1,
    Live_Two = 2,
    Sleep_Three = 3,
    Live_Three = 4,
    Sleep_Four = 5,
    Live_Four = 6,
    Live_Five = 7

Five = Chess_type.Live_Five.value
Four, Three, Two = Chess_type.Live_Four.value, Chess_type.Live_Three.value, Chess_type.Live_Two.value
S_Four, S_Three, S_Two = Chess_type.Sleep_Four.value, Chess_type.Sleep_Three.value, Chess_type.Sleep_Two.value