import pyautogui as gui
from datetime import datetime
import keyboard
import time

while not keyboard.is_pressed('ESC'):
    if keyboard.is_pressed('SPACE'):
        x, y = gui.position()
        current_time = datetime.now()
        print(f"{current_time}: x pos is {x}, y pos is {y}")
        while keyboard.is_pressed('SPACE'):
            junk = "do nothing"