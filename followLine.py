import ev3dev.ev3 as ev3
import threshold
thresh=threshold.main()

#config the motors and sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')
ts = ev3.TouchSensor()
assert ts.connected
cs = ev3.ColorSensor()
assert cs.connected
print(thresh)