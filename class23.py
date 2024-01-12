import pyautogui

import time
time.sleep(2)
count = 0
while count<=10:
    pyautogui.typewrite('Hello')
    pyautogui.press('Enter')
    count = count+1