#!/bin/env python3
from ev3dev.ev3 import *
#configuring motors
mA = LargeMotor('outA')
mB = LargeMotor('outB')


while(True):

	mA.run_forever(speed_sp=400)
	mB/run_forever(speed_sp=400)
