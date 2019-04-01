import pyautogui
import time
import numpy as np
import pytesseract
from PIL import ImageGrab, Image
import cv2

def setup_match():
    #cut scene
    time.sleep(10)
    pyautogui.moveTo(2233, 623, 1, pyautogui.easeInQuad)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

    #select character
    time.sleep(1.5)
    pyautogui.moveTo(2104, 447, 1, pyautogui.easeInQuad)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

    #confirm loadout
    time.sleep(1)
    pyautogui.moveTo(2302, 370, 1, pyautogui.easeInQuad)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

def main():
    while True:
        x = 2845
        y = 937

        offx = 180
        offy = 32

        new_size_x = 300
        new_size_y = 100

        img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
        img = img.resize((new_size_x, new_size_y), Image.ANTIALIAS)

        img = np.array(img)

        if pytesseract.image_to_string(img) == "VOTE FOR RETRY":
            pyautogui.moveTo(2845, 937, 1, pyautogui.easeInQuad) 
            pyautogui.mouseDown()
            time.sleep(.2)
            pyautogui.mouseUp()
            setup_match()

        cv2.imshow('R6', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
