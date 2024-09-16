import pyautogui as gui
from datetime import datetime
import keyboard

while not keyboard.is_pressed('ESC'):
    if keyboard.is_pressed('SPACE'):
        x, y = gui.position()
        current_time = datetime.now()
        print(f"{current_time}: x pos is {x}, y pos is {y}")
        keyboard.wait('SPACE', suppress=True, trigger_on_release=True)