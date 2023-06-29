
import pymysql
con = pymysql.connect(
    user = 'root', #사용자명
    passwd='1234', #비번
    host = '127.0.0.1', #일반적으로 로컬 호스트 주소
    db = 'shop', #사용할 데이터베이스
    charset='utf8' #인코딩 방법, 로컬뿐아니라 클라우드도 연결가능
    
)

mycursor = con.cursor() #cursor()메서드를 통해 데이터베이스의 커서 객체를 가져옴

#shop 데이터베이스중 goods 테이블을 가져옴
query = """
select * from goods; 
"""
#모든 열을 가져오는 쿼리, """세개는 줄바꿈을 해주는 형태로 가져옴


mycursor.execute(query) #쿼리가 실행되며 execute메서드를 사용하여 sql 쿼리를 DB서버에 보내게 된다
data = mycursor.fetchall() #서버로부터 데이터를 가져온다
con.close() # 작업을 마친 후에는 반드시 con.close()통해 데이터베이스와 연결을 종료한다

print(data)
