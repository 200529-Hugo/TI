import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    for i in range(8):
        time.sleep(1)
        np[i] = [255, 0, 0]
        np.write()
        time.sleep(1)
        if i == 7:
            for j in range(8):
                np[j] = [0, 0, 0]
                np.write()
