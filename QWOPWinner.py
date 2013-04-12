import time

def takeStep(leg, stepTime):
    ''' Takes a step on the leg that was passed
        leg: string, either left or right
        time: float, number of seconds to step
    '''

    if (leg='left'):
        #TODO press left leg keys

    if (leg='right'):
        #TODO press right leg keys

    time.sleep(stepTime)

def winQWOP():
    stepTime = 1.1
    for i in range(100):
        takeStep(left, stepTime)
        takeStep(right, stepTime)

print "Starting QWOP winner in 5 seconds..."
time.sleep(5)

winQWOP()
