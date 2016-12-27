#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep
mB = LargeMotor('outB')
mA = LargeMotor('outA')

mB.run_forever(speed_sp=900)
sleep(5)
mB.stop(stop_action="hold")
sleep(5)

mA.run_forever(speed_sp=900)
sleep(5)
mA.stop(stop_action="hold")
sleep(5)