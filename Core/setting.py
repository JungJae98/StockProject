import mysql.connector

# 데이터베이스 접근
conn = mysql.connector.connect(
        host="localhost",
        user="stock",
        password="admin",
        database="stockproject"
    )

#