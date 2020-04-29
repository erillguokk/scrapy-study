from pymysql import  *
from com.guosheng import *
print(listdir())
#列表推导式
i = [i for i in range(1,10) if i%2==0 if i>5]
y = [y for y in "abcde"]
print(y)
print(i)
i = [(i,j) for i in range(1,10) for j in range(1,10)]
print(i)

#操作数据库
conn = connect("10.164.10.240","root","Berker_31104","bn",3306)
cursor = conn.cursor()
count = cursor.execute("select * from recharge_order")
print(count)
result = cursor.fetchall()
for i in result:
    print(i)
conn.commit()#提交事务
conn.close()
