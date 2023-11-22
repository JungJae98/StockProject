from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import mysql.connector
import time

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
    a_tag.click() # a_tag 클릭
    time.sleep(1)

    # up_rows는 상승된 종목들을 가져옴
    up_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody#_topItems2 tr.up')
    for row in up_rows:
        # tr태그 내에 있는 th태그와 td태그를 모두 찾음
        cells = row.find_elements(By.XPATH, ".//th | .//td")
        # cell의 내용들을 join을 이용하여 한 줄로 출력, 구분자는 공백
        row_text = ' '.join([cell.text.replace('\n', ' ') for cell in cells])
        top10_up.append(row_text)
    #print(top10_up)

    for i in top10_up:
        split_top10 = (i.split(" ",))
        company = split_top10[0]
        price = split_top10[1]
        change = split_top10[2]
        change_price = split_top10[3]
        percent = split_top10[4]
        # 데이터베이스에 넣을 data
        data = (company, price, change, change_price, percent)
        cursor.execute(query, data)


    conn.commit()






finally:
    # 드라이버 종료
    driver.quit()


