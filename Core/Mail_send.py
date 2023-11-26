import setting

# 필요한 쿼리문
query_up = "SELECT * FROM top10_up WHERE n_date = CURDATE()"
query_down = "SELECT * FROM top10_down WHERE n_date = CURDATE()"

# 데이터베이스에서 데이터 가져오기
setting.cursor.execute(query_up)
rows = setting.cursor.fetchall()
for row in rows:
    print(row)

# # 메세지 전송 받을 이메일
# receiver_email = setting.receiver()
#
# # 이메일 내용에 담길 것
# email_body = "내가 추가할 내용 "
#
# # 이메일 보내기 위한 함수
# setting.send_email(receiver_email, email_body)
#
