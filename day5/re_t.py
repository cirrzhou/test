# Author:zhouxy


# import re
# # 默认匹配除\n之外的任意一个字符
# ret1=re.findall('李.','李爽\nalex\n李四\negon\nalvin\n李二')  #['李爽', '李四', '李二']
# # 匹配字符开头
# ret2=re.findall('^李.','李爽\nalex\n李四\negon\nalvin\n李二') #['李爽']
# # 匹配字符结尾
# ret3=re.findall('李.$','李爽\nalex\n李四\negon\nalvin\n李二') #['李二']


import re

ret1=re.findall('李.*','李杰\nalex\n李莲英\negon\nalvin\n李二棍子')
ret2=re.findall('李.+','李杰\nalex\n李莲英\negon\nalvin\n李二棍子')
ret3=re.findall('(李.{1,2})\n','李杰\nalex\n李莲英\negon\nalvin\n李二棍子') # 设定优先级的原因
ret4=re.findall('\d+\.?\d*','12.45,34,0.05,109') # 匹配一个数字包括整型和浮点型
print(ret1,ret2,ret3)
print(ret4)