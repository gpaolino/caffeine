#!.venv\Scripts\pythonw.exe

import multiprocessing
from datetime import datetime
from random import randint
from time import sleep

import PIL.Image
import pystray
from pyautogui import moveTo

image = PIL.Image.open('images/coffee.png')
running = False

def infinite_loop():
    try:
        while True:
            x = randint(1,1000)
            y = randint(1,1000)
            moveTo(x,y)
            sleep(10)
    except KeyboardInterrupt:
        print('Loop stopped by keyboard interrupt!')

def on_clicked(icon, item):
    global t
    global running
    if str(item) == 'Stay Awake':
        t = multiprocessing.Process(target=infinite_loop)
        t.start()
        running = True
    elif str(item) == 'Stop':
        t.terminate()
        running = False
    elif str(item) == 'Exit':
        icon.stop()
    else:
        print('Not implemented yet!')

def main():
    icon = pystray.Icon('Coffee', image, title='Caffeine', menu=pystray.Menu(
        pystray.MenuItem('Stay Awake', on_clicked, enabled=lambda item: not(running)),
        pystray.MenuItem('Stop', on_clicked, enabled=lambda item: running),
        pystray.MenuItem('Exit', on_clicked, enabled=lambda item: not(running))
    ))
    icon.run()

if(__name__=='__main__'):
    main()
