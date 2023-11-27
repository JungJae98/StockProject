import setting

# 필요한 쿼리문
query_up = "SELECT company, price, `change`, change_price, percent FROM top10_up WHERE n_date = CURDATE()"
query_down = "SELECT company, price, `change`, change_price, percent FROM top10_down WHERE n_date = CURDATE()"

# 데이터베이스에서 데이터 가져오기
setting.cursor.execute(query_up)
rows = setting.cursor.fetchall()

# 쿼리 결과값 저장할 공간
query_result = []

for row in rows:
    query_result.append(row)
    # print(row)

setting.cursor.execute(query_down)
rows = setting.cursor.fetchall()
for row in rows:
    query_result.append(row)
    # print(row)
print(query_result)

# HTML 테이블 헤더
html = "<table border = '1'><tr><th>회사명</th><th>가격</th><th>변동</th><th>변동 가격</th><th>변동률</th></tr>"

# 각 행에 대한 HTML 테이블 행 추가
for row in query_result:
    html += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
html += "</table>"

print(html)

# 메일 받을 주소 입력
receiver_email = setting.receiver()

# 메일 보내기
setting.send_email(receiver_email ,html)

# # 메세지 전송 받을 이메일
# receiver_email = setting.receiver()
#
# # 이메일 내용에 담길 것
# email_body = "내가 추가할 내용 "
#
# # 이메일 보내기 위한 함수
# setting.send_email(receiver_email, email_body)
#
