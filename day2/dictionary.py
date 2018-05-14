# Author:zhouxy

'''
info = {
    'zhouxy':'A',
    'panjq':'B',
    'lijm':'C',
    'caiyq':'D'
}
print(info)
print(info['zhouxy']) # 取值
info['zhouxy'] = "周小律" # 修改
info['linjm'] = '新增' # 不存在key值则新增
del info['caiyq'] # 删除
info.pop('panjq') # 删除
print(info)
info.popitem() # 随机删除
print(info)
print(info.get('liangjs')) # 不存在查找
print('liangjs' in info) # 是否存在，info.has_key("liangjs") in py2f.x
'''
'''
info = {
    'zhouxy':'A',
    'panjq':'B',
    'lijm':'C',
    'caiyq':'D'
}
print(info.values()) # 取全部value值
print(info.keys()) # 取全部key值
print(info.items()) # 字典转列表
print(info.setdefault('xyzhou','a')) # 不存在key则新增
print(info.setdefault('zhouxy','a')) # 相同key值不修改

name2 = {
    'zhouxy':'zxy',
    'liangjs':'梁胖'
}
print(info.update(name2)) # 不存在key则新增，相同key则更新

new = dict.fromkeys([1,2,3],['1',{'name':'level'},'a']) # 初始化新字典
print(new)
new [1][1]['name'] = 'Name'
print(new) # 多层修改，改则全改
'''
info = {
    'zhouxy':'A',
    'panjq':'B',
    'lijm':'C',
    'caiyq':'D'
}
for i in info:
    print(i,info[i])





