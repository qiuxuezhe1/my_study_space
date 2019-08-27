from xml.etree.ElementTree import Element, ElementTree

books = [
    {
        'name': u'Python黑帽子',
        'date': '2015',
        'price': u'37￥',
        'description': u'用python写一些程序'
    },
    {
        'name': u'Web安全深度剖析',
        'date': '2014',
        'price': u'39￥',
        'description': u'讲述web渗透的基础知识'
    },
    {
        'name': u'白帽子讲web安全',
        'date': '2013',
        'price': u'44￥',
        'description': u'道哥力作'
    }        
]


def indent(elem, level=0):
    """美化写入文件的内容"""
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


root = Element('books')
tree = ElementTree(root)

for book in books:
    child0 = Element('book')
    root.append(child0)

    for k,v in book.items():
        child00 = Element(k)
        child00.text = v
        child0.append(child00)

indent(root, 0)
tree.write('aa.xml', 'UTF-8')
