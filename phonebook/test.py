import dicttoxml
from xml.dom.minidom import parseString

d = {'k':[{'k1':'v1'}, {'k2':'v2', 'k3':'v3'}]}
xml = dicttoxml.dicttoxml(d, attr_type=False, root=False)
print(xml)

dom = parseString(xml)
xml = dom.toprettyxml()
print(xml.split('<?xml version="1.0" ?>'))