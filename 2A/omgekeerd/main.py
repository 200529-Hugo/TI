from machine import ADC, PWM, Pin
import time

led = PWM(Pin(20))
led.freq(1000)

adc = ADC(Pin(26))


def led_brightness(value):
    percentage = value / 65535 * 100
    led.duty_u16(int(percentage * 65535 / 100))


def reverse_brightness(value):
    percentage = 100 - value / 65535 * 100
    led.duty_u16(int(percentage * 65535 / 100))


while True:
    adc_value = adc.read_u16()
    reverse_brightness(adc_value)
    time.sleep(0.01)
