# Author:zhouxy
# 1、查
#     输入：www.oldboy.org
#     获取当前backend下的所有记录
#
# 2、新建
#     输入：
#         arg = {
#             'bakend': 'www.oldboy.org',
#             'record':{
#                 'server': '100.1.7.9',
#                 'weight': 20,
#                 'maxconn': 30
#             }
#         }
#
# 3、删除
#     输入：
#         arg = {
#             'bakend': 'www.oldboy.org',
#             'record':{
#                 'server': '100.1.7.9',
#                 'weight': 20,
#                 'maxconn': 30
#             }
#         }


#
#
#{'backend': 'www.leslie.com','record':{ 'server': '100.1.7.8' ,'weight': 10,'maxconn': 1000 }}
import shutil

#选项菜单
def choice():
    print ("Welcome".center(40,'#'))
    choice_list = ["1.查询","2.添加","3.删除","4.修改","q.退出"]
    print (choice_list)

#文件备份
def copy():
    shutil.copyfile('haproxy','haproxy.txt')

#查询
def query(backend):
    flag = False
    query_list = []
    with open ('haproxy','r',encoding="utf-8") as file:
        for line in file:
            if line.strip() == 'backend %s'% backend:
                flag = True
                continue
            if line.strip().startswith('backend'):
                flag = False
            if flag and line.strip():
                query_list.append(line.strip())
    return query_list

#内容添加
def add (dict_list):
    dict_list = eval(dict_list)
    backend_name = dict_list.get('backend')
    backend_context = (("backend %s")%backend_name)
    record_name = dict_list["record"]
    record_context = ("server %s %s weight %s maxconn %s"%(record_name['server'],record_name['server'],record_name['weight'],record_name['maxconn']))
    record_list = query(backend_name)
    flag = False
    if  record_list:
        write_flag = False
        with open ('haproxy','r',encoding="utf-8") as file_old ,open ('haproxynew','w',encoding="utf-8") as file_new:
            for line in file_old:
                if line.strip() == backend_context:
                    file_new.write("\n" + line)
                    flag = True
                    continue
                if flag and line.startswith('backend'):
                     flag = False
                if flag:
                    for line_new in record_list:
                        if not write_flag:
                            file_new.write(line_new)
                            write_flag = True
                else:
                    file_new.write(line)
    else:
         with open ('haproxy','r',encoding="utf-8") as file_old ,open ('haproxynew','w',encoding="utf-8") as file_new:
             for line in file_old:
                 file_new.write(line)
             file_new.write("\n" + backend_context + "\n")
             file_new.write(" "*8 + record_context +"\n")
             flag = True
    if flag is  True:
        shutil.move('haproxynew','haproxy')

#内容删除
def delete (dict_list):
    dict_list = eval(dict_list)
    backend_del = dict_list['backend']
    record_del = dict_list['record']
    backend_context = ('backend %s'%backend_del)
    record_context = ("server %s %s weight %s maxconn %s"%(record_del['server'],record_del['server'],record_del['weight'],record_del['maxconn']))
    query_list = query(backend_del)
    if not query_list:
        return
    else:
        if record_context not in query_list:
            print ("IT is not in it ")
            return
        else:
            query_list.remove(record_context)
        with open ('haproxy','r',encoding="utf-8") as file_old ,open ('haproxynew','w',encoding="utf-8") as file_new:
            flag = False
            write_flag = False
            for line in file_old:
                if line.strip()== backend_context:
                    file_new.write(line)
                    flag = True
                    continue
                if flag and line.startswith('backend'):
                    flag = False
                if flag:
                    if not write_flag:
                        print (query_list)
                        for line in query_list:
                            file_new.write("%s%s\n"%(""*8,line))
                        write_flag = True
                else:
                    file_new.write(line)
        if flag is  True:
            shutil.move('haproxynew','haproxy')

#内容修改
def change (dict_list):
    dict_list = eval(dict_list)
    backend_name = dict_list.get('backend')
    backend_context = (("backend %s")%backend_name)
    record_name = dict_list["record"]
    record_context = ("server %s  weight %s maxconn %s"%(record_name['server'],record_name['weight'],record_name['maxconn']))
    record_context_new =["server %s  weight %s maxconn %s"%(record_name['server'],record_name['weight'],record_name['maxconn'])]
    record_list = query(backend_name)
    record_list_new = str(record_list)
    flag = False
    if not record_list:
        with open ('haproxy','r',encoding="utf-8") as file_old ,open ('haproxynew','w',encoding="utf-8") as file_new:
            for line in file_old:
                file_new.write(line)
            file_new.write("\n" + backend_context +"\n")
            file_new.write(" "*8 + record_context +"\n")
            flag = True
    if record_list:
        with open ('haproxy','r',encoding="utf-8") as file_old ,open ('haproxynew','w',encoding="utf-8") as file_new:
            for line in file_old:
                file_new.write(line)
                if line.strip() == backend_context:
                    if record_list == record_context_new:
                        print ("It is in now".center(40,"#"))
                        continue
                    else:
                        for line in file_old:
                            if line.strip().startswith('server'):
                                line = (" "*8 + record_context + "\n")
                                file_new.writelines(line)
                                file_new.flush()
                                flag = True

    if flag is True:
        shutil.move('haproxynew','haproxy')


flag = False
while flag is not True:
    choice()
    choice_list = input ("Please input your choice:").strip()
    if choice_list.strip() == '1':
        copy()
        backend_name = input ("Please input backend:").strip()
        result = query(backend_name)
        print (result)
    elif choice_list.strip() == '2':
        copy()
        backend_list_dict = (input("Please input your backend:").strip())
        add(backend_list_dict)
    elif choice_list.strip() == '3':
        copy()
        backend_list_dict = (input("Please input your backend:").strip())
        delete(backend_list_dict)
    elif choice_list.strip() == '4':
        copy()
        backend_list_dict = (input("Please input your backend:").strip())
        change(backend_list_dict)
    elif choice_list.strip() == 'q':
            print ("GOOD BYE".center(40,'#'))
            flag = True
            exit('quit')
    else:
        print ("Sorry what is your input is error")