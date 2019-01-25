from microbit import *
import neopixel
import random
import radio

# The radio won't work unless it's switched on.
radio.on()

def ifCoitusInterruptus():
    global bmodeA
    if button_a.was_pressed() and button_b.was_pressed():
        #Check anytime any moment this for quick exit
        bmodeA = bmodeA * -1
        print("chaging mode")
        return

def fadeInFadeOut(auxMinB1, auxMaxB1, auxMinB2, auxMaxB2, auxIncUp, auxIncDown, auxDelay):
    ifCoitusInterruptus()
    for i in range(auxMinB1, auxMaxB1+1, auxIncUp):
        for led_id in range(len(np)):
            np[led_id] = (i, 0, 0)
        np.show()
        sleep(auxDelay)
    # fade out counterPeriod/2
    for i in range(auxMaxB2, auxMinB2, -auxIncDown):
        for led_id in range(len(np)):
            np[led_id] = (i, 0, 0)
        np.show()
        sleep(auxDelay)


flatSignal = Image("00000:"
             "05000:"
             "55555:"
             "00050:"
             "00000")

display.show(Image.HEART)

np = neopixel.NeoPixel(pin1, 8)



# Vars MODEA
bmodeA = 1
timePulse = 1000
myTimer = 0
lastTimer = 0
myMillis = running_time()
# Vars MODE B removed
minB = 0
maxB = 255

def simulatorPulseNeo( ):
    global timePulse
    global myTimer
    global lastTimer
    global myMillis

    # Vars MODE A
    nextDelay = 0
    stat = 1

    if stat == 1 and bmodeA == 1:
        display.show(Image.HEART)
        minB1 = 10
        maxB1 = 255
        minB2 = 0
        maxB2 = 155
        nextIncUp = 10
        nextIncDown = 10
        nextDelay = 0
        # print('stat1 nextIncUp = '+str(nextIncUp)+'\n')
        fadeInFadeOut(minB1, maxB1, minB2, maxB2, nextIncUp, nextIncDown, nextDelay)
        stat = 2

    if stat == 2 and bmodeA == 1:
        display.show(Image.HEART_SMALL)
        minB1 = 10
        maxB1 = 255
        minB2 = 0
        maxB2 = 155
        nextIncUp = 10
        nextIncDown = 7
        nextDelay = 0
        # print('stat2 nextIncUp = '+str(nextIncUp)+'\n')
        fadeInFadeOut(minB1, maxB1, minB2, maxB2, nextIncUp, nextIncDown, nextDelay)
        stat = 3

    if stat == 3 and bmodeA == 1:
        display.show(flatSignal)
        for i in range(len(np)):
            np[i] = (0, 0, 0)
        np.show()
        sleep(timePulse)
        stat = 0

    if button_a.get_presses() > 0:
        timePulse = timePulse *0.5
        print("timePulse = " + str(timePulse))

    if button_b.get_presses() > 0:
        timePulse = timePulse *2
        print("timePulse = " + str(timePulse))

    # update elapsed time since last interaction
    lastTimer = myTimer
    myTimer = myMillis - lastTimer
    print("myTimer = " + str(myTimer))

    return

# Vars MODEB
timeFading = 2000

def simulatorFade( _timeFading ):
    global bmodeA
    global minB
    global maxB

    ifCoitusInterruptus()

    # fade in
    for i in range(minB, maxB+1, 1):
        for led_id in range(len(np)):
            np[led_id] = (i, 0, 0)
        np.show()
        sleep(10)

    # fade out
    for i in range(maxB, minB, -1):
        for led_id in range(len(np)):
            np[led_id] = (i, 0, 0)
        np.show()
        sleep(10)

    # clear
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

    return

# my alien vars comunication
myLastReceivedRadio = running_time()

while True:

    # After a while without interaction comeback to standby
    if (running_time() - myLastReceivedRadio) > 10000:
        bmodeA = 0
        timePulse = 1000

    if bmodeA == 1:
        print("bmodeA")
        simulatorPulseNeo( )
    else:
        print("bmodeB")
        simulatorFade( timeFading )

    # If receive Pulse Radio "alienBeat_0" then change to this behauviour while is receiving this input
    # incoming = radio.receive()
    incoming = radio.receive_full()
    if incoming == 'alienBeat_0':
        print("received alienBeat_0")
        receivedPuseTimeGap = running_time() - myLastReceivedRadio
        if receivedPuseTimeGap < 20000 and receivedPuseTimeGap > 300:
            # a credible pulse received
            timePulse = receivedPuseTimeGap

        myLastReceivedRadio = running_time()
        bmodeA = 1

