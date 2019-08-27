### 1.django请求方式的判断

django中urls.py文件并不会判断此次请求的方法，请求方式是在视图函数这里进行判断的。

### 2.错误页面的处理

django自带的错误提示有400(请求错误)、403(请求被禁止或禁止访问)、404(页面不存在)和500(服务器错误),这些错误对应如下：

- handler400 —— django.conf.urls.handler400。
- handler403 —— django.conf.urls.handler403。
- handler404 —— django.conf.urls.handler404。
- handler500 —— django.conf.urls.handler500。

其底层调用的视图函数返回值有多简陋，恐怕你想象不到，让我来给你们看一个例子：return HttpResponseBadRequest('<h1>Bad Request (400)</h1>', content_type='text/html')

这就是400错误返回的页面，说实话，这的确对于我们程序员来说太low了。接下来就说说怎么修改它，其实很简单，你进去看它们的第一层源码，具体如下：

```python
handler400 = defaults.bad_request
handler403 = defaults.permission_denied
handler404 = defaults.page_not_found
handler500 = defaults.server_error
```

而赋值号右边是一个视图函数，这样一来，我们不就可以以相同的方式给这些错误重新赋予新的视图函数，不就可以改变这些错误的html页面了吗。答案就是这么简单，但是还有一个讲究，就是将下面的代码放在项目的跟urls.py文件中，我相信你应该知道我说的是哪个urls文件吧。

```python
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error
```

添加以上内容之后，你还需要做的就是无视图文件views.py中实现这些视图函数。

### 3.使用ORM框架进行增删改查

首先定义一个模型如下：

```python
from django.db import models


class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    intro = models.TextField('摘要', max_length=200, blank=True)

    class Meta:
        db_table = 'tb_article'
```

#### 3.1 增加数据

```python
from models import Article
# 方式1
dict1 = {'title': '文章一', 'intro': '文章摘要'}
Article.objects.create(**dict1)
# 方式2
article = Article()
article.title = '文章2'
article.save()
```

#### 3.2 查询数据

```python
article = Article.objects.filter(id=1)    # 得到一个查询集对象QuerySet
article = Article.objects.filter(id=1).first()    # 得到查询集对象中的第一个Article对象
# 按id进行降序排列查询
articles = Article.objects.order_by('-id').all()
```



#### 3.3 删除数据

```python
article = Article.objects.filter(id=1)
article.delete()
```

#### 3.4 修改数据

```python
article = Article.objects.filter(id=2)
article.update(title='修改标题')
```



### 4. HttpRequest对象

视图函数默认接收的参数就是一个HttpRequest对象，接下来介绍其中常用的一些属性和方法

#### 4.1 request.path:获取请求的路由

值得注意的是，request.path获取的仅仅是去掉域名的路由部分，即urls.py文件中path定义的路由

```python
def index(request):
    # url = http://127.0.0.1:8000/post/23?page=1
    print(request.path)  # /post/23
    # 获取完整的path
    print(request.get_full_path())  # post/23?page=1
```

#### 4.2 request.method:获取请方式

前面的文章已经说了urls.py文件无法判断请求的方式，是通过django的视图函数去判断，而这里就是通过这个属性进行判断的

```python
print(request.method)  # GET POST PUT PATCH DELETE UPDATE等
```

#### 4.3 request.body:含所有的请求体信息，bytes类型

#### 4.4 request.GET:获取GET方式传递的参数，QueryDict类型

```python
# url = http://127.0.0.1:8000/index/?name=tom&age=18
print(request.GET.get('name'))  # tom
```

#### 4.5 request.POST：获取POST请求的数据，应该说包括所有的form表单传递的数据

#### 4.6 request.COOKIES,包含所有cookies的标准Python字典对象；keys和values都是字符串。

#### 4.7 request.FILES

包含所有上传文件的类字典对象；FILES中的每一个Key都是<input type="file" name="" />标签中name属性的值，FILES中的每一个value同时也是一个标准的python字典对象，包含下面三个Keys：filename：上传文件名，用字符串表示、content_type:上传文件的Content Type、content：上传文件的原始内容。

#### 4.8 request.user

是一个django.contrib.auth.models.User对象，代表当前登陆的用户。如果访问用户当前没有登陆，user将被初始化为django.contrib.auth.models.AnonymousUser的实例。你可以通过user的is_authenticated()方法来辨别用户是否登陆：if request.user.is_authenticated();只有激活Django中的AuthenticationMiddleware时该属性才可用。

#### 4.9 request.session

唯一可**读写**的属性，代表当前会话的字典对象；自己有激活Django中的session支持时该属性才可用

#### 5. HttpResponse对象

#### 1. render函数

render(request, template_name[, context=None, content_type=None, status=None, using=None])

```python
def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    print(request.body)
    context = {
        'blog_index':blog_index,
    }
    return render(request, 'index.html',context)
```

参数说明：

request： 用于生成响应的请求对象。
template_name：要使用的模板的完整名称，可选的参数
context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。
content_type：生成的文档要使用的MIME类型(不了解MIME类型的，查一下百度)。默认为DEFAULT_CONTENT_TYPE 设置的值。
status：响应的状态码。默认为200。

render方法主要是将从服务器提取的数据，填充到模板中，然后将渲染后的html静态文件返回给浏览器。这里一定要注意：render渲染的是模板。

### 2. redirect函数

一个绝对的或相对的URL

```python
def test_view(request):
    ...
    return redirect('/index/')

def test_view1(request):
    ...
    return redirect('http://www.ybhx.xyz/')
```

### 3. render和redirect区别

1. 一个视图函数返回一个登陆成功后的页面，此时浏览器的url还是之前的登录url，所以刷新页面时，就等于刷新登录页面。而redirect是重定向到指定的url，此时浏览器中的url已经是非登录url的另外一个url。所以此时刷新的就是重定向之后的url。
2. redirect的实质是通过传入的url经过路由系统的分配去执行url对应的视图函数。相当于在你登录成功后，redirect让django系统自动帮你访问对应的url，并给你返回相应的页面。