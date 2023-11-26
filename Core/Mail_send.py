import json
import setting

with open(r"../../email.json", 'r') as email_file:
    email = json.load(email_file)

# json파일에서 가져온 로그인 정보
email_id = email['email_id'] ## 이메일 아이디
email_pw = email['email_pw'] ## 이메일 비밀번호

## 이메일 아이디 비번 출력 테스트 _S
print(email_id)
print(email_pw)
## 이메일 아이디 비번 출력 테스트 _E


# 이메일을 전송 받을 이메일
print("이메일을 입력하세요.")
receiver_email = input()

# MIME 메세지 생성
messa