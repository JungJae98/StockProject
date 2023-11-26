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
        user = "stock",
        password = "admin",
        database = "stockproject"
    )

    # 커서 생성
    cursor = conn.cursor()
    # query문 작성
    query = "INSERT INTO top10_down (n_date, company, price, `change`, change_price, percent) VALUES (NOW(),%s,%s,%s,%s,%s)"

    # 웹 드라이버 초기화 (ChromDriver 사용)
    service = Service(r'C:\Users\JungJaeHyeon\Desktop\StockProject\Core\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    top10_down = []

    try:
        # 네이버 금융 페이지
        driver.get('https://finance.naver.com/')
        time.sleep(2)

        # a_tag = TOP종목 내에 있는 하락 버튼
        a_tag = driver.find_element(By.CSS_SELECTOR, "ul.tab_area.sise_top1 li.tab3 a")
        a_tag.click() # a_tag 클릭
        time.sleep(1)

        # down_rows는 하락된 종목들을 가져옴
        down_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody#_topItems3 tr.down')
        for row in down_rows:
            # tr태그 내에 있는 th태그와 td태그를 모두 찾음
            cells = row.find_elements(By.XPATH, ".//th | .//td")
            # cell의 내용들을 join을 이용하여 한 줄로 출력, 구분자는 공백
            row_text = ' '.join([cell.text.replace('\n', ' ') for cell in cells])
            top10_down.append(row_text)
        print(top10_down)

        for i in top10_down:
            split_top10 = i.split(" ")
            # 데이터베이스에 넣을 data
            data = (split_top10[0], split_top10[1], split_top10[2], split_top10[3], split_top10[4])
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