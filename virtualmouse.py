"""import cv2
import keyboard
import HandTrackingModule as htm
import pyautogui
import pyautogui as mouse

cam = cv2.VideoCapture(0)
hand = htm.FindHands(detection_con=0.1, tracking_con=0.1)

mouse.FAILSAFE = False

while not keyboard.is_pressed("esc"):
    ret, img = cam.read()
    cv2.imshow("Hand", img)
    ret2,img2=cam.read()
    position1 = hand.getPosition(img=img, hand_no=1, indexes=[9])
    position2=hand.getPosition(img=img2,hand_no=1,indexes=[9])
    print(position1,position2)
    if position1!=[] and position2!=[]:
        x1, y1 = position1[0][0], position1[0][1]
        mouse.sleep(0.5)
        x2, y2 = position2[0][0], position2[0][1]
        xmouse, ymouse = mouse.position().x, mouse.position().y
        cv2.rectangle(img2, (x1, x2), (y1, y2), (255, 0, 0))
        cv2.imshow("hand2", img2)
        delx, dely = x2 - x1, y2 - y1
        mouse.moveTo(xmouse + delx*10, ymouse + dely*10)
        print(x1,x2,xmouse,ymouse,y1,y2,delx,dely)
    cv2.waitKey(1)


cam.release()
cv2.destroyAllWindows()

#method2

from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows
from keyboard import is_pressed
import HandTrackingModule as htm
from pyautogui import moveTo,position
import mouse

camera = VideoCapture(0)
hands = htm.FindHands(detection_con=0.5, tracking_con=0.5)

while not is_pressed("esc"):
    ret1, img1 = camera.read()
    ret2, img2 = camera.read()
    index1 = hands.getPosition(img=img1, indexes=[9], hand_no=0)
    index2 = hands.getPosition(img=img2, indexes=[9], hand_no=0)
    imshow(winname="hand1", mat=img1)
    imshow(winname="hand2", mat=img2)
    if index1 != [] and index2 != []:
        x1, y1, x2, y2 = index1[0][0], index1[0][1], index2[0][0], index2[0][1]
        mouse.move(x1*3,y1*3)
    waitKey(1)
camera.release()
destroyAllWindows()

#method3
from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows
from keyboard import is_pressed
import HandTrackingModule as htm
from pyautogui import moveTo,position

camera = VideoCapture(0)
hands = htm.FindHands(detection_con=0.5, tracking_con=0.5)
pyautogui.FAILSAFE=False

while not is_pressed("esc"):
    ret1, img1 = camera.read()
    ret2, img2 = camera.read()
    index1 = hands.getPosition(img=img1, indexes=[9], hand_no=0)
    index2 = hands.getPosition(img=img2, indexes=[9], hand_no=0)
    imshow(winname="hand1", mat=img1)
    imshow(winname="hand2", mat=img2)
    if index1 != [] and index2 != [] and not hands.middle_finger_up(img1,hand_no=0):
        x,y=position().x,position().y
        x1, y1, x2, y2 = index1[0][0], index1[0][1], index2[0][0], index2[0][1]
        delx, dely = x2 - x1, y2 - y1
        moveTo(x+delx,y+dely)
    waitKey(1)
camera.release()
destroyAllWindows()
"""
# attempt

import cv2
import pyautogui
from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows
from keyboard import is_pressed
import HandTrackingModule as htm
from pyautogui import move, click

camera = VideoCapture(0)
hands = htm.FindHands(detection_con=0.5, tracking_con=0.5)

pyautogui.FAILSAFE = False
while not is_pressed("esc"):
    ret1, img1 = camera.read()
    ret2, img2 = camera.read()
    index1 = hands.getPosition(img=img1, indexes=[8], hand_no=0)
    index2 = hands.getPosition(img=img2, indexes=[8], hand_no=0)
    for i, j in zip(index1, index2):
        cv2.rectangle(img1, i, j, color=(225, 0, 0), thickness=5)
        cv2.rectangle(img2, i, j, color=(225, 0, 0), thickness=5)
    imshow(winname="hand1", mat=img1)
    imshow(winname="hand2", mat=img2)
    waitKey(1)
    if not is_pressed("ctrl"):
        continue
    try:
        assert (hands.index_finger_up(img1, hand_no=0))
        x1, y1, x2, y2 = index1[0][0], index1[0][1], index2[0][0], index2[0][1]
        a, b = (x1, y1), (x2, y2)
        delx, dely = x2 - x1, y2 - y1
        move(delx * 8, dely * 4)
    except AssertionError:
        pass
    except IndexError:
        pass

camera.release()
destroyAllWindows()
