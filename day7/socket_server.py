# Author:zhouxy

import os
import socket

server = socket.socket() ##声明一个socket实例
server.bind(('localhost',6467))
server.listen()
while True:
    conn,addr = server.accept() #conn是客户端连接在服务端为其生成的一个连接实例
    print('new_conn:',conn)
    while True:
        data = conn.recv(1024)   # recv默认是阻塞的
        if not data:  #print(data.decode()) 客户端已断开，conn.recv收到就都是空数据
            print('断开连接')
            break     # 重新接入新链接
        print('执行指令',data.decode())
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) ==0:
            cmd_res='没有指令'
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))   #先发送大小给客户端
        conn.send(cmd_res.encode('utf-8'))
        print('完成发送')
server.close()




