# Author:zhouxy

import paramiko

transport = paramiko.Transport(('10.10.200.86', 22))
transport.connect(username='nova', password='nova')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()