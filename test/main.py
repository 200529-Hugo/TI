import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)


def ledStrip(r, g, b):
    for i in range(8):
        if np[i][0] < r:
            np[i][0] += 1
        elif np[i][0] > r:
            np[i][0] -= 1

        if np[i][1] < g:
            np[i][1] += 1
        elif np[i][1] > g:
            np[i][1] -= 1

        if np[i][2] < b:
            np[i][2] += 1
        elif np[i][2] > b:
            np[i][2] -= 1

    np.write()
    time.sleep(0.01)


while True:
    ledStrip(255, 20, 200)
