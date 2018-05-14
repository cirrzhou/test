# Author:zhouxy

# import configparser # python2.X 为 ConfigParser
#
# config = configparser.ConfigParser() # 创建一个config对象
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
#
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'no'
#
# with open('example.conf', 'w') as configfile:
#     config.write(configfile)
#

# 读取
# import configparser
#
# config=configparser.ConfigParser()
# config.read('db.conf')
#
# print(config.defaults()) # 查看default所有内容
# print(config.sections()) #查看所有的标题
# print(config.options('bitbucket.org')) #查看标题bitbucket.org和default下所有key=value的key,与default相同的key不重复显示
# print(config.items('bitbucket.org')) #查看标题bitbucket.org下和default所有key=value的(key,value)格式
#
# print(config.get('bitbucket.org','User')) #查看标题bitbucket.org下User的值=>字符串格式
# print(config.getint('DEFAULT','ServerAliveInterval'))#查看标题default下ServerAliveInterval的值=>整数格式
# print(config.getboolean('DEFAULT','ForwardX11')) #查看标题default下ForwardX11的值=>布尔值格式
# print(config.getfloat('topsecret.server.com','Port')) #查看标题topsecret.server.com下Port的值=>浮点型格式


import configparser

config=configparser.ConfigParser()
config.read('example.conf',encoding='utf-8')

config.remove_section('bitbucket.org') #删除整个标题bitbucket.org
config.remove_option('topsecret.server.com','ForwardX11') #删除标题topsecret.server.com下的某个ForwardX11
print(config.has_section('bitbucket.org')) #判断是否存在某个标题
print(config.has_option('topsecret.server.com','ForwardX11')) #判断标题topsecret.server.com和default下是否存在ForwardX11

config.add_section('zhouxy') #添加一个标题
config.set('zhouxy','name','zhouxy') #在标题zhouxy下添加name=zhouxy,age=18的配置
#config.set('egon','age',18) #报错,必须是字符串
config.write(open('example.conf','w')) #最后将修改的内容写入文件,完成最终的修改