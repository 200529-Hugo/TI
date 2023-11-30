from machine import Pin
import time
import random

ledR = Pin(20, Pin.OUT)
ledB = Pin(21, Pin.OUT)
ledG = Pin(22, Pin.OUT)
ledY = Pin(19, Pin.OUT)

# 16 is forbidden
btnR = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)
btnB = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
btnG = Pin(14, Pin.IN, pull=Pin.PULL_DOWN)
btnY = Pin(13, Pin.IN, pull=Pin.PULL_DOWN)


def showColor(color):
    if color == 0:
        ledR.value(1)
    elif color == 1:
        ledB.value(1)
    elif color == 2:
        ledG.value(1)
    elif color == 3:
        ledY.value(1)


def showRememberColor(colors):
    for i in colors:
        showColor(i)


def turnOff():
    ledR.value(0)
    ledB.value(0)
    ledG.value(0)
    ledY.value(0)


turnOff()

while True:
    if btnR.value():
        ledR.value(1)
    elif btnB.value():
        ledB.value(1)
    elif btnG.value():
        ledG.value(1)
    elif btnY.value():
        ledY.value(1)
    else:
        turnOff()


rememberColor = []

turnOff()
exit()

while True:
    randomColor = random.randrange(0, 4)
    rememberColor.append(randomColor)
    showColor(randomColor)

    time.sleep(5)
    turnOff()
    time.sleep(5)

    while True:
        if btnR.value():
            showColor(0)
            time.sleep(0.1)
            turnOff()
            if randomColor == 0:
                break
        elif btnB.value():
            showColor(1)
            time.sleep(0.1)
            turnOff()
            if randomColor == 1:
                break
        elif btnG.value():
            showColor(2)
            time.sleep(0.1)
            turnOff()
            if randomColor == 2:
                break
        elif btnY.value():
            showColor(3)
            time.sleep(0.1)
            turnOff()
            if randomColor == 3:
                break

    if len(rememberColor) == 4:
        break

showRememberColor(rememberColor)
