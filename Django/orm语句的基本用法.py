使用ORM完成模型的CRUD操作
在了解了Django提供的模型管理平台之后，
我们来看看如何从代码层面完成对模型的CRUD（Create / Read / Update / Delete）操作。
我们可以通过manage.py开启Shell交互式环境，然后使用Django内置的ORM框架对模型进行CRUD操作。
		(venv)$ python manage.py shell
		Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
		[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
		Type "help", "copyright", "credits" or "license" for more information.
		(InteractiveConsole)
		>>> 


1.新增
	>>> from hrs.models import Dept, Emp
	>>>
	>>> dept = Dept(40, '研发2部', '深圳')
	>>> dept.save()

2.更新
	>>> dept.name = '研发3部'
	>>> dept.save()
3.查询
	1)查询所有对象。
		>>> Dept.objects.all()
		<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>, <Dept: 运维1部>, <Dept: 研发3部>]>


	2)过滤数据。
		>>> Dept.objects.filter(name='研发3部') # 查询部门名称为“研发3部”的部门
		<QuerySet [<Dept: 研发3部>]>
		>>>
		>>> Dept.objects.filter(name__contains='研发') # 查询部门名称包含“研发”的部门(模糊查询)
		<QuerySet [<Dept: 研发1部>, <Dept: 研发3部>]>
		>>>
		>>> Dept.objects.filter(no__gt=10).filter(no__lt=40) # 查询部门编号大于10小于40的部门
		<QuerySet [<Dept: 销售1部>, <Dept: 运维1部>]>
		>>>
		>>> Dept.objects.filter(no__range=(10, 30)) # 查询部门编号在10到30之间的部门
		<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>, <Dept: 运维1部>]>


	3)查询单个对象。
		>>> Dept.objects.get(pk=10)
		<Dept: 研发1部>
		>>>
		>>> Dept.objects.get(no=20)
		<Dept: 销售1部>
		>>>
		>>> Dept.objects.get(no__exact=30)
		<Dept: 运维1部>
		>>>
		>>> Dept.objects.filter(no=10).first()
		<Dept: 研发1部>


	4)排序数据。
		>>> Dept.objects.order_by('no') # 查询所有部门按部门编号升序排列
		<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>, <Dept: 运维1部>, <Dept: 研发3部>]>
		>>>
		>>> Dept.objects.order_by('-no') # 查询所有部门按部门编号降序排列
		<QuerySet [<Dept: 研发3部>, <Dept: 运维1部>, <Dept: 销售1部>, <Dept: 研发1部>]>


	5)数据切片（分页查询）。
		>>> Dept.objects.order_by('no')[0:2] # 按部门编号排序查询1~2部门
		<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>]>
		>>>
		>>> Dept.objects.order_by('no')[2:4] # 按部门编号排序查询3~4部门
		<QuerySet [<Dept: 运维1部>, <Dept: 研发3部>]>


	6)高级查询。
		>>> Emp.objects.filter(dept__no=10) # 根据部门编号查询该部门的员工
		<QuerySet [<Emp: 乔峰>, <Emp: 张无忌>, <Emp: 张三丰>]>
		>>>
		>>> Emp.objects.filter(dept__name__contains='销售') # 查询名字包含“销售”的部门的员工
		<QuerySet [<Emp: 黄蓉>]>
		>>>
		>>> Dept.objects.get(pk=10).emp_set.all() # 通过部门反查部门所有的员工
		<QuerySet [<Emp: 乔峰>, <Emp: 张无忌>, <Emp: 张三丰>]>


4.删除
>>> Dept.objects.get(pk=40).delete()
(1, {'hrs.Dept': 1})




按字段查找可以用的条件：https://github.com/jackfrued/Python-100-Days/blob/master/Day91-100/95.%E4%BD%BF%E7%94%A8Django%E5%BC%80%E5%8F%91%E9%A1%B9%E7%9B%AE.md

QuerySet的方法
get() / all() / values()
说明：values()返回的QuerySet中不是模型对象而是字典
count() / order_by() / exists() / reverse()
filter() / exclude()
exact / iexact：精确匹配/忽略大小写的精确匹配查询
contains / icontains / startswith / istartswith / endswith / iendswith：基于like的模糊查询
in：集合运算
gt / gte / lt / lte：大于/大于等于/小于/小于等于关系运算
range：指定范围查询（SQL中的between…and…）
year / month / day / week_day / hour / minute / second：查询时间日期
isnull：查询空值（True）或非空值（False）
search：基于全文索引的全文检索
regex / iregex：基于正则表达式的模糊匹配查询
aggregate() / annotate()
Avg / Count / Sum / Max / Min
first() / last()
说明：调用first()方法相当于用[0]对QuerySet进行切片。
only() / defer()
create() / update() / raw()


Q对象和F对象
说明：Q对象主要用来解决多条件组合的复杂查询；F对象主要用于更新数据。

	>>> from django.db.models import Q
	>>> Emp.objects.filter(
	...     Q(name__startswith='张'),
	...     Q(sal__lte=5000) | Q(comm__gte=1000)
	... ) # 查询名字以“张”开头且工资小于等于5000或补贴大于等于1000的员工
	<QuerySet [<Emp: 张三丰>]>


	>>> from backend.models import Emp, Dept
	>>> emps = Emp.objects.filter(dept__no=20)
	>>> from django.db.models import F
	>>> emps.update(sal=F('sal') + 100)