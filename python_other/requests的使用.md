### 1.requests库的请求方式

请求方式相当简单，直接requests.请求方式(url)

1.1 GET请求

无参： resp = requests.get(url)

有参：resp = requests.get(url, params={'key': 'value'})

1.2 POST、PUT、PATCH等请求

resp = requests.post(url, data={'key': 'value'})

### 2.requests响应

```python
resp = requests.get(url)
# 直接通过resp.text就能获取已经解码的html字符串
html = resp.text
# 也有获取二进制数据的属性
content_bytes = resp.content
```

### 3.requests设置请求头和代理，以及不使用SSL证书验证

```python
# headers和proxies都是字典形式
resp = requests.get(url, headers=headers, proxies=proxies, verify=false)
```

### 4.requests请求对象

```python
resp = requests.get(url)

# 获取请求的url,当请求url有参数分离传递时，或许这个很有用
resp.url
# 获取响应内容，已经通过utf-8解码
resp.text
# 获取requests的编码方式
resp.encoding
# 获取响应的二进制数据
resp.content
# 官网给出的存图片的代码
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(resp.content))
i.save('保存的图片名.png/.jpg')
```





