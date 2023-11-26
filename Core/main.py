from apscheduler.schedulers.background import BackgroundScheduler
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def scheduled_job():
    # MariaDB 연결 설정
    conn = mysql.connector.connect(
        host="localhost",
        user="stock",
        password="admin",
        database="stockproject"
    )

    # 커서 생성
    cursor = conn.cursor()
    # query문 작성
    query = "INSERT INTO top10_up (n_date, company, price, `change`, change_price, percent) VALUES (NOW(),%s,%s,%s,%s,%s)"

    # 웹 드라이버 초기화 (ChromDriver 사용)
    service = Service(r'C:\Users\JungJaeHyeon\Desktop\StockProject\Core\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    top10_up = []

    try:
        # 네이버 금융 페이지
        driver.get('https://finance.naver.com/')
        time.sleep(2)
        # a_tag = TOP종목 내에 있는 상승 버튼
        a_tag = driver.find_element(By.CSS_SELECTOR, "ul.tab_area.sise_top1 li.tab2 a")
        a_tag.click()
        time.sleep(1)

        # up_rows는 상승된 종목들을 가져옴
        up_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody#_topItems2 tr.up')
        # 하위에 있는 th, td 태그를 가져옴
        for row in up_rows:
            header = row.find_element(By.TAG_NAME, 'th').text
            datas = row.find_elements(By.TAG_NAME, 'td')
            data_cell = datas[1].text.split("\n")
            # 전달할 데이터
            data = (header, datas[0].text, data_cell[0], data_cell[1], datas[2].text)
            print(data)
            # 데이터베이스에 전달
            cursor.execute(query, data)
        conn.commit()

    finally:
        # 드라이버 종료
        driver.quit()
        cursor.close()
        conn.close()


scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_job, 'cron', hour=0)
scheduler.start()

print("Press Ctrl+C to exit")

try:
    # 무한 루프를 돌면서 스케줄러가 작동하도록 유지
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    print("Scheduler is stopping...")
    scheduler.shutdown()  # 스케줄러 종료