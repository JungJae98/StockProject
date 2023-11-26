from apscheduler.schedulers.background import BackgroundScheduler
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import setting

# print(setting.a)

# 웹 드라이버 초기화 (ChromDriver 사용)
# service = Service(r'../chromedriver.exe')
# driver = webdriver.Chrome(service=service)
top10_up = []

try:
    # 네이버 금융 페이지
    setting.driver.get('https://finance.naver.com/')
    time.sleep(2)
    # a_tag = TOP종목 내에 있는 상승 버튼
    a_tag = setting.driver.find_element(By.CSS_SELECTOR, "ul.tab_area.sise_top1 li.tab2 a")
    a_tag.click()
    time.sleep(1)
    # up_rows는 상승된 종목들을 가져옴
    up_rows = setting.driver.find_elements(By.CSS_SELECTOR, 'tbody#_topItems2 tr.up')

    for row in up_rows:
        header = row.find_element(By.TAG_NAME, 'th').text
        datas = row.find_elements(By.TAG_NAME,'td')
        print(header)
        # print(datas[0].text)
        # print(datas[1].text)
        data1 = datas[1].text.split("\n")
        print(data1[0])
        # print(data1[1])
        # print(data2)
        # print(datas[2].text)
        # print(datas[3].text)



finally:
    # 드라이버 종료
    setting.driver.quit()
