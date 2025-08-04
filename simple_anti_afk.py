import keyboard
import time
import sys
import threading

running = False
spam_thread = None

def spam():
    keys = ['w','a','s','d']
    i = 0
    keyboard.press('shift') #camera lock for roblox
    while running == True:
        key = keys[i % 4]
        keyboard.press(key)
        time.sleep(0.2)
        keyboard.release(key)
        time.sleep(0.2)
        i += 1
def toggle_spam():
    global running, spam_thread
    if running:
        running = False
        print("off")
    else:
        running = True
        print("on")
        spam_thread = threading.Thread(target=spam)
        spam_thread.start()


def emergency_exit():
    global running
    print("get me out of here")
    running = False
    sys.exit()

keyboard.add_hotkey('p', toggle_spam)
keyboard.add_hotkey('l', emergency_exit)
keyboard.wait()
