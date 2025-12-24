import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    keyboard.col_pins = (board.GP29, board.GP6, board.GP7, board.GP0)
    keyboard.row_pins = (board.GP26, board.GP27, board.GP28)

    keyboard.diode_orientation = DiodeOrientation.ROW2COL