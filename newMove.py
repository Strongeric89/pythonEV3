#!/bin/env python3
from ev3dev.ev3 import *
#new move by eric strong
mA = LargeMotor('outA')
mB = LargeMotor('outB')
mA.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
mB.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")

print("set speed (speed) = " + str(mA.speed_sp))
