#!/usr/bin/env python3
"""
Example usage of the ODrive python library to monitor and control ODrive devices
"""

from __future__ import print_function

import odrive
from odrive.enums import *
from walking import walking
import time
import math

# Find a connected ODrive (this will block until you connect one)
#initial commit test
print("finding an odrive...")
my_drive = odrive.find_any()

# Find an ODrive that is connected on the serial port /dev/ttyUSB0
#my_drive = odrive.find_any("serial:/dev/ttyUSB0")

# Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

while my_drive.axis1.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# To read a value, simply read the property
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")

# Or to change a value, just assign to the property
my_drive.axis0.controller.pos_setpoint = 3.14
my_drive.axis1.controller.pos_setpoint = 3.14
print("Position setpoint is " + str(my_drive.axis0.controller.pos_setpoint))

# And this is how function calls are done:
for i in [1,2,3,4]:
    print('voltage on GPIO{} is {} Volt'.format(i, my_drive.get_adc_voltage(i)))

#my_drive.axis0.motor.config.current_lim = 75
#my_drive.axis0.controller.config.vel_limit = 64000
#my_drive.axis1.motor.config.current_lim = 75
#my_drive.axis1.controller.config.vel_limit = 64000

# Testing speed settings 
# my_drive.axis0.controller.vel_setpoint = 3000 * 2*3.14/60 

# A sine wave to test
t0 = time.monotonic()
while True:

##################NEW Velocity Setting ##############################
#
#    print("New Velocity: 64000")
#    my_drive.axis0.controller.config.vel_limit = 140000
#    my_drive.axis1.controller.config.vel_limit = 140000
#
##    setpoint = 10000.0 * math.sin((time.monotonic() - t0)*2)
#    for i in range(10):
#      my_drive.axis0.controller.pos_setpoint = 5000 
#      my_drive.axis1.controller.pos_setpoint = 5000
#      print("8000")
#      time.sleep(.05)
#      print("0")
#      my_drive.axis0.controller.pos_setpoint = 0
#      my_drive.axis1.controller.pos_setpoint = 0
#      time.sleep(.05)
#      print("8000")
#
# 
#
###################NEW Velocity Setting ##############################
#
#    my_drive.axis0.controller.config.vel_limit = 32000
#    print("New Velocity: 32000")
#    for i in range(4):
#      my_drive.axis0.controller.pos_setpoint = 8000
#      my_drive.axis1.controller.pos_setpoint = 8000
#      print("8000")
#      time.sleep(.25)
#    for x in range(4):
#      print("0")
#      my_drive.axis0.controller.pos_setpoint = 0
#      my_drive.axis1.controller.pos_setpoint = 0
#      time.sleep(.25)
#    for x in range(4):
#      print("8000")
#      my_drive.axis0.controller.pos_setpoint = 8000
#      my_drive.axis1.controller.pos_setpoint = 8000
#      time.sleep(.25)
#    for x in range(4):
#      print("0")
#      my_drive.axis0.controller.pos_setpoint = 0
#      my_drive.axis1.controller.pos_setpoint = 0
#      time.sleep(.25)
#
##################NEW Velocity Setting ##############################

    my_drive.axis0.controller.config.vel_limit = 16000
    my_drive.axis1.controller.config.vel_limit = 16000

    print("New Velocity: 16000")
    for i in range(4):
      my_drive.axis0.controller.pos_setpoint = 8000
      my_drive.axis1.controller.pos_setpoint = 8000
      print("8000")
      time.sleep(.25)
    for x in range(4):
      print("0")
      my_drive.axis0.controller.pos_setpoint = 0
      my_drive.axis1.controller.pos_setpoint = 0
      time.sleep(.25)
    for x in range(4):
      print("8000")
      my_drive.axis0.controller.pos_setpoint = 8000
      my_drive.axis1.controller.pos_setpoint = 8000
      time.sleep(.25)
    for x in range(4):
      print("0")
      my_drive.axis0.controller.pos_setpoint = 0
      my_drive.axis1.controller.pos_setpoint = 0
      time.sleep(.25)


##################NEW Setting ##############################

    my_drive.axis0.controller.config.vel_limit = 80000
    my_drive.axis1.controller.config.vel_limit = 80000
    print("New Velocity: 64000")
    my_drive.axis0.controller.pos_setpoint = 1000
    my_drive.axis1.controller.pos_setpoint = 1000
    print("1000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 2000
    my_drive.axis1.controller.pos_setpoint = 2000
    print("2000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 3000
    my_drive.axis1.controller.pos_setpoint = 3000
    print("3000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 4000
    my_drive.axis1.controller.pos_setpoint = 4000
    print("4000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 5000
    my_drive.axis1.controller.pos_setpoint = 5000
    print("5000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 6000
    my_drive.axis1.controller.pos_setpoint = 6000
    print("6000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 7000
    my_drive.axis1.controller.pos_setpoint = 7000
    print("7000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)


#################CounterClockWise########

    my_drive.axis0.controller.pos_setpoint = 7000
    my_drive.axis1.controller.pos_setpoint = 7000
    print("7000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 6000
    my_drive.axis1.controller.pos_setpoint = 6000
    print("6000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 5000
    my_drive.axis1.controller.pos_setpoint = 5000
    print("5000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 4000
    my_drive.axis1.controller.pos_setpoint = 4000
    print("4000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 3000
    my_drive.axis1.controller.pos_setpoint = 3000
    print("3000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 2000
    my_drive.axis1.controller.pos_setpoint = 2000
    print("2000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 1000
    my_drive.axis1.controller.pos_setpoint = 1000
    print("1000")
    time.sleep(2)


################Horses########

    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 7000
    my_drive.axis1.controller.pos_setpoint = 7000
    print("7000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 6000
    my_drive.axis1.controller.pos_setpoint = 6000
    print("6000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 5000
    my_drive.axis1.controller.pos_setpoint = 5000
    print("5000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 4000
    my_drive.axis1.controller.pos_setpoint = 4000
    print("4000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 3000
    my_drive.axis1.controller.pos_setpoint = 3000
    print("3000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 2000
    my_drive.axis1.controller.pos_setpoint = 2000
    print("2000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 8000
    my_drive.axis1.controller.pos_setpoint = 8000
    print("8000")
    time.sleep(.25)
    my_drive.axis0.controller.pos_setpoint = 1000
    my_drive.axis1.controller.pos_setpoint = 1000
    print("1000")
    time.sleep(2)

# Some more things you can try:

# Write to a read-only property:
my_drive.vbus_voltage = 11.0  # fails with `AttributeError: can't set attribute`

# Assign an incompatible value:
my_drive.motor0.pos_setpoint = "I like trains"  # fails with `ValueError: could not convert string to float`
