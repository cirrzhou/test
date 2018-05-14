# Author:zhouxy

# import hashlib
#
# m = hashlib.md5()
# m.update('hello'.encode('utf-8')) #5d41402abc4b2a76b9719d911017c592
# print(m.hexdigest())
# m.update('it’s me'.encode('utf-8')) #衔接hello加密 e36c615cdab6d98c413121f3b90de97a
# print(m.hexdigest())
#
# m2 = hashlib.md5()
# m2.update('helloit’s me'.encode('utf-8'))
# print(m2.hexdigest()) #16进制格式hash e36c615cdab6d98c413121f3b90de97a
# print(m2.digest()) #2进制格式hash

import hmac

h = hmac.new('阿里巴巴'.encode('utf-8'),'芝麻开门'.encode('utf-8'))
print(h.hexdigest())

h2 = hmac.new('阿里巴巴'.encode('utf-8'))
h2.update('芝麻开门'.encode('utf-8'))
print(h2.hexdigest())