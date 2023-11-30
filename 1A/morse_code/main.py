from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.on()
    time.sleep(high_time)
    pin.off()
    time.sleep(low_time)


def morse(pin, dot_length, text):
    for c in text:
        if c == ".":
            pulse(pin, dot_length, dot_length)
        elif c == "-":
            pulse(pin, 3 * dot_length, dot_length)
        elif c == " ":
            time.sleep(4 * dot_length)


morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")
