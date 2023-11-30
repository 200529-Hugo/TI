from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.on()
    time.sleep(high_time)
    pin.off()
    time.sleep(low_time)


while True:
    pulse(gpio_pin, 0.2, 0.2)
