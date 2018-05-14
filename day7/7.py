# Author:zhouxy

import pymysql
#链接
conn=pymysql.connect(host='10.10.200.61',user='dev_hx_ccs',password='dev_hx_ccs123',database='dev_hx_ccsdb')
#游标
cursor=conn.cursor()

#执行sql语句
sql='select * from ccs_acct;'
cursor.execute(sql) #执行sql语句，返回sql影响成功的行数rows,将结果放入一个集合，等待被查询
cursor.lastrowid
# cursor.scroll(3,mode='absolute') # 相对绝对位置移动
# cursor.scroll(3,mode='relative') # 相对当前位置移动
# res1=cursor.fetchone()
# res2=cursor.fetchone()
# res3=cursor.fetchone()
# res4=cursor.fetchmany(3)
res5=cursor.fetchall()
# print(res1)
# print(res2)
# print(res3)
# print(res4)
print(res5)
# print('%s rows in set (0.00 sec)' %rows)



conn.commit() #提交后才发现表中插入记录成功
cursor.close()
conn.close()