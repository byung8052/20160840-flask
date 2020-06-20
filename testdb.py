import sqlite3 
conn = sqlite3.connect('mydb.db') 

'''
# Cursor 객체 생성 
c = conn.cursor() 

# 테이블 생성 
c.execute("INSERT INTO student VALUES('20201234','파이썬')") 

# execute 에 db 에 적용 
conn.commit() 

# 접속한 db 닫기 
conn.close()
'''

# Cursor 객체 생성 
c = conn.cursor() 

# 데이터 불러 와서 출력 
#for row in c.execute('SELECT * FROM student'): 
#    print(row) 

#학번을 검색해서 정보 출력

num = ('20201234','파이썬') 
c.execute('SELECT * FROM student WHERE num = ? and name = ?', num) 
print(c.fetchone())

# 접속한 db 닫기 
conn.close()

