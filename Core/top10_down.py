from apscheduler.schedulers.background import BackgroundScheduler
import time
from selenium.webdriver.common.by import By
# 세팅저장
import setting

def scheduled_job():
    # query문 작성
    query = "INSERT INTO top10_down (n_date, company, price, `change`, change_price, percent) VALUES (NOW(),%s,%s,%s,%s,%s)"

    top10_down = []

    try:
        # 네이버 금융 페이지
        setting.driver.get('https://finance.naver.com/')
        time.sleep(2)

        # a_tag = TOP종목 내에 있는 하락 버튼
        a_tag = setting.driver.find_element(By.CSS_SELECTOR, "ul.tab_area.sise_top1 li.tab3 a")
        a_tag.click() # a_tag 클릭
        time.sleep(1)

        # down_rows는 하락된 종목들을 가져옴
        down_rows = setting.driver.find_elements(By.CSS_SELECTOR, 'tbody#_topItems3 tr.down')
        for row in down_rows:
            header = row.find_element(By.TAG_NAME, 'th').text
            datas = row.find_elements(By.TAG_NAME, 'td')
            data_cell = datas[1].text.split("\n")
            # 전달할 데이터
            data = (header, datas[0].text, data_cell[0], data_cell[1], datas[2].text)
            print(data)
            # 데이터베이스에 전달
            setting.cursor.execute(query, data)
        setting.conn.commit()
    finally:
        # 드라이버 종료
        setting.driver.quit()
        setting.cursor.close()
        setting.conn.close()

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