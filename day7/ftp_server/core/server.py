# Author:zhouxy
import socketserver
import json
import configparser
from conf import settings


class ServerHandle(socketserver.BaseRequestHandler):
    def handle(self):

        while True:
            conn = self.request
            data = conn.recv(1024).strip()
            data = json.loads(data.decode('utf-8'))
            '''
            {'action':'auth'
             'usrname':
             'password':
            }
           '''
            if data.get('action'):
                    if hasattr(self,data.get('action')):
                        func=getattr(self,data.get('action'))
                        func(**data)
                    else:
                        print('Invalid cmd')
            else:
                print('Invalid cmd')

    def auth(self,**data):
         username = data['username']
         password = data['password']
         self.authenticate(username,password)

    #验证用户是否存在
    def authenticate(self,user,pwd):
        cfg = configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)