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



