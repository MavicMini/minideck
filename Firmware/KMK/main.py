# You import all the IOs of your board
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros, tap, press, release

# Create keyboard instance
keyboard = KMKKeyboard()

# Add Macro module
macro = Macros()
keyboard.modules.append(macro)

# Define your keymaps
keyboard.keymap = [
    
        [KC.A, KC.B, KC.C, KC.D],
        [KC.E, KC.F, KC.G, KC.H],
        [KC.I, KC.J, KC.K, KC.L],
]

# Macros

# Open sound output selector (Ctrl + GUI + V)
keyboard.keymap[0][0] = KC.Macro(
    press(KC.LCTL),
    press(KC.LGUI),
    tap(KC.V),
    release(KC.LGUI),
    release(KC.LCTL),
)

# Lock PC (GUI + L)
keyboard.keymap[0][1] = KC.Macro(
    press(KC.LGUI),
    tap(KC.L),
    release(KC.LGUI),
)