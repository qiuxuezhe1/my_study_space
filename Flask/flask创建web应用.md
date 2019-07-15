flask创建一个最小的web应用
```python 
from flask import Flask
app = Flask(__name__)

app.route('/')
def index():
		return 'hello flask'

if __name__ == '__main__':
		app.run()
```
在终端运行此文件
```python
$ python manage.py
	* Running on http://127.0.0.1:5000/
```
flask的web服务默认启动在5000端口

可以通过以下方式将服务启动在指定的ip和端口上，并开启debug模式
```python
app.run(host='127.0.0.1', port='8000', debug=Ture)
```

三方库flask-script用于管理flask应用，使得启动app更加灵活。实现方式如下：
```python
form flask_script import Manage

# 初始化app
manager = Manager(app)
# 运行app
manager.run()
```
终端运行manage.py文件
```python
$ python manage.py -h(host) -p(port) -d 
```
由于一个项目创建app会出现很多配置，所以这里进行了代码的整理，方便管理以及代码更整洁
![项目部分结构图](/Users/mac/Downloads/项目部分结构图.jpg)

### flask项目的配置文件
```python
class Config():
		"""flask项目的配置信息"""
		SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:密码@127.0.0.1:3306/数据库名'
		SQLALCHEMY_TRACK_MODIFICATIONS = False
		SECRET_KEY = 'asdfsfvgesh34rfg'
```
### 利用三方库flask-blueprint来管理路由
```python
from flask import Blueprint

user_blue = Blueprint('user', __name__)

@user_blue.route('/index/', methods=['GET', 'POST'])
def index():
		return render_template('index.html', data=data)
		
@user_blue.route('/jump/')
def jump():
		return redirect(url_for('user.index'))
```

### 创建flask对象的函数
```python
from flask import Flask

from user.models import db
from user.views import user_blue
from utils.config import Config


# 这里的__name__指向当前文件，故如果此文件不在根目录，则应该对static_folder和template_folder参数进行修改，防止app应用找不到对应的静态资源和模板文件
def create_app():
		app = Flask(__name__,
								static_folder='../static',
								template_folder='../templates')

# 加载配置文件, Config类的定义将稍后给出
app.config.from_object(Config)
# 加载蓝图对象,并定义路由前缀为/user
app.register_blueprint(blueprint=user_blue, url_prefix='/user')
# 加载三方sqlalchemy
db.init_app(app)

return app


class Config():
    """
    flask项目的配置信息
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/1902flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'AESDFGJH12345'
```