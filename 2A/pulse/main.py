from machine import ADC, PWM, Pin
import time

led = Pin(20, Pin.OUT)
adc = ADC(Pin(26))


def pulse(pin, high_time, low_time):
    pin.on()
    time.sleep(high_time)
    pin.off()
    time.sleep(low_time)


while True:
    adc_value = adc.read_u16()
    pulse(led, adc_value / 65535, 0.1)
    time.sleep(0.01)
