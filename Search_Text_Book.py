from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time

open_json = open("./json/my_id_and_pass.json")
session = json.load(open_json)
login_id = session["id"]
login_pass = session["pass"]

def set_up_chrome_driver():
    # ここでいろいろやる
    options = Options() 
    options.binary_location = '/usr/bin/google-chrome' 
    #chrome binary location specified here 
    options.add_argument('--start-maximized') 
    #open Browser in maximized mode 
    options.add_argument('--no-sandbox') 
    #bypass OS security model 
    options.add_argument('--disable-dev-shm-usage') 
    #overcome limited resource problems 
    options.add_experimental_option('excludeSwitches', ['enable-automation']) 
    options.add_experimental_option('useAutomationExtension', False) 
    chrome_driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
    return chrome_driver

def login_Dream_Canpas(chrome_driver):
    chrome_driver.get("https://www2.st.kagawa-u.ac.jp/Portal/?_gl=1*iafbpx*_ga*NjA3MDk0NzIwLjE2Mzk0NjU5ODk.*_ga_GF93XH9WXM*MTY5MzIwODI1Ny42OC4xLjE2OTMyMDk1NjYuNjAuMC4w")
    chrome_driver.find_element_by_id("txtID").send_keys(login_id)
    time.sleep(0.2)
    chrome_driver.find_element_by_id("txtPassWord").send_keys(login_pass)
    time.sleep(0.2)
    chrome_driver.find_element_by_id("btnLogIn").click()
    time.sleep(1.0)

def get_Syllabus_list(chrome_driver):
    chrome_driver.get("https://www2.st.kagawa-u.ac.jp/Portal/StudentApp/Regist/RegistList.aspx")
    html = chrome_driver.page_source.encode("utf-8")
    soup_race = BeautifulSoup(html, "html.parser")
    elems = soup_race.select("a")
    syllabus_list = []
    for elem in elems:
        href = elem.get("href")
        if href is not None and "Portal/Public/Syllabus" in href:
            syllabus_list.append(href)
    return syllabus_list 

def get_Text_Books(url):
    df_text_book = pd.read_html(url, match="教科書・参考書等")
    return df_text_book[-1].iloc[1,0]

def get_lesson_name(url):
    html = requests.get(url)
    html.raise_for_status()
    soup = BeautifulSoup(html.content, "lxml")
    lesson_name = soup.select("#ctl00_phContents_sylSummary_txtSbjName")
    return str(lesson_name[0])[50:-7]

if __name__ == "__main__":
    chrome_driver = set_up_chrome_driver()
    login_Dream_Canpas(chrome_driver)
    syllabus_list = get_Syllabus_list(chrome_driver)
    chrome_driver.close()