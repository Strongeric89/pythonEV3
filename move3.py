#!/usr/bin/env python3
import ev3dev.ev3 as ev3
#configuring motors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

count = int(0)
while(True):
    if(count == 10):
        break
    mA.run_forever(speed_sp=400)
    mB.run_forever(speed_sp=-400)
    ev3.Sound.speak(count).wait()
    count +=1
#if count reaches 10 stop the motors
mA.stop()
mB.stop()

