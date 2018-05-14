# Author:zhouxy

import optparse
import socket
import json

class ClientHandle():
    def __int__(self):
        self.op=optparse.OptionParser()
        self.op.add_option('-s','--server',dest='server')
        self.op.add_option('-P','--port',dest='port')
        self.op.add_option('-u','--username',dest='username')
        self.op.add_option('-p','--pwd',dest='password')

        self.options,self.args = self.op.parse_args()
        self.verify_args(self.options,self.args)
        self.makeconnect()
    #判断端口是否合法
    def varify_args(self,options,args):
        server =options.server
        port = options.port
        username = options.username
        passeword = options.pwd

    def  makeconnect(self):
        self.sock=socket.socket()
        self.sock.connect=(self.options.server,int(self.options.port))

    def interacticate(self):
        self.authenticate()
    #验证
    def authenticate(self):
        if self.options.username is None or self.options.pwd is None:
            username = input('username:')
            password = input('password:')
         return self.get_auth_result(self.options.username,self.options.pwd)

    def respose(self):

        data = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data)
        return  data

    def get_auth_result(self,user,pwd):

         data = {
             'action':'auth',
             'username':user,
             'password':pwd
         }
        self.sock.sent(json.dumps(data).encode('utf-8'))
        res= self.response()
        print(res)

ch = ClientHandle()
#交互
ch.interacticate()