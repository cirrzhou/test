# Author:zhouxy

exit_flag = False
the_choice= []
shop_list = {
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