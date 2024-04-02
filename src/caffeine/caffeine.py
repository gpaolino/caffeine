import multiprocessing
import os
import time
from datetime import datetime
from random import randint

import PIL.Image
import pyautogui
import pystray

image = PIL.Image.open(os.path.join(os.path.abspath(os.curdir), '../images/coffee.png'))
running = False

def dont_sleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)

def on_clicked(icon, item):
    global t
    global running
    if str(item) == 'Stay Awake':
        t = multiprocessing.Process(target=dont_sleep)
        t.start()
        running = True
    elif str(item) == 'Stop':
        t.terminate()
        running = False
    elif str(item) == 'Exit':
        icon.stop()
    else:
        print('Not implemented yet!')

icon = pystray.Icon('Coffee', image, title='Caffeine', menu=pystray.Menu(
    pystray.MenuItem('Stay Awake', on_clicked, enabled=lambda item: not(running)),
    pystray.MenuItem('Stop', on_clicked, enabled=lambda item: running),
    pystray.MenuItem('Exit', on_clicked, enabled=lambda item: not(running))
))
