from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.on()
    time.sleep(high_time)
    pin.off()
    time.sleep(low_time)


short = 0.5
long = 2

while True:
    for i in range(3):
        pulse(gpio_pin, short, short)

    pulse(gpio_pin, long, long)
