import pyautogui

def confirmBeforeTheRunning(msg) :
    return pyautogui.confirm("아래의 등록번호가 맞으면 \"예\"를 눌러주세요. \n" + msg, "등록번호 확인")

def sendAlertMessage(msg) :
    pyautogui.alert(msg)
    return