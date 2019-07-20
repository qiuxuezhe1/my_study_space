### 1. XPath概念

**XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航。**

### 2.以lxml中的etree为例

ps:值得注意的是最新版的lxml中没有etree模块，神奇的是用以下方式导入，pycharm虽然会报红，但任然可以使用。

```python
from lxml import etree

# 获取html整个文档的lxml.etree._Element的对象
tree = etree.xpath(html)

# 获取所有的a标签的lxml.etree._Element的对象，返回一个列表
a = tree.xpath('//a')
```

更多用法在下表列出

### 3. 节点（略）

[文档教程](http://www.w3school.com.cn/xpath/xpath_nodes.asp)

### 4. XPath语法

**XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。**
|  表达式  |  描述  |
|  :--  |  :--  |
|  /  | 从根节点开始选取 |
|  //  |  从任意位置开始向下匹配(**常用**)  |
|  .  | 从当前节点开始向下匹配  |
|  ..  |  从当前节点的父节点开始匹配  |
|  @  |  匹配属性(**常用**)  |
|  //div/ul[2]/li/@id  |  获取所有div标签下面的第二个ul标签下面的所有li标签的id属性的值(**常用**)  |
|  //@href  |  选取所有href的属性值(**常用**)  |
|  \* 或 ./\*  |  选取当前路径下的所有直接节点  |
|  /*  |  选取根路劲下的直接节点，即html，所以意义不大  |
|  //*  |  选取任意位置的任意节点(**常用**)。例如：//*[@class="item"]选取class属性为item的所有节点  |
|  //a/text()  |  选取所有a节点的文本(**常用**)  |

注：若觉得此总结看不懂，可参考[菜鸟教程](https://www.runoob.com/xpath/xpath-syntax.html)或[W3CSchool教程](http://www.w3school.com.cn/xpath/xpath_syntax.asp)。

### 5.XPath 轴（Axes）、运算符

目前本人用得少，若有需要，请点击以上两个教程网站参考。