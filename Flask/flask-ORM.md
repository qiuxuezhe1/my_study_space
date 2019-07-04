```python
order_by排序
# 升序order_by(Student.id)
# 降序order_by(-Student.id)
stus = Student.query.order_by(-Student.id).all()

# offset、limit
# offset偏移：跳过几个元素
# limit: 截图几个元素
# django中Paginator()用于分页
page = 3
stus = Student.query.offset((page - 1)*2).limit(2).all()

# 是否有上一页: flask中has_prev  django中has_previous
# 是否有下一页: flask中has_next  django中has_next
# 下一页角码: flask中next_num    django中next_page_number
# 上一页角码: flask中prev_num    django中previous_page_number

# 模糊查询，icontains，and_、not_、or_，startswith， endswith， like
# contains  like '%三%'
stus = Student.query.filter(Student.s_name.contains('三')).all()
stus = Student.query.filter(Student.s_name.like('%三%')).all()
print(stus)
# startswith like '三%'
stus = Student.query.filter(Student.s_name.startswith('三')).all()
stus = Student.query.filter(Student.s_name.like('三%')).all()
print(stus)
# endswith like '%三'
stus = Student.query.filter(Student.s_name.endswith('三')).all()
stus = Student.query.filter(Student.s_name.like('%三')).all()
print(stus)

# like % _
stus = Student.query.filter(Student.s_name.like('_三')).all()
print(stus)

# 与或非，django: 且
# filter(条件1，条件2，条件3) filter(Q(条件1)，Q(条件2)，Q(条件3))
# django ：或
# filter(Q(条件1) | Q(条件2) | Q(条件3))
# django ：非
# filter(~Q(条件1)，Q(条件2)，Q(条件3))

# 与或非，flask，and_，or_，not_
# 且操作， and_
stu = Student.query.filter(Student.s_name.like('%三%'))\
    .filter(Student.s_age == 20).all()

stu = Student.query.filter(Student.s_name.like('%三%'),
                           Student.s_age == 20).all()

stu = Student.query.filter(and_(Student.s_name.like('%三%'),
                           Student.s_age == 20)).all()
# 或操作，or_
stus = Student.query.filter(or_(Student.s_name.like('%三%'),
                           Student.s_age == 20)).all()
# 非操作，not_
stus = Student.query.filter(not_(Student.s_name.like('%三%')),
                            Student.s_age == 20).all()

print(stus)

# django中: gt gte lt lte
# flask中: gt ge lt le > >= < <= ==
stus = Student.query.filter(Student.s_age.__gt__(20)).all()
stus = Student.query.filter(Student.s_age >= 20).all()
print(stus)

# in_  notin_
stus = Student.query.filter(Student.id.in_([1, 2, 3])).all()
stus = Student.query.filter(Student.id.notin_([1, 2, 3])).all()


# 创建一个学生对象信息
# 创建学生信息
# student = Student()
# student.s_name = 'admin'
# # add()方法只是在准备向数据库中插入数据
# db.session.add(student)
# # commit()事务提交，将数据插入到数据库中
# db.session.commit()

# 创建多个学生对象信息
names = ['张三', 'coco', 'vincent', '李四']
stus = []
for name in names:
    student = Student()
    student.s_name = name
    stus.append(student)
db.session.add_all(stus)
db.session.commit()

# delete()删除，接收删除的对象
db.session.delete(stu)	


# 多对多中间表添加数据
# 向中间表加信息
cou1 = Course.query.filter(Course.c_name == 'VHDL').first()
cou2 = Course.query.filter(Course.c_name == 'JAVA').first()
stus = Student.query.filter(Student.id.in_([1,2])).all()
# 获取课程所关联的学生信息
# print(cou1.stus)
# for stu in stus:
#     cou1.stus.append(stu)
# print(cou1.stus)
# 向中间表加数据，append，向中间表删除数据，remove
for stu in stus:
    # stu.c.append(cou2)
    stu.c.remove(cou2)
db.session.commit()
```