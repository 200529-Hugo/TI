#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op TI

Voorbeeld voor communicatie met Raspberry Pi Pico. Flash dit bestand
eerst naar de Raspberry Pi Pico. Start dan in de folder serial/PC-serial `main.py` op je laptop/PC.

(c) 2022 Hogeschool Utrecht,
Hagen Patzke (hagen.patzke@hu.nl) en
Tijmen Muller (tijmen.muller@hu.nl)
"""

from machine import Pin, ADC
import time

# Use on-board led
led = Pin(25, Pin.OUT)

# Configure ADC for reading the internal temperature sensor
adc = ADC(4)  # ADC channel 4 is connected to the internal temperature sensor


# Function to read temperature from the internal sensor
def read_temperature():
    temperature_voltage = adc.read_u16() * (3.3 / 65535.0)
    temperature = 27 - (temperature_voltage - 0.706) / 0.001721
    return temperature


# Blink the led to confirm successful flashing
for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)

# Wait for data from the connection
while True:
    data = input("Enter command (0: turn led off, 1: turn led on, 2: get temperature): ")

    print("Received '" + data + "'.")
    if data == '0':
        print("Turning led off.")
        led(0)
    elif data == '1':
        print("Turning led on.")
        led(1)
    elif data == '2':
        # Read and print temperature
        temperature = read_temperature()
        print("Temperature: {:.2f} °C".format(temperature))
    else:
        print("Unknown command.")
