#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
#ev3.speaker.beep()

#we need two wheels an ultasocic and a bump (maybe)
right_wheel = Motor(Port.C)
left_wheel = Motor(Port.B)
distance_Sensor = UltrasonicSensor(Port.S1)
push_Sensor = TouchSensor(Port.S4)


def drive_fast(dist, speed):
    dist = dist * 10
    velocity = speed * (3.1415/180) * 26.5 #mm / sec
    print(velocity)
    run_time = dist/velocity
    print(run_time)
    right_wheel.run(speed)
    left_wheel.run(speed)
    wait(run_time * 1000)
    right_wheel.brake()
    left_wheel.brake()

def ranging(stopDist, speed):
    runningAverageData = []

    left_wheel.run(speed)
    right_wheel.run(speed)

    while True:
        print(distance_Sensor.distance())

        runningAverageData.append(distance_Sensor.distance())
        if(len(runningAverageData) > 30): runningAverageData.pop(0)

        if ((sum(runningAverageData)/len(runningAverageData)) <= stopDist*10):
            left_wheel.brake()
            right_wheel.brake()
            break

def bumping(speed):
    while True:
        right_wheel.run(speed)
        left_wheel.run(speed)

        if (push_Sensor.pressed()):
            left_wheel.brake()
            right_wheel.brake()
            drive_fast(-50, -speed)
            break


while(Button.CENTER not in ev3.buttons.pressed()):
    wait(100)
drive_fast(120, 500)
while(Button.CENTER not in ev3.buttons.pressed()):
    wait(100)
ranging(50, 200)
while(Button.CENTER not in ev3.buttons.pressed()):
    wait(100)
bumping(500)
