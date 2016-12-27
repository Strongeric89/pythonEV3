#!/usr/bin/env python3
#The following program is a simple program that gets a dark and bright value to the robot can follow a line
import ev3dev.ev3 as ev3
#config the motors and sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')
ts = ev3.TouchSensor('in4')
cs = ev3.ColorSensor('in1')
cs.mode='COL-AMBIENT'

def getValue(option):
    if(option == 1):
        ev3.Sound.speak('press touch sensor when on bright color').wait()
        while not (ts.value()):
            value = int(cs.value())
            print('the bright value is ' + str(value))
            ev3.Sound.speak('the bright value is ' + str(value))
            return value
    else :
        ev3.Sound.speak('press touch sensor when on dark color').wait()
        while not (ts.value()):
            value = int(cs.value())
            print('the dark value is ' + str(value))
            ev3.Sound.speak('the dark value is ' + str(value))
            return value

#main
ev3.Sound.speak('get brigth value').wait()
bright = getValue(1)
ev3.Sound.speak('get dark value').wait()
dark = getValue(2)

#get threshold value
threshold = int((bright + dark) / 2)
ev3.Sound.speak('The threshold value is ' + str(threshold))