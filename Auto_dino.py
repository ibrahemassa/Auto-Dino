import pyautogui
import keyboard
import time

while True:  
    manager = pyautogui.screenshot()

    v = []
    curr_x = 250
    y_coordinates = [660, 650, 640, 630, 620]

    for x in range(15):
        for y in y_coordinates:               
            pixel_color = manager.getpixel((curr_x, y))
            v.append(pixel_color)
        curr_x -= 5

    if any(x != (32, 33, 36) for x in v):
        pyautogui.press('space')
        time.sleep(0.00001)



    if keyboard.is_pressed('z'):
        break