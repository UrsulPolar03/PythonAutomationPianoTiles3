# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, sys, os
import win32con


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixelMatchesColor(690, 400, (0, 0, 0)):
        click(690, 400)
    elif pyautogui.locateOnScreen('slide.png',region=(655,225,120,304), grayscale=True, confidence=.9):
        click(690, 400)


    if pyautogui.pixelMatchesColor(838, 400, (0, 0, 0)):
        click(838, 400)
    elif pyautogui.locateOnScreen('slide.png',region=(799,225,120,304), grayscale=True, confidence=.9):
        click(838, 400)


    if pyautogui.pixelMatchesColor(976, 400, (0, 0, 0)):
        click(976, 400)
    elif pyautogui.locateOnScreen('slide.png',region=(942,225,120,304), grayscale=True, confidence=.9):
        click(976, 400)


    if pyautogui.pixelMatchesColor(1125, 400, (0, 0, 0)):
        click(1125, 400)
    elif pyautogui.locateOnScreen('slide.png',region=(1087,225,120,304), grayscale=True, confidence=.9):
        click(1125, 400)


