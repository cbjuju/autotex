#!/usr/bin/python3
# something added

import pyautogui as pag
import time

theBrowser = [1700, 75]

def delay():
    time.sleep(1)

def browserFocus(n):
    for i in range(n): pag.hotkey('alt', 'tab')
    delay()
    pag.click(theBrowser)
