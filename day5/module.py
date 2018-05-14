# Author:zhouxy

import time

# # <1> 时间戳
# print(time.time()) # 时间戳:1521424491.5176704
# # <2> 时间字符串
# print(time.strftime("%Y-%m-%d %X")) #格式化的时间字符串:'2018-03-19 09:54:51'
# # <3> 时间元组
# print(time.localtime()) #本地时区的struct_time:'time.struct_time(tm_year=2018, tm_mon=3, tm_mday=19, tm_hour=9, tm_min=54, tm_sec=51, tm_wday=0, tm_yday=78, tm_isdst=0)'
# print(time.gmtime())    #UTC时区的struct_time:isdst为时区


# #时间戳<- - ->结构化时间：  localtime/gmtime/mktime
#
# print(time.localtime(3600*24))
# print(time.gmtime(3600*24))
# print(time.mktime(time.localtime()))
#
#字符串时间<- - ->结构化时间： strftime／strptime
# print(time.strftime("%Y-%m-%d %X", time.localtime()))
# print(time.strptime("2017-03-16","%Y-%m-%d"))


# time.sleep(seconds)
# print(time.asctime(time.localtime()))
# print(time.ctime(1521425493.0))


#时间加减
# import datetime
#
# print(datetime.datetime.now()) #返回当前时间 2018-03-19 10:17:39.694514
# print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2018-03-19
# print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
#
# c_time  = datetime.datetime.now()
# print(c_time.replace(minute=3,hour=2)) #时间替换


# import random
#
# print(random.random())  # (0,1)float 大于0且小于1之间的小数
# print(random.randint(1, 3))  # [1,3] 大于等于1且小于等于3之间的整数
# print(random.randrange(1, 3))  # [1,3) 大于等于1且小于3之间的整数
# print(random.choice([1, '23', [4, 5]]))  # 1或者23或者[4,5]
# print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合
# print(random.uniform(1, 3))  # 大于1小于3的小数，如1.927109612082716
#
# item = [1, 3, 5, 7, 9]
# random.shuffle(item)  # 打乱item的顺序,相当于"洗牌"
# print(item)


# import random
# def make_code(n):
#     res=''
#     for i in range(n):
#         s1=chr(random.randint(65,90))
#         s2=str(random.randint(0,9))
#         res+=random.choice([s1,s2])
#     return res
#
# print(make_code(4))
#
#
# import random
# checkcode = ''
# for i in range(4):
#     current = random.randrange(0,4)
#     if current != i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode += str(temp)
# print(checkcode)


# import shutil
# f1= open('file1','r',encoding='utf-8')
# f2= open('file2','w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)  #将文件内容拷贝到另一个文件中


# import  shutil
# shutil.copyfile('file2','file3') #拷贝文件，目标文件无需存在


# import  shutil
# shutil.copymode('file1','file2') #仅拷贝权限。内容、组、用户均不变，目标文件必须存在

# import  shutil
# shutil.copystat('file1','file3') #仅拷贝状态的信息，包括：mode bits, atime, mtime, flags，目标文件必须存在

# import shutil
# shutil.copy('file1','file2')#拷贝文件和权限

# import shutil
# shutil.copy2('file1','file2')#拷贝文件和状态信息

# import shutil
# shutil.copytree('a','copy_a') #递归的去拷贝文件夹
#
# import shutil
# shutil.rmtree('copy_a') #递归的去删除文件

# import shutil
# shutil.move('file3','a')#递归的去移动文件，它类似mv命令

# import shutil
# shutil.make_archive('archive_test','zip',r'C:\Users\zhouxy\PycharmProjects\untitled\day4')

# import zipfile
# z = zipfile.ZipFile('file.zip','w')
# z.write('file1')
# print('-----')
# z.write('file2')
# z.close()
#
# import zipfile
# z = zipfile.ZipFile('archive_test.zip', 'r')
# z.extractall()
# z.close()