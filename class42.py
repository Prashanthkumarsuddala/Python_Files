import pyautogui

import time
time.sleep(1)
count = 0
while count<=10:
    pyautogui.typewrite('my python')
    pyautogui.press('Enter')
    count = count+1