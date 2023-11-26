import json
with open(r'../../email.json', 'r') as email_file:
    email = json.load(email_file)

# json파일에서 가져온 로그인 정보
email_id = email['email_id']
email_pw = email['email_pw']

print(email_id)
print(email_pw)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 메시지를 받을 이메일
print("이메일 입력")
receiver_email = input()

# MIME 메시지 생성
message = MIMEMultipart()
message["From"] = email_id
message["To"] = receiver_email
message["Subject"] = "전송 테스트"
email_body = "이메일 전송 테스트"


# 이메일에 본문 추가
message.attach(MIMEText(email_body, "plain"))

# SMTP 서버에 연결하고 이메일 전송
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email_id, email_pw)
    server.sendmail(email_id, receiver_email, message.as_string())