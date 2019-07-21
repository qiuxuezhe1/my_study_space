### 1.安装和导入的差别

pip install beautifulsoup4

from bs4 import BeautifulSoup

### 2.解析器的比较

python自带html.parser解析器
	 BeautifulSoup(resp.text, "html.parser")速度一般，容错能力好
lxml HTML解析器
	 BeautifulSoup(resp.text, "lxml")速度快，容错好
lxml xml解析器 
	 BeautifulSoup(resp.text, "xml")速度快，但只支持xml
html5lib解析器
	 BeautifulSoup(resp.text, "html5lib")最好的容错性，速度慢
注： html5lib拥有最好容错性的原因是因为他会以浏览器的方式解析文档，并自动补全不完整的标签，所以只要浏览器能正确显示，html5lib就能正确的获取，进而生成html5的文档

### 3.Tag对象

ps：本文档之后的讲解都将基于下面的soup对象

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>学习爬虫好开心</title></head>
<body>
<p class="title" name="dromouse"><b>(￣ＴＴ￣)笔芯</b></p>
<p class="story">喵了个猫
<a href="http://example.com/elsie" class="sister" id="link1">汪汪汪，汪星人</a> and
<a href="http://example.com/lacie" class="sister" id="link2">喵喵喵，喵星人</a>
最后变成一锅汤</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# 通过标签名直接获取，但当html字符串中有对个相同标签时，这个方法只能获取第一个标签
soup.a
# 通过字典的操作获取标签的属性，对于多值属性，例如class可同时拥有多个值，则返回list
soup.a['class']
# NavigableString对象.以下两者获取的内容相同，但text得到的额是字符串，string得到的是NavigableString对象
soup.a.text
soup.a.string
# 拥有子节点的标签
soup.p.b  # <b>(￣ＴＴ￣)笔芯</b>
soup.body.contents # 获取body标签写所有子标签的列表，会匹配换行
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
soup.html.string # None

# parent标签的父节点，html的父节点是BeautifulSoup对象
soup.html.parent
# next_sibling下一个兄弟节点
soup.p.next_sibling
# previous_sibling上一个兄弟节点
# 但往往这两个方法的结果是换行符和顿号
```

### 4.搜索文档树(find/find_all)

#### 4.1 其中的过滤器

##### 4.1.1 字符串

搜索匹配第一个a标签，等同于Tag对象中的soup.a

```python
soup.find('a')
```

搜索匹配所有的a标签，返回一个列表

```python 
soup.find_all('a')
```

##### 4.1.2 正则表达式

传入正则表达式对象，搜索标签名字中包含’o‘的标签

```python
soup.find_all(re.compile('o'))
```

##### 4.1.3 列表

 传入字符串的列表，搜索匹配出所有字符串对象的标签，返回list

```python
soup.find_all(['a','b']) # 将同时搜索a标签和b标签
```

##### 4.1.4 True和方法略

[官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#tag)

### 5.find_all()详解

find_all(name, attrs, recursive, text, **kwargs)

#### 5.1 name参数

name参数可以查找所有名字为name的tag，字符串对象会被自动忽略掉。

重申：搜索 `name` 参数的值可以使任一类型的过滤器,字符窜,正则表达式,列表,方法或是 `True` .

#### 5.2 keyword参数

如果一个指定名字的参数不是搜索内置的参数名(`name`, `attrs`,` recursive`,` text`),搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 `id` 的参数,Beautiful Soup会搜索每个tag的”id”属性.

```python
soup.find_all(id='link2')
```

搜索指定名字的属性时可以使用的参数值包括字符串、正则表达式、列表、True。

下面的例子在文档树中查找所有包含 `id` 属性的tag,无论 `id` 的值是什么:

```python
soup.find_all(id=True)
```

使用多个指定名字的参数可以同时过滤tag的多个属性

```python
soup.find_all(href=re.compile("elsie"), id='link1')
```

注：每一个关键字参数都可以接受不同类型的过滤器：字符串、正则表达式、方法或True

#### 5.3 text参数

通过 `text` 参数可以搜搜文档中的字符串内容.与 `name`参数的可选值一样, `text` 参数接受字符串、正则表达式、方法或True

```python
soup.find_all(text=re.compile(r'喵'))
# ['喵了个猫\n', '喵喵喵，喵星人']
```

#### 5.4 recursive参数

是否递归搜索标签下的子标签。调用tag的 `find_all()` 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 `recursive=False` .

```python
soup.html.find_all('title', recursive=False)
# 返回空列表，只在html的直接子节点中查找title标签
```

### 6.不得不知道的简写(因为太方便)

`find_all()` 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. `BeautifulSoup` 对象和 `tag` 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 `find_all()` 方法相同,下面两行代码是等价的（官方原话）:

```python
soup.find_all('a')
soup.('a')
```

关于find('html')的简写(其实一直在用，只是不知道)

```python
soup.html # 实质是在下面形式的简写
soup.find('html')
```

### 7.CSS选择器

使用select方法查找CSS中的类选择器和id选择器

```python
soup.select('.title')
soup.select('#link1')
```

