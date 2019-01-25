import radio
from microbit import *

dotSignalImage = Image("00000:"
             "00000:"
             "04440:"
             "04440:"
             "00000")

# The radio won't work unless it's switched on.
radio.on()

display.show(Image.PACMAN)

# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.is_pressed():
        radio.send('alienBeat_0')  # a-ha
        display.show(dotSignalImage)
    else:
        display.show(Image.PACMAN)
