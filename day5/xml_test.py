# Author:zhouxy
#import xml.etree.cElementTree as ET

# tree = ET.parse('xml_test.xml')
# root = tree.getroot()
# print(root.tag)
# #遍历xml文档
# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.text,i.attrib)
# #遍历year节点
# for note in root.iter('year'):
#     print(note.tag,note.text)

# import xml.etree.cElementTree as ET
#
# tree = ET.parse('xml_test.xml')
# root = tree.getroot()
#
# #修改
# for node in root.iter('year'):
#     new_year = int(node.text)+1
#     node.text = str(new_year)
#     node.set('updated','zhouxy') #增加属性
# tree.write('xml_test.xml')
#
# #删除
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
# tree.write('xml_test.xml')


import xml.etree.ElementTree as ET

name_xml = ET.Element("namelist")  #创建根节点并赋值给一个对象
name = ET.SubElement(name_xml, "name", attrib={"enrolled": "yes"}) #创建一级子节点
name.text = 'zhouxy'
age = ET.SubElement(name, "age", attrib={"checked": "no"}) #创建二级子节点
age.text = '18'
sex = ET.SubElement(name, "sex") #创建二级子节点
sex.text = 'F'
name2 = ET.SubElement(name_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")

et = ET.ElementTree(name_xml)  # 生成文档对象
et.write("name.xml", encoding="utf-8", xml_declaration=True)

ET.dump(name_xml)  # 打印生成的格式