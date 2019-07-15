```python
import urllib.request
import urllib.response
import urllib.parse


# 1. 语法一：直接传递参数给urlopen
# urllib.request.urlopen(url, data, timeout)

# 第一步设置请求的url
url = 'http://www.baidu.com/'

# 第二步通过urllib.request.urlopen()获取一个HTTPRsponse对象
resp = urllib.request.urlopen(url)

# 第三步read()读取响应内容，默认为bytes类型，所以需要用decode进行解码成utf-8的内容
text = resp.read().decode('utf-8')

# 参数通过data传递给urlopen时，请求方式为post
# 但是urlopen的data接受的是bytes类型的数据，所以需要进行转换，如下
data = {
  'wd': 'python',
  'ed': 'java'
}
# 这里需要将data转换成get请求的url参数那样的格式：wd=python&ed=java,所以它是一个字符串
data = parse.urlencode(data)

# 参数timeout的作用，这个参数的作用是当urlopen请求超过timeout值时，就会抛出urllib.error.URLError: <urlopen error timed out>的错误
url = 'http://www.baidu.com/'
try:
    response3 = request.urlopen(url, timeout=1)
    text3 = response3.read().decode('utf-8')
except urllib.error.URLError as e:
    print('超时')
      
# 2.语法二：将参数传递给urllib.request.Request(),返回一个请求对象，再将请求对象传递给urllib.request.urlopen()
headers = {
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
request_object = urllib.request.Request(url, data, headers)
response_object = urllib.request.urlopen(request_object)

# 3.设置代理ip
# http://httpbin.org/get/一个可以请求之后，返回请求信息的一个网站
url = 'http://httpbin.org/get'
proxies = {
  'http': 'http://59.37.33.62.50686'
}
proxy_handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy_handler)
respnse_object = opener.open(url)
text3 = response_object.read().decode('utf-8')

# 一般使用urllib的爬虫文件结构为
def get_html(url):
  """通过url获取html页面的源码"""
  pass

def parse_html(html):
  """解析get_html返回的html源码，用正则表达式匹配出想要的数据"""
  pass

def main():
  """产生需要的url，调用get_html()和parse_html()函数获得解析后的结果"""
  pass

if __name__ == '__main__':
  main()
```

