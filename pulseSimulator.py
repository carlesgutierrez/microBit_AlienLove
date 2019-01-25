from microbit import *
import neopixel

def fadeInFadeOut(auxMinB1, auxMaxB1, auxMinB2, auxMaxB2, auxIncUp, auxIncDown, auxDelay):
    global bmodeA
    if button_a.is_pressed() and button_b.is_pressed():
        #Check anytime any moment this for quick exit
        bmodeA = bmodeA * -1
        print("chaging mode")
        return
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

# Vars MODE A removed
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

    if stat == 1:
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

    if stat == 2:
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

    if stat == 3:
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
    # print("myTimer = " + str(myTimer))

    return


def simulatorFade( _timeFading ):
    global bmodeA
    global minB
    global maxB

    display.show(Image.FABULOUS)

    if button_a.is_pressed() and button_b.is_pressed():
        #Check anytime any moment this for quick exit
        bmodeA = bmodeA * -1
        print("chaging mode")
        return

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

while True:

    # gesture = accelerometer.current_gesture()
    # if gesture == "face up":
    #     bmodeA = True
    #     print("Face UP")
    # else:
    #     bmodeA = False
    #     print("Face Down")

    if bmodeA == 1:
        print("bmodeA")
        simulatorPulseNeo( )
    else:
        print("bmodeB")
        simulatorFade( 2000 )