# Author:zhouxy

import  time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://10.10.200.86:10004/ccs-web/index.jsp'
Account = 'zhouxy'
Password = '111'

def get_ele_time(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def operBrowser():
    '''
    return:webdriver_handle
    '''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle

def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()

def findElement(handle,*args):
    '''
    :param handle:
    :param args:
    :return: loginEle,userEle,pwdEle
    '''
    if 'text_css' in args:
        loginEle = get_ele_time(handle, 10, lambda handle: handle.find_element_by_css_selector(args['text_xpath']))
    userEle = handle.find_element_by_id(args['user_id'])  # 用户名元素
    pwdEle = handle.find_element_by_id(args['pwd_id'])
    return loginEle,userEle,pwdEle

def sentVals(eletupe,*args):
    listkey=[ 'account','password']
    i = 1
    for key in listkey:
        eletupe[i].clear()
        eletupe[i].send_keys(args[key])
        i +=1
    eletupe[0].click()

def checkResult(handle,text):
    try :
        ele = handle.find_element_by_link_text(text)
        print('登录失败')
    except:
        print('登录成功')

def login_test():
    d = operBrowser()
    openUrl(d,url)
    ele_dict = {
        'text_css': 'html body form table tbody tr td table tbody tr td table tbody tr td img',
        'user_id':'j_username',
        'pwd_id':'j_password'
    }
    ele_tuple =findElement(d,ele_dict)
    account_dict={
        'account':Account,
        'password':Password
    }
    sentVals(ele_tuple,account_dict)
    checkResult(d,'Login fail: 错误的凭证')

if __name__ == '__main__':
    login_test()