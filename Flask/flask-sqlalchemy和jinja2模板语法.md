### 一. 知识点散记
flask中继承父模板语法{{ super() }}
django中继承父模板语法{% block.super %}

<link rel="stylesheet" href="/static/css/others.css">
<link rel="styleshhet" href="{{ url_for('static', filename='css/others.css') }}">

{# django中加载样式：{% load static %} {% static 'css/others.css' %} #}


flask中获取data中第二个元素:{{ data[1] }}
django中获取data中第二个元素:{{ data.1 }}


使用封装的三方库flask-sqlalchemy来进行模型的建立和迁移
```python
# 生成对象
db = SQLAlchemy()

# 创建模型字段
# 自增且int类型的主键, 长度11位
id = db.Column(db.Integer, primary_key=True)
# 长度50，且唯一， 不能为空的s_name字段
s_name = db.Column(db.String(50), unique=True, nullable=False)  

# 指定数据库名
__tablename__ = 'stu'


连接数据库：mysql+pymysql://数据库用户名:数据库密码@连接主机的ip
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@47.102.100.231:3306/flaskbase'

# 以下连个方法时flask-sqlalchemy自带的迁移和删除数据库的方法，可以引入三方库flask-migrate来进行模型的管理
# 创建所有模型对应的表，成功不能修改表属性
db.create()

# 删除所有模型对应的表
db.drop_all()
```

### 二. jinja2模板语法简记
模板表达式是包含在分割符{{ }}内

模板控制语句都是包含在分割符{% %}中

模板注释都是包含在分隔符{# #}中

1. 变量: 视图(views)传过来的数据{{ 变量名称 }}
2. 标签：类似于python中的循环分支结构等{% 标签名称 %}{% end标签名称 %}
    + 过滤器
        - {# 过滤器：使用管道符 '|', #}
        {{ content_h2 | safe }}
        
        - {# 去掉标签的样式：striptags #}
        {{ content_h2 | striptags }}
    + 运算符
        - {{ 1+3 }}
    + 操作符
        - in: {{ 1 in [1, 2, 3] }}
    + ~字符串连接
        - {{ 'like'~'you' }}
3. 控制标签
```python
{% for user in users if user.hidden %}
    {% if user.status %}
        xxxx
    {% elif user.name %}
        xxxx
    {% else %}
        xxxx
    {% endif %}
    
    {% if user.is_select %}
        xxxx
    {% endif %}
    
{% else %} # 都不满足执行else
    xxx
{% endfor %}
```
4. for循环内置变量	描述
    + loop.index	获取当前迭代的索引,从1开始
    + loop.index0	获取当期迭代的索引 从0开始
    + loop.first	是否为第一次迭代,返回True或者False
    + loop.last	是否为最后一次迭代 返回True或者False
    + loop.length	迭代的长度
    + loop.depth	当前循环在递归中的层级（从1开始）
    + loop.depth0	当前循环在递归中的层级（从0开始）




