import pyautogui
import threading
import sys
import keyboard

pyautogui.FAILSAFE = True

def failsafe_0():
    pyautogui.moveTo(-1,-1)
    sys.exit()

running = True
mousemove_thread = None

def simple_movement():
    global running
    i = 0
    while running == True:
        pyautogui.moveRel(200, 0, duration=1)
        pyautogui.moveRel(0, -200, duration=1)
        pyautogui.moveRel(-200, 0, duration=1)
        pyautogui.moveRel(0, 200, duration=1)
        i += 1
        print("moved times", i)


def toggle_mouse():
    global running, mousemove_thread
    if not running:
        running = True
        mousemove_thread = threading.Thread(target=simple_movement)
        mousemove_thread.start()
        print("on")
    else:
        running = False
        print("off")


keyboard.add_hotkey('f', failsafe_0)
keyboard.add_hotkey('m',toggle_mouse)
keyboard.wait()

