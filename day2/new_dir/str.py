# Author:zhouxy
#-*-coding:gbk-*-

str='你好'
print(str.encode('utf-8').decode('utf-8').encode('gb2312'))
