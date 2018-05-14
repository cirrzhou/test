# Author:zhouxy
'''
names = ["zhouxy","panjq","lijm","caiyq"]
print(names[0])
print(names[1:3]) # 左闭右开
print(names[:3]) # 如果是从头开始取，0可以忽略
print(names[-1]) # 取最后一个值，倒数第二为-2 以次类推
print(names[-3:-1]) # 切片从左往右数,但不包括-1最后一个值
print(names[-3:]) # 包括最后一个值
print(names[0::2]) # 后面的2是代表，每隔一个元素，就取一个
print(names[::2]) # 上句效果一样

'''
'''
names = ["zhouxy","panjq","lijm","caiyq"]
names.append("linjm") # 新增在最后
print(names)

names.insert(0,"liangjs") # 新增在指定下标位
print(names)
'''
'''
names = ["zhouxy","panjq","lijm","caiyq"]
names[3] = "cyq"
print(names)
'''
'''
names = ["zhouxy","panjq","lijm","caiyq"]
names.remove("caiyq") # 删除指定元素
names.pop() # 删除列表最后一个值
del names[0] # 相当于names.pop(0)
print(names)
'''
'''
names = ["zhouxy","zhouxy","panjq","lijm","caiyq",1,2,3]
print(names.index("zhouxy")) # 只返回找到的第一个下标

names.clear() # 清空
print(names)

names.reverse() # 反转
print(names)
'''
'''
names = ["zhouxy","zhouxy","panjq","lijm","caiyq",'1','2','3']
names.sort() # 排序，特殊字符、数字、大写、小写，python3里不同数据类型不能放在一起排序
print(names)

names = ["zhouxy","zhouxy","panjq","lijm","caiyq",'1','2','3']
b = ['a','b','c']
names.extend(b) # 合并列表
print(names)
'''

'''
names = ["zhouxy","panjq","lijm","caiyq",["linjm","liangjs"]]
names2 = names.copy()
print(names,names2)
names[0] = "周小律"
print(names,names2)
names[-1][1] = "梁胖"
print(names,names2) # copy只拷贝内存地址，只拷贝第一层数据
# names2 = names
# print(names,names2)
'''
'''
import copy
names = ["zhouxy","panjq","lijm","caiyq",["linjm","liangjs"]]
names2 = names
names[0] = "周小律"
names[-1][1] = "梁胖"
print(names,names2)
'''

names = ["zhouxy","panjq","lijm","caiyq",["linjm","liangjs"]]
print(len(names)) # 统计列表的长度以及列表元素的长度

for i in names: # 循环打印列表
    print(i)
names = ["zhouxy","panjq","lijm","caiyq",["linjm","liangjs"]]
index = 0
while index < len(names):
    print(names[index], end=' ')  # end='' 不换行打印， <br>#' ' 有一个空格，不换行隔一个空格打印
    index += 1


'''
index = 0
while index < len(list1):
    print(list1[index], end=' ')  # end='' 不换行打印， <br>#' ' 有一个空格，不换行隔一个空格打印         
    index += 1
'''



