from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

# 웹 드라이버 초기화 (ChromDriver 사용)
service = Service(r'C:\Users\JungJaeHyeon\Desktop\StockProject\Core\chromedriver.exe')
driver = webdriver.Chrome(service=service)


try:
    # 네이버 금융 페이지
    driver.get('https://finance.naver.com/')
    time.sleep(10)


finally:
    driver.quit()


# service = Service(executable_path='chromedriver')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
#
# url = 'https://finance.naver.com/'
# driver.get(url)

