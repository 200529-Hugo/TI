from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
adc = ADC(4)


def read_temperature():
    temperature_voltage = adc.read_u16() * (3.3 / 65535.0)
    temperature = 27 - (temperature_voltage - 0.706) / 0.001721
    return temperature


while True:
    temperature_celsius = read_temperature()

    lcd.move_to(0, 0)
    lcd.putstr("Temperature: \n")
    lcd.move_to(0, 1)
    lcd.putstr("{:.2f} C".format(temperature_celsius))

    utime.sleep(1)
