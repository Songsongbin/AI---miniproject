import pymssql

conn=pymssql.connect(host='14.38.220.222',user='python1',password='python1',database='staging', charset='utf8')
cursor = conn.cursor()  
cursor.execute("select user_name AS ID,user_level AS LV,champ_name,position,concat(year,'-',month,'-',day,' ',minute,':',second) match_date,color_name from lol_match_detail D join lol_user U on D.fk_lol_user_seq = U.seq join lol_champ C on D.fk_lol_champ_seq= C.seq join lol_match M on D.fk_lol_match_seq = M.seq join lol_team_color T on D.fk_lol_team_color_seq = T.seq;")
row=cursor.fetchone()
while row:
    print(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]))
    row=cursor.fetchone()
conn.commit()
# 연결 끊기
conn.close() 

'''
#Database 정보
SERVER = 14.38.220.222
DATABASE = staging
LOGIN ID = python1
PASSWORD = python1

실제로 데이터베이스의 테이블정보까지 보려면 매니지먼트가 필요함
SSMS 를 다운 설치하고 직접로그인하여 테이블정보까지 확인먼저해주세요
테이블명
python
SELECT
- 데이터 조회
INSERT  ( 컬럼정보에 맞게 데이터를 2개 입력해주세요)
- 데이터 삽입
UPDATE  ( 삽입된 데이터 중에 1개의 SEQ 와 날짜를 제외한 데이터를 수정해주세요 )
- 데이터 수정
DELETE  ( Update 까지 되신분만 저에게 확인받고 Delete 해서 1개의 데이터를 삭제해주세요.)
- 데이터 삭제
-- 위에까지 진행되신분들은 Join 문을 활용하여 데이터를 조회하는 문제를 내도록 하겠습니다.
JOIN
- 데이터를 결합
'''