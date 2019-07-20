### 1.一些基本概念

URI(uniform resource identifier)统一资源标识符

URL(universal resource locator)统一资源定位符

HTTP(hyper text transfer protocol)-超文本传输协议

HTTPS(secure socket layer 安全套接层SSL)-传输内容通过SSL加密，安全通道保证数据传输安全，确保网站真实性。

### 2.请求方法

GET-请求URL的长度根据浏览器的不同而不同

POST、PUT、PATCH等-请求参数通过表单提交，数据大小没有限制

### 3.爬取网页信息的库urllib、urllib2、urllib3、requests

python2系列中可以使用以上所有库名，python自带urllib、urllib2

python3系列中将urllib2整合到了urllib中，所以python自带urllib没有urllib2了

urllib3、requests是三方库，但requests被反映出更好用。

#### 3.1urllib的简单使用

```python
import urllib.request
import urllib.parse


# 只传入url，即请求的网址，此时请求方式为GET
url = "http://www.jd.com"
# 通过request中的urlopen方法去请求url并返回响应对象
resp = urllib.request.urlopen(url)
# read()函数读取响应对象的内容,返回二进制数据，在通过decode进行解码
text = resp.read().decode('utf-8')

# 再传入data参数时，请求方式为POST
url1 = 'https://search.jd.com/Search'
data = {
  'keyword': '%E7%BE%8E%E9%A3%9F'  # 此处为中文的百分号编码，因为浏览器只认识某些特殊符号、数字和字母以及百分号编码的url
}
# 使用urlencode将data转换成key=value&key=value的字符串形式
data_str = urllib.parse.urlencode(data) 
# bytes将data_str转换成bytes类型的数据，urlopen才会请求到正确的地址
data_bytes = bytes(data_str, encoding='utf-8')
resp1 = urllib.request.urlopen(url1, data=data_bytes)
text = resp.read().decode('utf-8')

# urllib.request.urlopen()还可接受一个timeout参数，用来设置请求url的超时时间
resp2 = urllib.request.urlopen(url1, data=data_bytes, timeout=1)
# 这里设置在一秒之内没有请求到数据，则抛出urllib.error.URLError的异常

# 由于urllib加请求头和代理等信息相对麻烦，所以不建议使用urllib，推荐更好用的requests库
```

