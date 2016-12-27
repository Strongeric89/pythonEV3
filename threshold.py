#!/usr/bin/env python3
#The following program is a simple program that gets a dark and bright value to the robot can follow a line
import ev3dev.ev3 as ev3
#config the motors and sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')
ts = ev3.TouchSensor()
assert ts.connected
cs = ev3.ColorSensor()
assert cs.connected

def getValue(option):
    if(option == 1):
        ev3.Sound.speak('press touch sensor when on bright color').wait()
        while not (ts.value() == 1):
            value = cs.value()
            print('the bright value is ' + str(value))
            ev3.Sound.speak('the bright value is ' + str(value)).wait()
            return value
    else :
        ev3.Sound.speak('press touch sensor when on dark color').wait()
        while (ts.value() ==1 ):
            value = cs.value()
            print('the dark value is ' + str(value))
            ev3.Sound.speak('the dark value is ' + str(value)).wait()
            return value

#main
ev3.Sound.speak('get brigth value').wait()
bright = float(getValue(1))
ev3.Sound.speak('get dark value').wait()
dark = float(getValue(2))

#get threshold value
threshold = float((bright + dark) / 2)
print('threshold =' + str(threshold))
ev3.Sound.speak('The threshold value is ' + str(threshold)).wait()