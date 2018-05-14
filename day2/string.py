# Author:zhouxy
'''
name = "ZZzzhouxy"

print(name.capitalize()) # 首字母大写
print(name.count('z')) # 统计字符串z出现次数
print(name.casefold()) # 大写全部变小写
print(name.center(20,'-'))
print(name.encode()) # 将字符串编码成bytes格式
print(name.endswith('xy')) # 判读字符串是否以xy结尾
print(name.expandtabs()) # 将\t转换成多长的空格
print(name.find('Z')) # 查找A,找到返回其索引， 找不到返回-1
print(name[name.find("Z"):3]) # 字符串切片
print(name.rfind('z')) # 找最右的值下标
name = "my name is {name}"
print(name.format(name="zhouxy"))
'''
'''
print('1'.isdigit()) # 是否为整型
print('a1'.isalnum()) # 是否为字母加数字
print('a1'.isalpha()) # 是否为纯英文字符
print('10'.isdecimal()) # 是否为十进制
print('1_a'.isidentifier()) # 是否为合法的标识符
print('1.0'.isnumeric()) # 是否为纯数字
print('Zhouxy'.isupper()) # 是否都为大写
print('My name is zhouxy'.istitle()) # 是否每个字符首字母大写
print('My name is zhouxy'.title()) # 每个字符首字母转为大写
print('Zhouxy'.lower()) # 大写转为小写
print('Zhouxy'.upper()) # 小写转为大写
print('Zhouxy'.swapcase()) # 大写转小写，小写转大写

'''
print('1+2+3'.split('+')) # 字符转按分隔符分成列表
print('a\nb'.splitlines()) # 按换行符分隔
print(' zhouxy '.strip()) # 去空格和去回车
print(' zhouxy '.lstrip()) # 左边去空格和去回车
print(' zhouxy '.rstrip()) # 右边去空格和去回车
print('zhouxyzxy'.replace('z','Z',1)) # 指定替换个数
print('zhouxy'.ljust(20,'*'))
print('zhouxy'.rjust(20,'*'))
print('zhouxy'.zfill(20)) # 补零
print('+'.join(['1','2'])) # 列表转为字符串
n = str.maketrans('xyzabc','123456') # 加密
print("zhouxy".translate(n))





