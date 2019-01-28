from microbit import *
import neopixel
import random
import radio

# The radio won't work unless it's switched on.
radio.on()
radio.config(channel=19)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strengt

#General Vars
np = neopixel.NeoPixel(pin1, 8)
incoming = radio.receive()
idGeneral = 4
tagReveicer = 'alienBeat_'+str(idGeneral)

#0 (rojo) #1 (verde) #2(azul) #(3)amarillo #4(turquesa) #5(lila)
idColorType = 2

def receiveRadioBehauviour():
    global bmodeA
    global myLastReceivedRadio
    global incoming
    incoming = radio.receive()
    #incoming = radio.receive_full()
    if incoming is not None:
        if incoming == tagReveicer:
            print(incoming)
            myLastReceivedRadio = running_time()
            bmodeA = 1
            simulatorPulseNeo( )

def fadeInFadeOut(auxMinB1, auxMaxB1, auxMinB2, auxMaxB2, auxIncUp, auxIncDown, auxDelay):
    for i in range(auxMinB1, auxMaxB1+1, auxIncUp):
        for led_id in range(len(np)):
            if idColorType == 0:
                np[led_id] = (i, 0, 0) # rojo
            elif idColorType == 1:
                np[led_id] = (0, i, 0) # verde
            elif idColorType == 2:
                np[led_id] = (0, 0, i) # azul
            elif idColorType == 3:
                np[led_id] = (i, i, 0) # amarillo
            elif idColorType == 4:
                np[led_id] = (0, i, i) # turquesa
            elif idColorType == 5:
                np[led_id] = (i, 0, i) # lila
        np.show()
        sleep(auxDelay)
    # fade out counterPeriod/2
    for i in range(auxMaxB2, auxMinB2, -auxIncDown):
        for led_id in range(len(np)):
            if idColorType == 0:
                np[led_id] = (i, 0, 0) # rojo
            elif idColorType == 1:
                np[led_id] = (0, i, 0) # verde
            elif idColorType == 2:
                np[led_id] = (0, 0, i) # azul
            elif idColorType == 3:
                np[led_id] = (i, i, 0) # amarillo
            elif idColorType == 4:
                np[led_id] = (0, i, i) # turquesa
            elif idColorType == 5:
                np[led_id] = (i, 0, i) # lila
        np.show()
        sleep(auxDelay)


flatSignal = Image("00000:"
             "05000:"
             "55555:"
             "00050:"
             "00000")

display.show(idGeneral)

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
        print("Black ")
        #sleep(timePulse)
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
    print("Mode A myTimer = " + str(myTimer))

    return

# Vars MODEB
timeFading = 2000
simulatorPulseNeo()

def simulatorFade( _timeFading ):
    global minB
    global maxB

    display.show(idGeneral)

    if bmodeA == 0:
        # fade in
        for i in range(minB, maxB+1, 1):
            for led_id in range(len(np)):
                if idColorType == 0:
                    np[led_id] = (i, 0, 0) # rojo
                elif idColorType == 1:
                    np[led_id] = (0, i, 0) # verde
                elif idColorType == 2:
                    np[led_id] = (0, 0, i) # azul
                elif idColorType == 3:
                    np[led_id] = (i, i, 0) # amarillo
                elif idColorType == 4:
                    np[led_id] = (0, i, i) # turquesa
                elif idColorType == 5:
                    np[led_id] = (i, 0, i) # lila
            np.show()
            sleep(10)

    receiveRadioBehauviour()

    if bmodeA == 0:
        # fade out
        for i in range(maxB, minB, -1):
            for led_id in range(len(np)):
                if idColorType == 0:
                    np[led_id] = (i, 0, 0) # rojo
                elif idColorType == 1:
                    np[led_id] = (0, i, 0) # verde
                elif idColorType == 2:
                    np[led_id] = (0, 0, i) # azul
                elif idColorType == 3:
                    np[led_id] = (i, i, 0) # amarillo
                elif idColorType == 4:
                    np[led_id] = (0, i, i) # turquesa
                elif idColorType == 5:
                    np[led_id] = (i, 0, i) # lila
            np.show()
            sleep(10)

    receiveRadioBehauviour()

    # clear
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

    return


# my alien vars comunication
myLastReceivedRadio = running_time()

while True:

    receiveRadioBehauviour()

    # After a while without interaction comeback to standby
    if (running_time() - myLastReceivedRadio) > 10000:
        bmodeA = 0
        timePulse = 1000

    if bmodeA == 1:
        # print("bmodeA")
        # simulatorPulseNeo( )
        pass
    else:
        print("bmodeB")
        simulatorFade( timeFading )