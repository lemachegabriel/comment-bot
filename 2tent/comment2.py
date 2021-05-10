from pyautogui import * 
import pyautogui
import time 
import win32api, win32con

for i in range(5):
    print(i)
    time.sleep(1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def position():

#### 862 1027 ## 654 668
x,y = pyautogui.locateCenterOnScreen('2tent/comment.png', confidence=0.8)





       