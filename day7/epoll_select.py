# Author:zhouxy

import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)  #非阻塞
    sel.register(conn, selectors.EVENT_READ, read) # 新建立的链接注册read回调函数

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select() # 默认是阻塞，有活动链接就返回活动的链接列表
    for key, mask in events:
        callback = key.data   # 相当于调accept
        callback(key.fileobj, mask)  # key.fileobj= 文件句柄相当于还没建立链接的r