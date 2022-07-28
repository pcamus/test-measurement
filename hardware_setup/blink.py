# File : blink.py
# Simple blink program to measure power consumption
# info@pcamus.be
# 20/7/2022

import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(5)