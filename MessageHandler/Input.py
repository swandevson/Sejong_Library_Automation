import pyautogui

def checkLength(number) :
    if  len(str(number)) is not 12 :
        raise ValueError
    
    return

def checkFrontFormat(number) :
    for i in range(0,6) : 
        if number[i] is not '0' :
            raise ValueError
    return

def isValidNumber(number) :
    checkLength(number)    
    checkFrontFormat(number[0 : 6])
    return 

def getStartRegistNumber() :
    return inputRegistNummber("시작번호")
    
def getEndRegistNumber() :
    return inputRegistNummber("끝번호")

def inputRegistNummber(position):
    msg = None
    prompt_title = "등록번호 {} 입력".format(position)
    prompt_content = "작업할 등록번호 범위의 {} 12자리를 입력하세요.\n 등록번호는 앞\"0\" 6개, 등록번호 6개입니다.".format(position)
    
    while True : 
        result = pyautogui.prompt(prompt_content, prompt_title, msg)
        if result is None :
            return result
        
        try :
            isValidNumber(result)
            return result
        except :
            msg = "등록번호를 정확히 입력하세요"
            continue
