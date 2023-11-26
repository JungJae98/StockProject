import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 데이터베이스 접근
conn = mysql.connector.connect(
        host="localhost",
        user="stock",
        password="admin",
        database="stockproject"
    )

# 데이터베이스 커서 생성
cursor = conn.cursor()

def web_driver():
    # 웹 드라이버 초기화 (ChromDriver 사용)
    service = Service(r'C:\Users\JungJaeHyeon\Desktop\StockProject\Core\chromedriver.exe')
    return webdriver.Chrome(service=service)



# 메일 세팅
# def mail_Set():
