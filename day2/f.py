# Author:zhouxy

def add (x,y,f):
    return  f(x)+ f(y)

res = add(-1,3,abs)
print(res)












# classmate_list = ['panjq','lijm','caiyq']
# def change_classmate_list(classmate):
#     '''改同学名'''
#     classmate_list[2] = 'zhouxy' #列表，字典，集合都可以在局部变量修改全局变量
#     print(classmate)
#
# change_classmate_list(classmate_list)
# print(classmate_list)






# def add(n):
#     n=n+1
#     print(n)
#     if n<999: #最大递归次数999
#         add(n+1)
# add(0)








# school = '深圳大学' # 全局变量
# def change_school(school_name):
#     global school # 声明，参数不能与变量同名
#     school = '育才中学' # 局部变量
#     print(school)
#
# change_school(school)
# print(school)















# def info(name,sex,*args,age=1,**kwargs):
#      print(name)
#      print(sex)
#      print(args)
#      print(age)
#      print(kwargs)
#      return  0
#
# info('zhouxy','f',1,2,3,age=18,address='CN')
# info('zhouxy','f',*[1,2])



# def stu_register(name, age, *args, **kwargs):  # *kwargs 会把多传入的参数变成一个dict形式
#     print(name, age, args, kwargs)
#
# stu_register("Jack", 32, "CN", "Python", sex="Male", province="ShanDong")


# def foo(x, y, **kwargs):
#     print(x, y)
#     print(kwargs)
# foo(1, y=2, a=1, b=2, c=3)
#
# def foo(x, y, **kwargs):
#     print(x, y)
#     print(kwargs)
# foo(1, y=2, **{'a': 1, 'b': 2, 'c': 3})
#
# def foo(x, y, z):
#     print(x, y, z)
# foo(**{'z': 1, 'x': 2, 'y': 3})