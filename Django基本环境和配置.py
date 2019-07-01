1.从GitHub上导入git项目
	在GitHub上创建项目，获取项目的克隆和下载选项的urls地址。
	在pycharm上创建git项目复制urls地址在此处。git项目已下载在pycharm上了

-----------------------------------------------------------------------------------------
2.Django，pymysql的安装，pip的升级，pycharm下配置豆瓣下载源

	pip install -U pip  --  linux下更新
	python -m pip install -U pip  --  window下更新
	pip install django==2.1.8  --  安装Django的2.1.8版本
	django-admin --version  --  查看Django版本
	pip freeze 或 pip list  --  通过pip来查看安装的依赖库及其版本
	在C:\Users\Administrator\pip路径下创建pip.ini内容为：
	[global]
	index-url=https://pypi.doubanio.com/simple

-----------------------------------------------------------------------------------------
3.Django项目的创建，创建应用，基本的配置

	1.使用django-admin创建项目，项目命名为xxx（最好和你的git的项目名一样，英文开头，不能写中文，数字开头）
		django-admin startproject xxx .    --   最后有一个点

				manage.py： 一个让你可以管理Django项目的工具程序。
				oa/__init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
				oa/settings.py：Django项目的配置文件。
				oa/urls.py：Django项目的URL声明（URL映射），就像是你的网站的“目录”。
				oa/wsgi.py：项目运行在WSGI兼容Web服务器上的接口文件。

	2.manage.py：在pycharm左上有个配置项目，配置manage.py的自动启动，加路径和runserver
		启动服务器运行项目。python manage.py runserver 查看是否能访问默认首页

	3.settings.py下配置默认语言修改为中文，时区设置为东八区。
		# 设置语言代码
		LANGUAGE_CODE = 'zh-hans'
		# 设置时区
		TIME_ZONE = 'Asia/Chongqing'

	4.创建名为hrs（人力资源系统）的应用，一个Django项目可以包含一个或多个应用

		python manage.py startapp hrs
			__init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
			admin.py：可以用来注册模型，用于在Django的管理界面管理模型。
			apps.py：当前应用的配置文件。
			migrations：存放与模型有关的数据库迁移信息。
			__init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
			models.py：存放应用的数据模型，即实体类及其之间的关系（MVC/MTV中的M）。
			tests.py：包含测试应用各项功能的测试类和测试函数。
			views.py：处理请求并返回响应的函数（MVC中的C，MTV中的V）。

	5.修改项目的settings.py文件，首先将我们之前创建的应用hrs添加已安装的项目中
			INSTALLED_APPS = [
			    'hrs',
			]

	6.配置MySQL作为持久化方案。
		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.mysql',
		        'NAME': 'oa',
		        'HOST': '127.0.0.1',
		        'PORT': 3306,
		        'USER': 'root',
		        'PASSWORD': '123456',
		    }
		}

	7.如果使用Python 3需要修改项目目录下的__init__.py文件并加入如下所示的代码，
	这段代码的作用是将PyMySQL视为MySQLdb来使用，
	从而避免Django找不到连接MySQL的客户端工具而询问你：“Did you install mysqlclient? ”
		import pymysql
		pymysql.install_as_MySQLdb()
		
	8.Django框架本身有自带的数据模型，我们稍后会用到这些模型，为此我们先做一次迁移操作。
		所谓迁移，就是根据模型自动生成关系数据库中的二维表

		python manage.py makemigrations hrs  --  生成迁移文件
		python manage.py migrate  --  迁移数据

		***数据库已有的表数据迁移到Django项目生成model文件中生成模型***
		
		python manage.py inspectdb > api/models.py


	9.创建超级管理员账号。
		python manage.py createsuperuser

	10.注册模型类 --  后台才看得到可以自定义类来规定显示的内容，比如用有些字段用中文标示，排序等

		from django.contrib import admin
		from hrs.models import Emp, Dept

		admin.site.register(Dept)
		admin.site.register(Emp)


	11.生成.gitignore忽略文件和requirement.txt文件记录项目所依赖的环境软件和版本。
		内容直接访问https://gitignore.io/自动生成（windows，linux，macOS，pycharm等）
		pip freeze > requirement.txt  重定向到requirement.txt里面


	12.加载静态资源
		在上面的模板页面中，我们使用了<img>标签来加载老师的照片，其中使用了引用静态资源的模板指令{% static %}，
		要使用该指令，首先要使用{% load static %}指令来加载静态资源，
		我们将这段代码放在了页码开始的位置。在上面的项目中，我们将静态资源置于名为static的文件夹中，
		在该文件夹下又创建了三个文件夹：css、js和images，分别用来保存外部层叠样式表、
		外部JavaScript文件和图片资源。为了能够找到保存静态资源的文件夹，
		我们还需要修改Django项目的配置文件settings.py，如下所示：

		
				# 此处省略上面的代码
				STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
				STATIC_URL = '/static/'
				# 此处省略下面的代码


	13.给pycharm配置密钥对，免密登录。
--------------------------------------------------------------------------------------------------------
4.Django模型最佳实践
		1.正确的为模型和关系字段命名。
		2.设置适当的related_name属性。
		3.用OneToOneField代替ForeignKeyField(unique=True)。
		4.通过“迁移操作”（migrate）来添加模型。
		5.用NoSQL来应对需要降低范式级别的场景。
		6.如果布尔类型可以为空要使用NullBooleanField。
		7.在模型中放置业务逻辑。
		8.用<ModelName>.DoesNotExists取代ObjectDoesNotExists。
		9.在数据库中不要出现无效数据。
		10.不要对QuerySet调用len()函数。
		11.将QuerySet的exists()方法的返回值用于if条件。
		12.用DecimalField来存储货币相关数据而不是FloatField。
		13.定义__str__或__repr__方法。
		14.不要将数据文件放在同一个目录中。


