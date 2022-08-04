## your welcome ##
## Team P455 ##
from djitellopy import tello
import KeyPressModule as kpm
import time, cv2


kpm.init()
me = tello.Tello()

me.connect()
print(me.get_battery())
me.streamon()


global img


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    # if kpm.getKey("w"): speed = 50
    # if kpm.getKey("x"): speed = 75
    
    ### Turbo mode #input# ###
    if kpm.getKey("c"): speed = 100

    if kpm.getKey("LEFT"): lr = -speed
    elif kpm.getKey("RIGHT"): lr = speed

    if kpm.getKey("UP"): fb = speed
    elif kpm.getKey("DOWN"): fb = -speed

    if kpm.getKey("z"): ud = speed
    elif kpm.getKey("s"): ud = -speed

    if kpm.getKey("q"): yv = -speed
    elif kpm.getKey("d"): yv = speed

    if kpm.getKey("i"): me.takeoff()
    elif kpm.getKey("k"): me.land(); time.sleep(3)

    if kpm.getKey("o"): me.streamon()
    elif kpm.getKey("l"): me.streamoff()

    if kpm.getKey("p"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)


    return[lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
