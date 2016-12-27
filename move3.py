#!/usr/bin/env python3
import ev3dev.ev3 as ev3
#configuring motors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

count = int(0)
while(True):
    mA.run_forever(speed_sp=400)
    mB.run_forever(speed_sp=-400)
    ev3.Sound.speak(count).wait()
    count +=1

