### 1.安装selenium

由于本人使用的是mac，所以主要介绍mac环境的安装。

```python
pip install selenium
```

### 2.安装ChromeDriver

由于本人使用的是Chrome浏览器，所以对应的驱动安装的也是Chrome，没用过其他浏览器，估计按道理应该是需要安装对应的浏览器驱动。

首先确认自己电脑的Chrome版本，打开chrome浏览器设置——关于chrome——查看版本号

![image-20190720191140868](/Users/mac/Library/Application Support/typora-user-images/image-20190720191140868.png)

![image-20190720191230143](/Users/mac/Library/Application Support/typora-user-images/image-20190720191230143.png)

如上图，我的版本号是75.0.3770.142，然后到[官网](http://chromedriver.chromium.org/)(太慢)或[淘宝镜像](http://npm.taobao.org/mirrors/chromedriver/)(推荐)下载，选择对应的版本号，进去之后再选择对应点的操作系统。

**注意：如果没有对应的版本号，就选择最近的版本号试一试。windows系统使用者会看到没有win64的对应驱动，本人建议直接安装win32的，因为我有同学使用windows安装win32能够正常使用**

接下来将压缩包解压，把chromedriver.exe文件拷贝到你对应的python环境变量文件夹下，方便管理。windows拷贝到python的scritp文件夹下。前提是需要配置python环境变量。然后mac打开terminal,windows打开cmd，输入chromedriver。若出现以下情况，则表明环境变量配置成功。

![image-20190720192748118](/Users/mac/Library/Application Support/typora-user-images/image-20190720192748118.png)

原因说明：方便管理；当然可以拷贝到任何环境变的文件夹下，但在若干时间以后，估计你就会忘记你的Chromedriver放在哪里了，不方便以后的版本更新导致需要的旧版本删除。当然不介意内存泄漏的朋友随意。

接下来就可以愉快的玩耍了！O(∩_∩)O哈哈~

### 3.selenium的简单使用

[selenium中文文档](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html)

```python
from selenium import webdriver

# 创建对应的浏览器驱动对象，创建成功会打开一个chrome进程
driver = webdriver.Chrome()
# 通过get请求对应的url，在chrome进程中输入url进行访问
driver.get("http://www.baidu.com")
# 判断url是否请求成功并得到响应，driver.title得到的是url对应的html文档中title标签的内容，在这里即得到"百度一下，你就知道"。即下面语句成功，若失败直接抛出错误。
assert "百度一下，你就知道" in driver.title
# 通过CSS选择器获取输入框
elem = driver.find_element_by_css_selector('#kw')
# 首先清空输入框中的内容，因为selenium不会自动清除获得的输入框内容
elem.clear()
# 向输入框输入内容
elem.send_keys('python')
# 获取百度一下的按钮
button = driver.find_element_by_xpath('//*[@id="su"]')
# 模拟认为进行点击
button.click()
# 关闭chrome进程
driver.close()
```

补充：

```python
# 关于driver.find_element()系列函数获取的对象类型“揭秘”
print(type(button))
<class 'selenium.webdriver.remote.webelement.WebElement'>

# 官方解释称driver.close()关闭的是当前标签，由于上面程序只打开了一个标签，所以chrome默认关闭一个标签的串口就是关闭该chrome进程？事实证明：的确是这样。也可使用一下方式关闭浏览器
driver.quit()
```

ps：官方文档有实例的详细说明[selenium中文文档](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html)

### 4.对页面中的元素进行拖放，比如登录中使用的滑块验证码("极验验证码",或许更应该这么叫，因为更专业)

下面是哔哩哔哩登录界面的**极验验证码**的滑块标签拖动代码

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://passport.bilibili.com/login')
"""<div class="geetest_slider_button" style="opacity: 1; transform: translate(0px, 0px);"></div>"""
# 获取他的xpath语法为


# 获取账号/用户名输入框，密码、登录按钮相同，省略
name_input = driver.find_element_by_xpath('//*[@id="login-username"]')
# 清除账号/用户名输入框内容
name_input.clear()
# 填充账号
name_input.send_keys('d')
password_input = driver.find_element_by_xpath('//*[@id="login-passwd"]')
password_input.clear()
password_input.send_keys('sd')
login_button = driver.find_element_by_xpath('//*[@id="geetest-wrap"]/ul/li[5]/a[1]')
login_button.click()
# 主动睡眠3秒，等待验证码图片加载完成
# 这种做法被认为很糟糕，这里暂时这样写，请继续阅读本文章有关显示等待和隐式等待的讲解
time.sleep(3)

# 获取滑块
slider = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]')

from selenium.webdriver import ActionChains
# 点击滑块并坚持住
ActionChains(driver).click_and_hold(slider).perform()
# 移动滑块，x方向向右移10像素，y方向不动
ActionChains(driver).move_by_offset(xoffset=10, yoffset=0).perform()
# 释放掉滑块
ActionChains(driver).release(slider).perform()
# driver.close()
```

注：为了方便读者粘贴代码运行，故以上紧挨着的python框是后续填充完整的！

### 5.模拟浏览器的前进后退

```python
driver.forward()
driver.back()
```

### 6.查找元素

在一个页面中有很多不同的策略可以定位一个元素。在你的项目中， 你可以选择最合适的方法去查找元素。Selenium结合了CSS选择器、beautifulsoup4、xpath的一些理念，提供了下列的方法给您（如果不理解xpath语法，可通过我的另外一篇文章[XPath的讲解](http://47.102.100.231/article/32)进行了解。）：

- find_element_by_id  
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

**一次查找多个元素 (这些方法会返回一个list列表):**

仅仅是把element改成负数形式，例如find_elements_by_id,其他类推



其实上面的方法可以变成另外一种形式，官方文档这样说：除了上述的公共方法，下面还有两个私有方法。 他们是 find_element 和 find_elements 。

用法实例：

```python
from selenium.webdriver.common.by import By  # 导入By类

# 这里举XPATH的例子，因为官方也是这个，主要还是因为我个人也喜欢用XPATH
driver.find_element(By.XPATH, '//a/@href')
driver.find_elements(By.XPATH, '//a/@href')
```

By类的可用属性，对应到上面的find_element_by_id后面的部分，例如By.ID。

#### 6.1 详解每一个查找元素的方法

**温馨提示：所有的方法都已find_element…单数的形式进行讲解，单数形式查找元素时，当且仅当页面存在该元素时，只会匹配页面中第一个元素，不论有多少个该元素。find_elements...复数形式只不过是返回查到的所有元素，并以列表组装返回。找不到元素会抛出 `NoSuchElementException` (没有这个元素)异常。**

##### 6.1.1 通过ID查找元素

当你知道一个元素的 id 时，你可以使用本方法。在该策略下，页面中第一个该 id 元素会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>
```

可以这样查找表单(form)元素:

```python
login_form = driver.find_element_by_id('loginForm')
login_form = driver.find_element(By.ID, 'loginForm')
```

##### 6.1.2 通过name查找元素

当你知道一个元素的 name 时，你可以使用本方法。在该策略下，页面中第一个该 name 元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:
```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>
```
name属性为 username的元素可以像下面这样查找:
```python
username = driver.find_element_by_name('username')
username = driver.find_element(By.NAME, 'username')
```
##### 6.1.3 通过xpath查找元素

使用XPath的主要原因之一就是当你想获取一个既没有id属性也没有name属性的元素时， 你可以通过XPath使用元素的绝对位置来获取他（这是不推荐的），或相对于有一个id或name属性的元素 （理论上的父元素）的来获取你想要的元素。XPath定位器也可以通过非id和name属性查找元素。

因为只要页面结构允许，它可以长到超乎你的想象。此外绝对的XPath是所有元素都从根元素的位置（HTML）开始定位，只要应用中有轻微的调整，会就导致你的定位失败。 但是通过就近的包含id或者name属性的元素出发定位你的元素，这样相对关系就很靠谱， 因为这种位置关系很少改变，所以可以使你的测试更加强大。

作为示例，页面元素如下所示:
```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>
```

可以这样查找表单(form)元素:

```python
login_form = driver.find_element_by_xpath('/html/body/form[1]')
login_form = driver.find_element_by_xpath('//form[1]')
login_form = driver.find_element_By_xpath('//form[@id="loginForm"]')
login_form = find_element(By.XPATH, '/html/body/form[1]')
login_form = find_element(By.XPATH, '//form[1]')
login_form = find_element(By.XPATH, '//*[@id="loginForm"]')
```

1. 绝对定位 (页面结构轻微调整就会被破坏)
2. HTML页面中的第一个form元素
3. 包含 id 属性并且其值为 loginForm 的form元素

##### 6.1.4 通过链接文本获取超链接

当你知道在一个锚标签中使用的链接文本时使用这个。 在该策略下，页面中第一个匹配链接内容锚标签 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
<html>
```

```python
# 根据连接的完整内容获取
continue_link = driver.find_element_by_link_text('Continue')
# 根据连接的部分内容获取
continue_link = driver.find_element_by_partial_link_text('Conti')
continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
```

##### 6.1.5 通过标签名查找元素

当你向通过标签名查找元素时使用这个。 在该策略下，页面中第一个匹配该标签名的元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <h1>Welcome</h1>
  <p>Site content goes here.</p>
</body>
<html>
```

h1 元素可以如下查找:

```
heading1 = driver.find_element_by_tag_name('h1')
heading1 = driver.find_element(By.TAG_NAME, 'h1')
```

##### 6.1.6 通过Class name 定位元素

当你向通过class name查找元素时使用这个。 在该策略下，页面中第一个匹配该class属性的元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

p 元素可以如下查找:

```python
content = driver.find_element_by_class_name('content')
content = driver.find_element(By.CLASS_NAME, 'content')
```

##### 6.1.7 通过CSS选择器查找元素

当你向通过CSS选择器查找元素时使用这个。 在该策略下，页面中第一个匹配该CSS 选择器的元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

p 元素可以如下查找:

```python
content = driver.find_element_by_css_selector('p.content')
content = driver.find_element(By.CSS_SELECTOR, 'p.content')
```

同样奉上一篇很好的CSS选择器教程：

[Sauce 实验室有一篇很好的文档来介绍CSS选择器](http://saucelabs.com/resources/selenium/css-selectors)

### 7. 等待页面加载完成(Waits)

现在的大多数的Web应用程序是使用Ajax技术。当一个页面被加载到浏览器时， 该页面内的元素可以在不同的时间点被加载。这使得定位元素变得困难， 如果元素不再页面之中，会抛出 ElementNotVisibleException 异常。 使用 waits, 我们可以解决这个问题。waits提供了一些操作之间的时间间隔- 主要是定位元素或针对该元素的任何其他操作。

Selenium Webdriver 提供两种类型的waits - 隐式和显式。 **显式等待**会让WebDriver等待满足**一定的条件**以后再进一步的执行。 而**隐式等待**让Webdriver等待**一定的时间**后再才是查找某元素。

##### 7.1 显式等待

显式等待是你在代码中定义等待一定条件发生后再进一步执行你的代码。 最糟糕的案例是使用time.sleep()，它将条件设置为等待一个确切的时间段。 这里有一些方便的方法让你只等待需要的时间。WebDriverWait结合ExpectedCondition 是实现的一种方式。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://somedomain/url_that_delays_loading")
try:
    # 给当前浏览器对象创建一个等待10秒的显示等待对象
		wait = WebDriverWait(driver, 10)
    # wait.until(指一直等待到这里面的条件满足或者超过10秒为止)
    element1 = wait.until(
        # 判断元素是否能被获取到，否，此处ExpectedCondition会做处理，下面讲解
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
    element2 = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
finally:
    driver.quit()
```

在抛出TimeoutException异常之前将等待10秒或者在10秒内发现了查找的元素。 WebDriverWait 默认情况下会每500毫秒调用一次ExpectedCondition直到结果成功返回。 ExpectedCondition成功的返回结果是一个布尔类型的true或是不为null的返回值。

##### 7.2 隐式等待

如果某些元素不是立即可用的，隐式等待是告诉WebDriver去等待一定的时间后去查找元素。相当于time.sleep()，只不过不建议使用。 默认等待时间是0秒，一旦设置该值，隐式等待是设置该WebDriver的实例的生命周期。

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```



**注：其他更测试联系更紧密的内容还未总结，因为还涉及到python自带的unittest单元测试框架，用于编写和运行可重复的测试**