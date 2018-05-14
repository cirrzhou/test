# Author:zhouxy
# 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作

# def change_file(filename,old,new):
#     f = open(filename,'r',encoding='utf-8')
#     f_new = open('filename.bak','w',encoding='utf-8')
#     for line in f:  # 循环旧文件
#         if old in line:
#             line = line.replace('old','new')
#             f_new.write(line)
#     f_new.close()
#     f.close()
#
# change_file('1','old','new')


#2、写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数

# def calc(str):
#     res= {
#         'num': 0, 'alpha': 0, 'space': 0, 'other': 0
#     }
#     for i in str:
#         if i.isdigit():
#             res['num']=res['num']+1
#         elif i.isalpha():
#             res['alpha']=res['alpha']+1
#         elif i.isspace():
#             res['space']=res['space']+1
#         else:
#             res['other']=res['other']+1
#     print(res)
#
# calc('abcd 1231 ///122vv ')

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

# def judge(object):
#     if len(object)>5:
#         print('yes')
#     else:
#         print('no')
#     return 0
#
# judge('123456')
# judge([1,23,45])
# judge((4,5,6,7,8,9,0))

#4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

# def new_judge(object):
#     if len(object)>2:
#         new_object= object[0:2]
#         return new_object
#     else:
#         return object
#
# a=new_judge([[1,2],{'b':2},{'c':3},'d'])
# print(a)
# b=new_judge([1,2])
# print(b)
#高阶函数应用1:把函数当做参数传给高阶函数
# import time
# def timmer(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print('%f'% float(stop_time-start_time))
#     return func
# def foo():
#     time.sleep(3)
#     print('the program run')
#
# foo=timmer(foo)
# foo()
# # #为函数foo增加了foo运行时间的功能,但是foo原来的执行方式是foo(),现在我们需要调用高阶函数timmer(foo),改变了函数的调用方式
#
#
#
#
# #高阶函数应用2:把函数名当做参数传给高阶函数,高阶函数直接返回函数名
# import time
# def timmer(func):
#     start_time=time.time()
#     return func
#     stop_time=time.time()
#     print('%f'% float(stop_time-start_time))
#
# def foo():
#     time.sleep(3)
#     print('the program run')
#
# foo=timmer(foo)
# foo()
# #没有改变foo的调用方式,但是我们也没有为foo增加任何新功能

username='zhouxy'
password='111111'
def login(type):
    def outter(func):
        def wrapper(*args,**kwargs):
            user=input('请输入用户名:')
            pswd=input('请输入密码:')
            if type == 'local':
                print('使用本地认证')
                if user==username and pswd==password:
                    print('登录成功')
                    res=func(*args,**kwargs)    #func=home/bbs
                    return res
                else:
                    print('登录失败')
            else:
                print('使用其它认证')
                if user == username and pswd == password:
                    print('登录成功')
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('登录失败')
        return wrapper
    return outter
@login #语法糖 index调用的是outter
def index(type):
    print('欢迎进入首页'.center(10,'-'))
    return 1
@login(type='local') #home=wrapper
def home():
    print('欢迎进入登陆界面'.center(10,'-'))
@login(type='API')
def bbs():
    print('欢迎进入论坛界面'.center(10,'-'))

index('local')
home()
bbs()

# def auth(driver='file'):
#     def auth2(func):
#         def wrapper(*args,**kwargs):
#             name=input("user: ")
#             pwd=input("pwd: ")
#             if driver == 'file':
#                 if name == 'egon' and pwd == '123':
#                     print('login successful')
#                     res=func(*args,**kwargs)
#                     return res
#             elif driver == 'ldap':
#                 print('ldap')
#         return wrapper
#     return auth2
#
# @auth(driver='file')
# def foo(name):
#     print(name)
#
# foo('egon')