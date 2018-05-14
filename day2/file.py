# Author:zhouxy

#data = open("yesterday once more",encoding='utf-8').read()
'''
f =open('yesterday once more','r+',encoding='utf-8')   # 文件句柄，将打开的文件对象赋值给变量
first_line = f.readline()
print('first line:',first_line) # 读一行
data = f.read() # 光标读完一次，光标在文件最后
print(data)
f.write('卡朋特乐队')
f.close() # 关闭文件
'''
#for i in range (5):
   # print(f.readline()) # 读5行

#for line in f.readlines() :
   # print(line.strip()
'''
f =open('yesterday once more','r+',encoding='utf-8')   # 文件句柄，将打开的文件对象赋值给变量
f.seek(0)  # 重置文件光标
f.tell() # 光标所在位置
f.truncate(10) # 从10开始截断
f.closed # 文件是否关闭
f.readable() # 文件打开是否可读
f.writable() # 文件打开是否可写
f.flush() # 强制写入硬盘
'''

f = open('yesterday once more','r',encoding='utf-8')
f_new = open('yesterday once more.bak','w',encoding='utf-8')

for line in f:  # 可以用该语句循环读文件，不建议用readline
    if 'young' in line:
        line=line.replace('young','old')
    f_new.write(line)
f.close()
f_new.close()

