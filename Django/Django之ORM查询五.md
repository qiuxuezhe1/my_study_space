| 函数              | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| all()             | 查询所有结果                                                 |
| filter(**kwargs)  | 它包含了与所给筛选条件相匹配的对象                           |
| get(**kwargs)     | 返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误 |
| exclude(**kwargs) | 它包含了与所给筛选条件不匹配的对象                           |
| order_by(*field)  | 对查询结果排序                                               |
| distinct()        | 从返回结果中剔除重复纪录                                     |
| count()           | 返回数据库中匹配查询(QuerySet)的对象数量                     |
| first()           | 返回第一条记录                                               |
| last()            | 返回最后一条记录                                             |
| exists()          | 如果QuerySet包含数据，就返回True，否则返回False              |
| annotate()        | 使用聚合函数                                                 |
| dates()           | 根据日期获取查询集                                           |
| datetimes()       | 根据时间获取查询集                                           |

以上查询方法的基本用法为：

Article.objects.函数名()

#### 1. filter常用查询

```python
# 大于，>，对应SQL：select * from Article where id > 724
Article.objects.filter(id__gt=724)
# 大于等于，>=，对应SQL：select * from Article where id >= 724
Article.objects.filter(id__gte=724)
# 小于，<，对应SQL：select * from Article where id < 724
Article.objects.filter(id__lt=724)
# 小于等于，<=，对应SQL：select * from Article where id <= 724
Article.objects.filter(id__lte=724)
# 同时大于和小于， 1 < id < 10，对应SQL：select * from Article where id > 1 and id < 10
Article.objects.filter(id__gt=1, id__lt=10)
# 包含，in，对应SQL：select * from Article where id in (11,22,33)
Article.objects.filter(id__in=[11, 22, 33])
# 不包含，not in，对应SQL：select * from Article where id not in (11,22,33)
Article.objects.filter(pub_date__isnull=True)
# 不为空：isnull=False，对应SQL：select * from Article where pub_date is not null
Article.objects.filter(pub_date__isnull=True)
# 匹配，like，大小写敏感，对应SQL：select * from Article where name like '%sre%'，SQL中大小写不敏感
Article.objects.filter(name__contains="sre")
# 匹配，like，大小写不敏感，对应SQL：select * from Article where name like '%sre%'，SQL中大小写不敏感
Article.objects.filter(name__icontains="sre")
# 范围，between and，对应SQL：select * from Article where id between 3 and 8
Article.objects.filter(id__range=[3, 8])
# 以什么开头，大小写敏感，对应SQL：select * from Article where name like 'sh%'，SQL中大小写不敏感
Article.objects.filter(name__startswith='sre')
# 以什么开头，大小写不敏感，对应SQL：select * from Article where name like 'sh%'，SQL中大小写不敏感
Article.objects.filter(name__istartswith='sre')
# 以什么结尾，大小写敏感，对应SQL：select * from Article where name like '%sre'，SQL中大小写不敏感
Article.objects.filter(name__endswith='sre')
# 以什么结尾，大小写不敏感，对应SQL：select * from Article where name like '%sre'，SQL中大小写不敏感
Article.objects.filter(name__iendswith='sre')
# 排序，order by，正序，对应SQL：select * from Article where name = '关键词' order by id
Article.objects.filter(name='关键词').order_by('id')
# 多级排序，order by，先按name进行正序排列，如果name一致则再按照id倒叙排列
Article.objects.filter(name='关键词').order_by('name','-id')
# 排序，order by，倒序，对应SQL：select * from Article where name = '关键词' order by id desc
Article.objects.filter(name='关键词').order_by('-id')
```

#### 2. order_by

```python
article = models.Article.objects.filter(created_time__year=2018).order_by('-created_time', 'title')
```

上面的结果将按照created_time降序排序，然后再按照title升序排序。"-created_time"前面的负号表示降序顺序。 升序是默认的。

```python
article = models.Article.objects.order_by('category__name', 'title')
```

上面结果按关联模型的name属性进行升序，再按title升序

#### 3. Q和F对象

使用Q对象进行复杂查询

```python
Q(question__startswith='Who') | ~Q(pub_date__year=2005)
```

使用F获取当前对象指定属性的值，可以进一步进行运算等

```python
F('price') + 10
```

#### 4. 删除对象

可删除一个对象或一个查询集中的所有对象

```python
Article.objects.filter(id=1).delete()
Article.objects.all().delete()
```

#### 5. 更新对象

可更新一个对象或一个查询集中的所有对象

```python
Article.objects.filter(id=1).update(name='更新名称')
Article.objects.all().update(info='xxxxxx')
```

