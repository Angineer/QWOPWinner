import time
import uinput

events = (uinput.KEY_Q, uinput.KEY_W, uinput.KEY_O, uinput.KEY_P)
device = uinput.Device(events)

def takeStep(leg, stepTime):
    ''' Takes a step on the leg that was passed
        leg: string, either left or right
        time: float, number of seconds to step
    '''

    if (leg=='left'):
        device.emit(uinput.KEY_W, 1)
        device.emit(uinput.KEY_O, 1)

    if (leg=='right'):
        device.emit(uinput.KEY_Q, 1)
        device.emit(uinput.KEY_P, 1)

    time.sleep(stepTime/2)

    device.emit(uinput.KEY_W, 0)
    device.emit(uinput.KEY_O, 0)
    device.emit(uinput.KEY_Q, 0)
    device.emit(uinput.KEY_P, 0)

    time.sleep(stepTime/2)

def winQWOP():
    takeStep("left", 0.8)
    stepTime = 2.0
    for i in range(5):
        takeStep("left", stepTime)
        takeStep("right", stepTime)

print "Starting QWOP winner in 5 seconds..."
time.sleep(5)

winQWOP()
