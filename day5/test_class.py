# Author:zhouxy

# # 创建类
# class Foo:
#
#     def Bar(self):
#         print('Bar')
#
#     def Hello(self, name):
#         print('i am %s' % name)
#
# # 根据类Foo创建对象obj
# obj = Foo()
# obj.Bar()  # 执行Bar方法
# obj.Hello('zhouxy')  # 执行Hello方法　


# # 创建类
# class Foo():
#
#     def __init__(self,name,age):  #称为构造方法，根据类创建对象时自动执行
#         self.name = name,
#         self.age = age
# # 根据类Foo创建对象
# # 自动执行Foo类的__init__方法
# obj1 = Foo('zhouxy',18)  #将zhouxy和18分别封装到obj1 self的name和age属性中
# # 根据类Foo创建对象
# # 自动执行Foo类的__init__方法
# obj2 = Foo('xyzhou',18)  #将xyzhou和18分别封装到obj2 self的name和age属性中



# class Foo():
#
#     def __init__(self,name,age):
#         self.name = name,
#         self.age = age
#
#     def info(self):
#         print(self.name)
#         print(self.age)
#
# obj1 = Foo('zhouxy',18)
# obj1.info() # Python默认会将obj1传给self参数，即：obj1.info(obj1)，所以，此时方法内部的self＝obj1，即：self.name是zhouxy，self.age是18
#
# obj2 = Foo('xyzhou',18)
# obj2.info()


# class Animal:
#
#     def eat(self):
#         print('%s吃'%self.name)
#     def drink(self):
#         print('%s喝'%self.name)
#
# # 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = '猫'
#
#     def yeal(self):
#         print('喵喵')
# # 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = '狗'
#
#     def yeal(self):
#         print('汪汪')
#
# c1 = Cat('小猫')
# c1.eat()
#
# d1 = Dog('小狗')
# d1.drink()

# class 父类:
#     def 父类中的方法:
#         #do something
# class 子类(父类): #子类继承父类
#     pass
# zi = 子类()   #创建子类对象
# zi.父类中的方法()  #执行从父类中继承的方法

# class People:    # 定义父类
#     # 定义构造方法
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def walk(self):
#         print('%s is walking' %self.name)
#     def foo(self):
#         print('from father %s' %self.name)
#
# class Love(object):   #新式类
#     def fall_in_love(self,obj):
#         print('%s fall in love with %s'%(self.name,obj.name))
#
# class Boy(People,Love):    # 定义派生（子类）
#     def __init__(self,name,age,sex,face):    # 重构构造方法
#         People.__init__(self,name,age,sex)   # super().__init__(name,age,sex)
#         self.face=face
#     def boy(self):
#         print('%s is a boy' %self.name)
#     def foo(self):
#         People.foo(self)
#         print('from boy')
#
# class Gril(Love,People):    # 定义派生（子类），找构造函数的顺序，子类->父类顺序，但是在父类顺序中构造函数中调用不存在的数据属性则报错
#     def gril(self):
#         print('%s is a gril'%self.name)
#
# b = Boy('JACK',18,'M','so handsome!!')
# g = Gril('ROSE','16','F')
# b.fall_in_love(g)
# g.gril()
# g.walk()
# b.foo()    #调用子类中的方法


# class C:
#     def __init__(self,num):
#         self.num = num
#     def __private(self):
#         print('私有方法')
# Func=()


# class Foo(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('%s is eatting'%self.name)
#
# def Drink(self):
#     print('%s is drinking'%self.name)
#
# obj = Foo("zhouxy")
# choice = input('>>:').strip()
#
# if hasattr(obj,choice):   #判断该对象是否存在对应字符串方法
#     print(getattr(obj,choice))   #根据字符串获取对象对应方法的内存地址
#     # getattr(obj,choice)()    #调用
#     setattr(obj,choice,'xyzhou') #修改属性
#     delattr(obj,choice) #删除
# else:
#     setattr(obj,choice,Drink)  #动态加方法
#     obj.drink(obj)    #输入drink调用
#     #setattr(obj,choice,None)  # 动态加属性

# def func(self):
#     print('hello zhouxy')
#
#
# Foo = type('Foo', (object,), {'func': func})
# # type第一个参数：类名
# # type第二个参数：当前类的基类
# # type第三个参数：类的成员
#
# f = Foo()
# f.func()


try:
    raise TypeError('类型错误')
except Exception as e:
    print(e)