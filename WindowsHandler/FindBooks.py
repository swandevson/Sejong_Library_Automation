import pyautogui
import time
import sys

def findRegistNumberCategory():
    w = pyautogui.getWindowsWithTitle("통합작업환경")
    print(w[0])
    region = (w[0].left+20, w[0].top+20, int(w[0].size.width/4), int(w[0].size.height/4))
    categoryBox = pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/categoryEssentialInitName.png"
                                             , confidence = 0.9
                                             , region = region )
    
    if categoryBox is None :
        pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/categoryExpander.png"
                                                , confidence = 0.9
                                                , region =region))
        pyautogui.move(0,200)
        while True :
            time.sleep(1)
            categoryBox = pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/categoryEssentialInitName.png"
                                                , confidence = 0.9
                                                , region = region)
            if categoryBox is not None :
                break
            pyautogui.scroll(500)
    return categoryBox

def putsRegistNumber(registNumberString) :
    
    categoryBox = findRegistNumberCategory()
    
    pyautogui.click(categoryBox)
    
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("back")
    pyautogui.typewrite(registNumberString)
    pyautogui.press("enter")
    return

def selectCheckBox(_cnt) :
    #체크박스 선택
    cnt = _cnt
    now_cnt = 0
    w = pyautogui.getWindowsWithTitle("통합작업환경")
    checkbox_region = (w[0].left+20, w[0].top + int(w[0].size.height/3), int(w[0].size.width/2), int(w[0].size.height/3*2))
    
    while now_cnt <= cnt :
        for i in pyautogui.locateAllOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/checkbox.png", confidence = 0.9, region = checkbox_region):
            pyautogui.click(i, duration=0.1)
            now_cnt += 1
        if now_cnt <= cnt :
            pyautogui.scroll(-500)
    return
