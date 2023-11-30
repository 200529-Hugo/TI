from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
onBtn = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
offBtn = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

led_pin.value(0)
while True:
    if onBtn.value():
        led_pin.value(1)
    elif offBtn.value():
        led_pin.value(0)
    time.sleep(0.1)
