# Author:zhouxy
import os
import sys

# 定义登录黑白名单列表
pass_list = open("pass.txt","r") # 预先填写，格式为姓名：密码
black_list = open ("black.txt","r")
# 定义空列表
name_list = []
clock_list =[]
name_dict = {} # 字典
# 定义变量
count = 0
_count = 2
#将白名单中的信息读取，存储到列表中
for i in pass_list:
    name,password = i.strip('\n').split('：')
    name_list.append(name)
    name_dict[name] = password
pass_list.close()
#将黑名单的信息读取，存储到列表中
for i in black_list:
    clock_list.append(i.strip('\n'))
black_list.close()

username = input("请输入用户名：")
if not username:
    print("用户名不能为空")
elif username in clock_list:
    print ("抱歉，用户名已被锁定QAQ")
    sys.exit()
else:
    if username in name_dict:
        for count in range(10):
            if count < 3:
                passwd = input("请输入用户密码：")
                if not passwd:
                    print("用户密码不能为空")
                elif passwd == name_dict[username]:
                    print ("欢迎".center(40,'-'))
                    break
                else:
                    print ("密码错误，还剩下%s机会"%(_count))
                    count +=1
                    _count -=1
                    continue
            if count > 3:
                print ("用户名已被锁定")
                f = open('black.txt','a')
                f.write(username + '\n')
                f.close()
                sys.exit()
    else:
        print ("用户未注册")
        sys.exit()
