import time
import pyautogui
import pyperclip

def selectRelationTab(w) :
    w_width = w[0].size.width
    w_height = w[0].size.height
    start_x = w[0].left + 20
    start_y = w[0].top + 20
    region = (start_x, int(w_height/2), int(w_width/2), int(w_height/2))
    for i in pyautogui.locateAllOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/relationIngoIcon.png", confidence = 0.8, region = region):
        pyautogui.moveTo(i)
        pyautogui.move(50,0)
        pyautogui.click()
    
    return

def checkAlreadyHave(w) :
    time.sleep(0.25)
    w_width = w[0].size.width
    w_height = w[0].size.height
    start_x = w[0].left + 20
    start_y = w[0].top + 20
    
    if pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/NoneIntroTable.png") :
        return False
    else :
        return True
    
def openTextMagican(w) :
    w_width = w[0].size.width
    w_height = w[0].size.height
    start_x = w[0].left + 8
    start_y = w[0].top + w_height//2
    
    region = (start_x, start_y , w_width//2, w_height//2)
    textButton = pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/textButton.png", confidence = 0.9
                                          , region = region)
    
    pyautogui.click(textButton)
    pyautogui.rightClick()
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton_kor.png"), interval = 0.2)
    
    
    return
    
def saveInformation(bookIntro, tableContent, w) :
    pyautogui.PAUSE = 0.5

    if not bookIntro:
        return
    
    openTextMagican(w)
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/bookIntroButton.png"), interval = 0.2)
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton_kor.png"), interval = 0.2)
    
    w2 = pyautogui.getActiveWindow()
    pos_x = w2.left + (w2.size.width/2)
    pos_y = w2.top + (w2.size.height/2)
    pyautogui.click(pos_x, pos_y)
    pyperclip.copy(bookIntro)

    pyautogui.hotkey("ctrl", "v")    
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton_kor.png"), interval = 0.2)
    pyautogui.press("enter")


    if not tableContent:
        return

    print(tableContent)
    openTextMagican(w)
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/tableContentButton.png"), interval = 0.2)
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton_kor.png"), interval = 0.2)
    
    w2 = pyautogui.getActiveWindow()
    pos_x = w2.left + (w2.size.width/2)
    pos_y = w2.top + (w2.size.height/2)
    pyautogui.click(pos_x, pos_y)
    pyperclip.copy(tableContent)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(pyautogui.locateOnScreen("C:/Program Files (x86)/Sejong Library Automation/asset/nextButton_kor.png"), interval = 0.2)
    pyautogui.press("enter")
    
    return
