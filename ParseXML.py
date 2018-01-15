from xml.dom.minidom import parse
import xml.dom.minidom
#import requests

def format(text):
    text.replace("\&nbsp","")
    text.split('"')
    return text[1]

def showinfo(node):
    print("nodeName:%s, localName:%s, nodeValue:%s, nodeType:%s, tagName:%s" \
          % (node.nodeName,node.localName,node.nodeValue,node.nodeType,node.tagName))

# 使用minidom解析器打开 XML 文档
#DOMTree = xml.dom.minidom.parse("fund_eastmoney.html")
#page = requests.get("http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=jjcc&code=000577&topline=10&year=&month=&rt=0.07605353511836399")
#doc = format(page.text)
DOMTree = xml.dom.minidom.parse("test.xhtml")

#DOMTree = xml.dom.minidom.parseString(page)
onedoc = DOMTree.documentElement
if onedoc.hasAttribute("shelf"):
   print ("Root element : %s" % onedoc.getAttribute("shelf"))

# 在集合中获取所有电影
tbodys = onedoc.getElementsByTagName("tbody")

for tbody in tbodys:
    showinfo(tbody)
    trs=tbody.getElementsByTagName("tr")
    print("trs[0]:%s" % trs[0])
    for tr in trs:
       showinfo(tr)
       tds=tr.getElementsByTagName("td")
       print("tds[0]:%s" % tds[0])
       if len(tds) == 9:
           for i in [0,1,2,6,7,8]:
               for cn in tds[i].childNodes:
                   print("cn.nodeName:%s, nodeType:%s" % (cn.nodeName, cn.nodeType))
                   if cn.nodeType == cn.TEXT_NODE:
                        if (not cn.data.isspace()):
                            print("tds[%d] data:%s, name:%s, type:%s" %(i,cn.data,cn.nodeName,cn.nodeType))
                   else:
                       for a in cn.childNodes:
                            if a.nodeType == a.TEXT_NODE and (not a.data.isspace()):
                                print("cn.childNodes.data:%s, name:%s, type:%s" % (a.data, a.nodeName, a.nodeType))
       else:
           raise Exception('items in tr is %d. NOT equal to 9. Break!' %len(tds))
    pass

