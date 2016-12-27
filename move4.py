#!/usr/bin/env python3
import ev3dev.ev3 as ev3

def led():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
#configuring motors
ts = ev3.TouchSensor()
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')
button = ev3.Button()

count = int(0)
while(True):
    print("the robot has done " + str(count) + " turns")
    if ts.value():
        break
    elif button.any():
        break
    mA.run_forever(speed_sp=-400)
    mB.run_forever(speed_sp=400)
    ev3.Sound.speak(count).wait()
    led()
    count +=1
#if count reaches 10 stop the motors
mA.stop()
mB.stop()
#end program

