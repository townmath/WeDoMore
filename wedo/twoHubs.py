import wedo

UNAVAILABLE = None
TILTSENSOR = (38, 39)
DISTANCESENSOR = (176, 177, 178, 179)
#more MOTOR values pop up when two hubs are attached
MOTOR = (0, 1, 2, 3, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240)

#sometimes this gives an error, but doesn't seem to affect performance
def initTwoHubs (): #initialize 2 hubs
    wd1 = wedo.WeDo()
    wd2 = wedo.WeDo()
    wd2.dev=wedo.scan_for_devices()[1]
    wd1.init_device()
    wd2.init_device()
    return (wd1,wd2) # it works!

#the easiest thing is to have one motor hub and one sensor hub
def motorOrSensor((wd1,wd2)): #returns motor hub first, sensor second
    wd1Data= wd1.getData().keys()
    wd2Data= wd2.getData().keys()
    if wd1Data[0] not in MOTOR and wd2Data[0] not in MOTOR:
        print 'no motor hub'
        print wd1Data, wd2Data #for debugging
    for keys in wd1Data:
        if keys in TILTSENSOR or keys in DISTANCESENSOR:
            return (wd2,wd1)
    for keys in wd2Data:
        if keys in TILTSENSOR or keys in DISTANCESENSOR:
            return (wd1,wd2)
    print 'no sensor hub'
    print wd1Data, wd2Data # for debugging
    return (UNAVAILABLE,UNAVAILABLE)
