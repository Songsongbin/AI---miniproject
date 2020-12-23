import pymssql
import base64
import requests

conn=pymssql.connect(host='14.38.220.222',user='python1',password='python1',database='staging', charset='utf8')
cursor = conn.cursor()  

cursor.execute("SELECT BASE64 FROM Image_File WHERE STUDENT_NAME='수빈';")

row = cursor.fetchone()
cnt=0
while row:
    data=base64.b64decode(row[0])
    
    f = open("새파일{}.png".format(cnt), 'wb')
    f.write(data)
    
    f.close()

    row = cursor.fetchone()
    cnt+=1
conn.commit()
# 연결 끊기
conn.close() 