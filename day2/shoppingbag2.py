# Author:zhouxy
#启动程序后，让用户输入工资，然后打印商品列表
#允许用户根据商品编号购买商品
#用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#可随时退出，退出时，打印已购买商品和余额

shopping_list = [
    ('Iphone',5000),
    ('Macbook Pro',128000),
    ('iWatch',2400),
    ('Ipad',7000)
]
_shopping_list = []
salary = input('请输入余额：')
if salary.isdigit():
    salary = int(salary)
    new_salary = salary
    for index,item in enumerate(shopping_list):
        print(index,item)
    while True:
        product_code = input('请输入购买的商品编号：')
        if product_code.isdigit():
            product_code= int(product_code)
            if product_code < len(shopping_list) and product_code >= 0:
                if new_salary >= shopping_list[product_code][1]:
                    _shopping_list.append(shopping_list[product_code])
                    new_salary = new_salary-shopping_list[product_code][1]
                    print('\033[32;1m%s\033[0m已加入购物车，还剩下余额\033[31;1m%s\033[0m' %(shopping_list[product_code], new_salary))
                else:
                    print('余额已不足，还剩余额%s' %new_salary)
            else:
                print('商品编号不存在')
        elif product_code =='q':
            print('已购买以下商品'.center(50,'-'))
            print(_shopping_list)
            exit()
