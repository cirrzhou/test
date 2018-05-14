# Author:zhouxy
import os
import queue
import select
import socket

server = socket.socket()
server.bind(('localhost',10000))
server.listen(100)
msg_dict = {}
server.setblocking(False) # 必须处于非阻塞的情况
inputs = [server] #inputs = [server,conn]
outputs = [] #[r1],[r2]
while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs) # select监测链接
    print(readable,writeable,exceptional)
    for r in readable:
        if r is server: #代表接入一个新链接
            conn,addr = server.accept()  # 没有新链接会报错
            print(conn, addr)
            inputs.append(conn) # 因为新建立的链接还没发数据，并处于为阻塞的状态，现在接收数据则报错，需要让select监测conn
            msg_dict[conn] =queue.Queue() # 初始化一个队列，后面存要返回给这个客户端的数据
        else:
            data = r.recv(1024)
            print('接收数据',data)
            msg_dict[r].put(data) #r.send(data)
            outputs.append(r) # 放入返回的链接队列里
    for w in writeable: # 要返回给客户端的链接列表
        data_to_client = msg_dict[w].get()
        w.send(data_to_client) #返回给客户端源数据
        outputs.remove(w) #确保下次循环writeable，不返回已经处理完的链接
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dict[e]