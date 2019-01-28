from microbit import *
import radio
import random

# General Vars to send to all 7 microbits
nextMicroBit_Id = 0
noOneThereTime = 0

# Pulse to Send
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

def chooseNewIdUp():
    global nextMicroBit_Id
    global noOneThereTime
    noOneThereTime = running_time()
    nextMicroBit_Id = nextMicroBit_Id+1
    if nextMicroBit_Id > 4:
        nextMicroBit_Id = 0
    print("Next ID Up ",nextMicroBit_Id)

def chooseNewIdDown():
    global nextMicroBit_Id
    global noOneThereTime
    noOneThereTime = running_time()
    nextMicroBit_Id = nextMicroBit_Id-1
    if nextMicroBit_Id < 0:
        nextMicroBit_Id = 4
    print("Next ID Down ",nextMicroBit_Id)

def chooseNewIdRandom():
    global nextMicroBit_Id
    global noOneThereTime
    noOneThereTime = running_time()
    nextMicroBit_Id = random.randint(0,4)
    print("Next ID Random ",nextMicroBit_Id)

def sendRadioPulse():
    global timeEllapsedPulse
    display.show(nextMicroBit_Id)
    timeEllapsedPulse = running_time()
    radio.send("alienBeat_"+str(nextMicroBit_Id))
    print("alienBeat_"+str(nextMicroBit_Id)+" at ", running_time())

while True:
    if button_a.was_pressed():
        chooseNewIdDown()

    if button_b.was_pressed():
        chooseNewIdUp()

    if pin1.read_digital():
        noOneThereTime = running_time()
        display.show(Image.HEART)
        if (running_time() - timeEllapsedPulse) > 700:
            sendRadioPulse()
        else:
            print("Filtering too quick pulse")

    else:
        display.show(nextMicroBit_Id)
        if (running_time() - noOneThereTime) > 7000:
            # choose new ID
            chooseNewIdRandom()