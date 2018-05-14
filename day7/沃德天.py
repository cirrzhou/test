# Author:zhouxy
import  time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


Url = 'http://10.10.200.86:10004/ccs-web/index.jsp'
Account = 'zhouxy'
Password = '111'

def get_ele_time(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def login_test():
    b = webdriver.Firefox()  #启动浏览器
    b.get(Url) #输入url
    b.maximize_window()
    login_ele = get_ele_time(b,10,lambda b:b.find_element_by_xpath('/html/body/form/ \
    table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[7]/img'))

    username_ele = b.find_element_by_id('j_username') #用户名元素
    username_ele.clear() #清空
    username_ele.send_keys(Account) #输入用户名
    password_ele = b.find_element_by_id('j_password')
    password_ele.clear()
    password_ele.send_keys(Password)
    login_ele.click()
    try :
        ele = b.find_element_by_link_text('Login fail: 错误的凭证')
        print('登录失败')
    except:
        print('登录成功')
    time.sleep(10)
    b.close()

if __name__ == '__main__':
    login_test()