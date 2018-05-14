# Author:zhouxy

'''
import sys

#print (sys.path) #打印环境变量
print (sys.argv) #打印绝对路径/相对路径
print (sys.argv[2]) #取值
'''

import os

cmd_res = os.system("dir") #只执行命令，不保存结果
cmd_res = os.popen("dir").read()
print(cmd_res)

os.mkdir("new_dir")
