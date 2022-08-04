from djitellopy import tello
import KeyPressModule as kpm
from time import sleep
import cv2

kpm.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kpm.getKey("LEFT"): lr = -speed
    elif kpm.getKey("RIGHT"): lr = speed

    if kpm.getKey("UP"): fb = speed
    elif kpm.getKey("DOWN"): fb = -speed

    if kpm.getKey("z"): ud = speed
    elif kpm.getKey("s"): ud = -speed

    if kpm.getKey("q"): yv = speed
    elif kpm.getKey("d"): yv = -speed

    if kpm.getKey("i"): me.takeoff()
    elif kpm.getKey("k"): me.land()

    return[lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
