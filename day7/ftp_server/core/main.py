# Author:zhouxy
import os,sys
import optparse
import socketserver
from conf import settings
from core import server
SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(SETTINGS_PATH)


class ArgvHandle():

    def __int__(self):
        self.op = optparse.OptionParser()
        #self.op.add_option('-s','--s',dest='server')
        #self.op.add_option('-P', '--port', dest='port')
        options,args = self.op.option_args()
        self.verify_agrv(options,args)
#命令分发
    def verify_agrv(self,options,args):
        cmd = args[0]
        if hasattr(self,cmd):
            func=getattr(self,cmd)
            func()

    def start(self):
        s = socketserver.ThreadingTCPServer((settings.IP,settings.PORT),ServerHandle)
        s.serve_forever()

    def help(self):
        pass


