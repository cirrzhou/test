# Author:zhouxy

import socket

client = socket.socket()
client.connect(('localhost',10000))
while True:
    cmd = input('>>:').strip()
    if len(cmd) ==0:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)  #接受命令结果的长度
    print('命令大小',cmd_res_size)
    recv_size = 0
    while recv_size != int(cmd_res_size.decode()):
        #print(recv_size)
        data = client.recv(1024)
        recv_size += len(data)   #每次收到可能小于1024，所以必须用len判断
        print(data.decode())
    else:
        print('收到命令大小',recv_size)
client.close()