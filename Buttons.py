#!/usr/bin/env python3
import ev3dev.ev3 as ev3
speed = 100
def led():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)


def left(state):
    if state:
        print('Left button pressed')
        mA.run_to_rel_pos(position_sp="180", speed_sp=speed, stop_action="hold")
        ev3.Sound.speak('moving to the left').wait()
    else:
        print('Left button released')


def right(state):  # neater use of 'if' follows:
    print('Right button pressed' if state else 'Right button released')
    mB.run_to_rel_pos(position_sp="180", speed_sp=speed, stop_action="hold")
    ev3.Sound.speak('moving to the left').wait()


def up(state):
    print('Up button pressed' if state else 'Up button released')
    mA.run_to_rel_pos(position_sp="180", speed_sp=speed, stop_action="hold")
    mB.run_to_rel_pos(position_sp="180", speed_sp=speed, stop_action="hold")



def down(state):
    print('Down button pressed' if state else 'Down button released')
    mA.run_to_rel_pos(position_sp="180", speed_sp=-speed, stop_action="hold")
    mB.run_to_rel_pos(position_sp="180", speed_sp=-speed, stop_action="hold")




def enter(state):
    print('Enter button pressed' if state else 'Enter button released')


def backspace(state):
    print('Backspace button pressed' if state else 'Backspace button released')


#configuring motors
ts = ev3.TouchSensor()
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')
button = ev3.Button()
button.on_left = left
button.on_right = right
button.on_up = up
button.on_down = down
button.on_enter = enter
button.on_backspace = backspace

while(True):
    button.process()
