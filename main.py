import pyautogui
import time
import numpy as np
import pytesseract
from PIL import ImageGrab, Image
from tkinter import Tk, Scale, Label, HORIZONTAL
import json
import cv2
from win32api import GetSystemMetrics

root = Tk()

def setup_match(data):
    #cut scene
    time.sleep(10)
    pyautogui.moveTo(data['spawnx'], data['spawny'], 1, pyautogui.easeInQuad)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

    #select character
    time.sleep(1.5)
    pyautogui.moveTo(data['characterx'], data['charactery'], 1, pyautogui.easeInQuad)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

    #confirm loadout
    time.sleep(1)
    pyautogui.moveTo(data['confirmx'], data['confirmy'], 1, pyautogui.easeInQuad)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

def main():
    data = {}
    with open('config.json') as json_file:  
        data = json.load(json_file)
    w = Label(root, text="Retry Coordinates")
    w.pack()
    w = Label(root, text="X Retry Button")
    w.pack()
    w1 = Scale(root, from_=0, to=GetSystemMetrics(0), orient=HORIZONTAL)
    w1.pack()
    w1.set(data['x'])
    w = Label(root, text="Y Retry Button")
    w.pack()
    w2 = Scale(root, from_=0, to=GetSystemMetrics(1), orient=HORIZONTAL)
    w2.set(data['y'])
    w2.pack()


    w = Label(root, text="Level Spawn Coordinates")
    w.pack()
    w = Label(root, text="X Level Button")
    w.pack()
    w3 = Scale(root, from_=0, to=GetSystemMetrics(0), orient=HORIZONTAL)
    w3.pack()
    w3.set(data['spawnx'])
    w = Label(root, text="Y Level Button")
    w.pack()
    w4 = Scale(root, from_=0, to=GetSystemMetrics(1), orient=HORIZONTAL)
    w4.pack()
    w4.set(data['spawny'])

    w = Label(root, text="Character Selection Coordinates")
    w.pack()
    w = Label(root, text="X Character Button")
    w.pack()
    w5 = Scale(root, from_=0, to=GetSystemMetrics(0), orient=HORIZONTAL)
    w5.pack()
    w5.set(data['characterx'])
    w = Label(root, text="Y Character Button")
    w.pack()
    w6 = Scale(root, from_=0, to=GetSystemMetrics(1), orient=HORIZONTAL)
    w6.pack()
    w6.set(data['charactery'])

    w = Label(root, text="Confirm Loadout Coordinates")
    w.pack()
    w = Label(root, text="X Loadout Button")
    w.pack()
    w7 = Scale(root, from_=0, to=GetSystemMetrics(0), orient=HORIZONTAL)
    w7.pack()
    w7.set(data['confirmx'])
    w = Label(root, text="Y Loadout Button")
    w.pack()
    w8 = Scale(root, from_=0, to=GetSystemMetrics(1), orient=HORIZONTAL)
    w8.pack()
    w8.set(data['confirmy'])

    while True:
        real_data = {}
        with open('config.json') as json_file:  
            real_data = json.load(json_file)
        root.update()
        x = w1.get()
        y = w2.get()

        data['x'] = w1.get()
        data['y'] = w2.get()
        data['spawnx'] = w3.get()
        data['spawny'] = w4.get()
        data['characterx'] = w5.get()
        data['charactery'] = w6.get()
        data['confirmx'] = w7.get()
        data['confirmy'] = w8.get()

        with open('config.json', 'w') as outfile:  
            json.dump(data, outfile)

        offx = 180
        offy = 32
        
        new_size_x = 300
        new_size_y = 100

        img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
        img = img.resize((new_size_x, new_size_y), Image.ANTIALIAS)
        img2 = ImageGrab.grab(bbox=(real_data['spawnx'], real_data['spawny'], real_data['spawnx'] + 100, real_data['spawny'] + 100))
        img3 = ImageGrab.grab(bbox=(real_data['characterx'], real_data['charactery'], real_data['characterx'] + 100, real_data['charactery'] + 100))
        img4 = ImageGrab.grab(bbox=(real_data['confirmx'], real_data['confirmy'], real_data['confirmx'] + 100, real_data['confirmy'] + 100))

        img = np.array(img)
        img2 = np.array(img2)
        img3 = np.array(img3)
        img4 = np.array(img4)

        if pytesseract.image_to_string(img) == "VOTE FOR RETRY":
            pyautogui.moveTo(data['x'], data['y'], 1, pyautogui.easeInQuad) 
            pyautogui.mouseDown()
            time.sleep(.2)
            pyautogui.mouseUp()
            setup_match(real_data)

        cv2.imshow('Retry Window', img)
        cv2.imshow('Level', img2)
        cv2.imshow('Character', img3)
        cv2.imshow('Confirm', img4)


        if cv2.waitKey(1) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
