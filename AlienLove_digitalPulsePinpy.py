from microbit import *
import radio

diff_ElapsedPulse = 0
timeEllapsedPulse = 0
last_timeEllapsedPulse = 0
pulseRead = 0
display.show(Image.HEART)
counterRead = 0

# The radio won't work unless it's switched on.
radio.on()
radio.config(channel=19)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strengt

while True:
    if pin1.read_digital():
        print("pin dig 1")
        display.show(Image.HEART)
        if (running_time() - timeEllapsedPulse) > 700:
            display.show(0)
            timeEllapsedPulse = running_time()
            radio.send('alienBeat_0')
            print("send alienBeat_0 at ", running_time())
    else:
        display.show(Image.HEART_SMALL)