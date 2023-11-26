import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
with open(r'../../email.json', 'r') as email_file:
    email = json.load(email_file)
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText



# 데이터베이스 설정 _S @@@@@@@@@@@@@@@@@@@@@@
conn = mysql.connector.connect(
        host="localhost",
        user="stock",
        password="admin",
        database="stockproject"
    )

# 데이터베이스 커서 생성
cursor = conn.cursor()
# 데이터베이스 설정 _E @@@@@@@@@@@@@@@@@@@@@@




# 웹 드라이버 설정 _S @@@@@@@@@@@@@@@@@@@@@@
def web_driver():
    # 웹 드라이버 초기화 (ChromDriver 사용)
    service = Service(r'C:\Users\JungJaeHyeon\Desktop\StockProject\Core\chromedriver.exe')
    return webdriver.Chrome(service=service)
# 웹 드라이버 설정 _E @@@@@@@@@@@@@@@@@@@@@@





# 메일 세팅 _S @@@@@@@@@@@@@@@@@@@@@@
# json파일에서 가져온 로그인 정보
email_id = email['email_id']
email_pw = email['email_pw']

# 이메일을 전송 받을 이메일
def receiver():
    print("이메일을 입력하세요")
    receiver_email = input()
    message["To"] = receiver_email
    return receiver_email

# MIME 메시지 생성
message = MIMEMultipart()
message["From"] = email_id
message["Subject"] = "주식 현황"

def send_email(receiver_email,email_body):
    # 이메일에 본문 추가
    message.attach(MIMEText(email_body, "plain"))
    # SMTP 서버에 연결하고 이메일 전송
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_id, email_pw)
        server.sendmail(email_id, receiver_email, message.as_string())
# 메일 세팅 _E @@@@@@@@@@@@@@@@@@@@@@