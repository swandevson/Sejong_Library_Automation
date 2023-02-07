from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import requests
from bs4 import BeautifulSoup

def initOptions() :
    # 옵션 생성
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless")                                           # 창 숨기는 옵션 추가
    return options

def initBrowser():
    options = initOptions()
    service = Service("C:/Program Files (x86)/Sejong Library Automation/driver/chromedriver.exe")
    service.creation_flags = CREATE_NO_WINDOW
    browser = webdriver.Chrome(service=service, options=options)
    return browser

def expandDisplay(browser) :
    try :
        #초록
        elem = browser.find_element_by_xpath(".//*[@id='bookIntroOpen']/..")
        if elem.get_attribute("style") == "display: block;" :
            elem = browser.find_element_by_id("bookIntroOpen")
            elem.click()
        
        #목차
        elem = browser.find_element_by_xpath(".//*[@id='tableOfContentsOpen']/..")
        if elem.get_attribute("style") == "display: block;" :
            elem = browser.find_element_by_id("tableOfContentsOpen")
            elem.click()
    except :
        return browser
    
    return browser


def getBookDetailUrl(browser, isbn) :
    url  = "https://search.shopping.naver.com/book/search?query="
    url = url + str(isbn)

    browser.get(url)
    browser.implicitly_wait(time_to_wait=1000)

    html = browser.page_source
    soup = BeautifulSoup(html, "xml")
    
    try :
        bidUrl = soup.find("div", class_="bookListItem_grade__tywh2").parent.parent.parent
        book_id = bidUrl['data-i']

        return book_id
    except AttributeError :
        return None


def searchData(browser, isbn):
    try:
        url = "https://search.shopping.naver.com/book/search?query=" + str(isbn)
        browser.get(url)
        browser.implicitly_wait(time_to_wait=1000)

        html = browser.page_source
        soup = BeautifulSoup(html, "xml")
    except:
        return None
    
    try:
        bidUrls = soup.find_all("a", class_="bookListItem_info_top__VgpiO linkAnchor")
        for bidUrl in bidUrls:
            book_id = bidUrl['data-i']
            url = "https://search.shopping.naver.com/book/catalog/" + book_id

            browser.get(url)
            browser.implicitly_wait(time_to_wait=1000)
            
            html = browser.page_source
            soup = BeautifulSoup(html, "html.parser")
            bookInfo = soup.find_all("div", class_="infoItem_data_text__bUgVI")

            #print(bookInfo)

            if bookInfo:
                return bookInfo
    except TypeError:
        return None

def getData(browser, isbn) :
    bookInfo = searchData(browser, isbn)
    if bookInfo is None:
        return None

        
    try :
        bookIntro = "".join(map(str, bookInfo[0].contents))
        bookIntro = bookIntro.replace("<br/>", "\n")
    except :
        bookIntro = ""
    try :
        tableOfContents = "".join(map(str, bookInfo[2].contents))
        tableOfContents = tableOfContents.replace("<br/>", "\n")
    except :   
        tableOfContents = ""
        
    return bookIntro, tableOfContents
