# Author:zhouxy

# 建立一个多层字典
chinese_catelog = {
    '广东省':{
        '广州市':{
            '越秀区',
            '荔湾区',
            '天河区',
            '番禺区',
            '白云区',
        },
        '深圳市':{
            '南山区':['长亮科技','深圳湾科技生态园'],
            '福田区':['平安银行','平安银行大厦'],
            '罗湖区':[],
            '宝安区':[],
        },
        '珠海市':{},
        '东莞市':{},
        '汕头市':{},
    },
    '江苏省':{
        '南京市',
        '苏州市',
        '扬州市',
        '南通市',
    },
}
exit_flag = False

while exit_flag is not True:
    for i1 in chinese_catelog: # 循环打印省列表
        print(i1)
    choice1 = input('请输入所在省：')
    if choice1 in chinese_catelog: # 如果输入存在省
        while exit_flag is not True:
            for i2 in chinese_catelog[choice1]:  # 循环打印市列表
                print(i2)
            choice2 = input('请输入所在市：')
            if choice2 in chinese_catelog[choice1]: # 如果输入存在市
                while exit_flag is not True:
                    for i3 in chinese_catelog[choice1][choice2]: # 循环打印区列表
                         print(i3)
                    choice3 = input('请输入所在区：')
                    if choice3 in chinese_catelog[choice1][choice2]: # 如果输入存在区
                        while exit_flag is not True:
                            for i4 in chinese_catelog[choice1][choice2][choice3]:
                                print(i4)
                            choice4 = input('已选择完成，请按b返回')
                            if choice4 == 'b':
                                break
                            elif choice4 == 'q':
                                exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 =='q':
                        exit_flag = True
            if choice2 == 'b':
                break
            if choice2 == 'q':
                exit_flag = True






















'''
import sys
import shop

shop_list = shop.shop_list
exit_flag = False
the_choice = []

while exit_flag is not True:
    for i in shop_list:
        print (i)
    choice1 = input ("Please input your choice:")
    if choice1 in shop_list:

        for a in shop_list[choice1]:
            print (a)
        choice2 = input ("Please input your choice2:")
        if choice2 in shop_list[choice1]:

            for c in shop_list[choice1][choice2]:
                print (c)
            choice3 = input ("Please input your choice3:")
            if choice3 in shop_list[choice1][choice2]:

                the_choice.append(choice3)
            elif choice3 == 'b':
                continue
            elif choice3 == 'q':
                exit_flag = True
            else:
                print ("No your choice")
                continue
        elif choice2 == 'b':
            continue
        elif choice2 == 'q':
            exit_flag = True
        else:
            print ("No your choice")
            continue
    elif choice1 == 'b':
        continue
    elif choice1 == 'q':
        exit_flag = True
        print (the_choice)
        break
        sys.exit()
    else:
        print ("No your choice")
        continue
'''