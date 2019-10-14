**Retry**

　　重试Retry表示流中的一个基本重试单元，它是一个特殊的单元，用来处理流中发生的失败，它可以控制流的执行，例如使用其它参数重试其它的atom。当一个atom发生失败是，重试单元会决定采用哪种策略进行重试。策略的类型包括：使用其它参数重试、恢复单个atom和恢复所有的atom。



**类Retry**

　　类Retry代表任务retry，是从类Atom派生出来的，也是一个抽象类，无法直接实例化。通常，开发者需要从类Retry派生出新类，并实现on_failure()方法和execute()方法。on_failure()方法觉得如何处理失败。on_failure()方法可以返回一个Decsion的实例。execute()方法通常定义为空方法。
　　下面是对类Decsion的介绍：
　　　　Decision派生于taskflow.utils.misc.StrEnum。用来表示决定结果或策略的枚举。它包含三个值：
　　　　　　**REVERT**：恢复所在或所关联的子流。这种策略会先检查父atom，判断其是否有相容的策略，以允许安全的进行流嵌套。如果父流没有重试策略，默认会恢复其所在的子流。engine的选项defer_reverts用来设置相对与父流的行为。如果其设置为True，则意味着会服从父流的重试策略。如果父流没有重试策略，那么默认会恢复其所在的子流。
　　　　　　**REVERT_ALL**：忽略父流的重试策略，总是恢复整个流。这种策略会恢复所有已经执行过的atom。
　　　　　　**RETRY**：再次重试所在的子流。



**Retry派生类**

　　为了方便开发者使用，TaskFlow提供了多个Retry派生类。有了这些派生类，开发就无需自己从类Retry派生出新类，简单使用这些已有的派生类即可。下面是这些派生类的简单介绍：
　　　　
　　　　**AlwaysRevert**: 当失败发生时，总是重试子流
　　　　**AlwaysRevertAll**: 当失败发生时，总是重试整个流
　　　　**Times**: 当失败发生时，重试给定的次数
　　　　**ForEach**: 当失败发生时，使用不同的输入来重试
　　　　**ParameterizedForEach**: 与ForEach类似，不同的是从存储层获取输入的值
　　　　
　　下面是一个使用AlwaysRevert的简单例子：

```python
from taskflow import task, engines, retry, task
from taskflow.patterns import linear_flow
class MyTask(task.Task):  
    def execute(self, arg1):    
        print('execute() = %s arg1=%r.' % (self.name, arg1))    
        if self.name == 'task-3':      
            raise Exception('Occur Error!')    
        return True  
    def revert(self, arg1, result, flow_failures):    
        print('revert() name =%s arg1=%r' % (self.name, arg1))    
        if result:      
            print('Undo the side-effect.')
            f = linear_flow.Flow('top-flow').add(MyTask('task-a'),linear_flow.Flow('sub-flow',retry=retry.AlwaysRevert()).add(MyTask('task-1'),MyTask('task-2'),MyTask('task-3'),MyTask('task-4')),MyTask('task-b'))

engines.run(f, store={'arg1': 100})
```



　　程序输出：

```python
execute() = task-a arg1=100.
execute() = task-1 arg1=100.
execute() = task-2 arg1=100.
execute() = task-3 arg1=100.
revert() name =task-3 arg1=100
Undo the side-effect.
revert() name =task-2 arg1=100
Undo the side-effect.
revert() name =task-1 arg1=100
Undo the side-effect.
Traceback (most recent call last):
...
Exception: Occur Error!
```


　　下面是一个使用AlwaysRevertAll的简单例子：

```python
from taskflow import task, engines, retry, task
from taskflow.patterns import linear_flow
class MyTask(task.Task):  
    def execute(self, arg1):    
        print('execute() = %s arg1=%r.' % (self.name, arg1))    
        if self.name == 'task-3':      
            raise Exception('Occur Error!')    
        return True  
    def revert(self, arg1, result, flow_failures):    
        print('revert() name =%s arg1=%r' % (self.name, arg1))    
        if result:      
            print('Undo the side-effect.')


f = linear_flow.Flow('top-flow').add(MyTask('task-a'),linear_flow.Flow('sub-flow',retry=retry.AlwaysRevertAll()).add(MyTask('task-1'),MyTask('task-2'),MyTask('task-3'),MyTask('task-4')),MyTask('task-b'))
engines.run(f, store={'arg1': 100})
```



　　程序输出：

```python
execute() = task-a arg1=100.
execute() = task-1 arg1=100.
execute() = task-2 arg1=100.
execute() = task-3 arg1=100.
revert() name =task-3 arg1=100
Undo the side-effect.
revert() name =task-2 arg1=100
Undo the side-effect.
revert() name =task-1 arg1=100
Undo the side-effect.
revert() name =task-a arg1=100
Undo the side-effect.
Traceback (most recent call last):
  ...  
    raise Exception('Occur Error!')
Exception: Occur Error!
```


　　下面是一个使用Times的简单例子：

```python
from taskflow import task, engines, retry, task
from taskflow.patterns import linear_flow
class MyTask(task.Task):  
    def execute(self, arg1):    
        print('execute() = %s arg1=%r.' % (self.name, arg1))    
        if self.name == 'task-repeat':      
            raise Exception('Occur Error!')    
        return True  
    def revert(self, arg1, result, flow_failures):    
        print('revert() name =%s arg1=%r' % (self.name, arg1))    
        if result:      
            print('Undo the side-effect.')

f = linear_flow.Flow('top-flow').add(MyTask('task-a'),linear_flow.Flow('sub-flow',retry=retry.Times(3)).add(MyTask('task-repeat')),MyTask('task-b'))

engines.run(f, store={'arg1': 100})
```


　　程序输出：

```python
execute() = task-a arg1=100.
execute() = task-repeat arg1=100.
revert() name =task-repeat arg1=100
Undo the side-effect.
execute() = task-repeat arg1=100.
revert() name =task-repeat arg1=100
Undo the side-effect.
execute() = task-repeat arg1=100.
revert() name =task-repeat arg1=100
Undo the side-effect.
Traceback (most recent call last):
  ...
Exception: Occur Error!
```


　　下面是一个使用ForEach的简单例子：

```python
from taskflow import task, engines, retry, task
from taskflow.patterns import linear_flow
class MyTask(task.Task):  
    def execute(self, arg1):    
        print('execute() = %s arg1=%r.' % (self.name, arg1))    
        if self.name == 'task-repeat' and arg1 in (101, 102):      
            raise Exception('Occur Error!')    
        return True  
    def revert(self, arg1, result, flow_failures):    
        print('revert() name =%s arg1=%r' % (self.name, arg1))    
        if result:      
            print('Undo the side-effect.')
  
 
args = [101, 102, 103, 104, 105]
f = linear_flow.Flow('top-flow').add(linear_flow.Flow('sub-flow',retry=retry.ForEach(args, provides='arg1')).add(MyTask('task-repeat')),                   MyTask('task-b'))

engines.run(f)
```


　　程序输出：

```python
execute() = task-repeat arg1=101.
revert() name =task-repeat arg1=101
Undo the side-effect.
execute() = task-repeat arg1=102.
revert() name =task-repeat arg1=102
Undo the side-effect.
execute() = task-repeat arg1=103.
execute() = task-b arg1=103.
```


　　下面是一个使用ParameterizedForEach的简单例子：

```python
from taskflow import task, engines, retry, task
from taskflow.patterns import linear_flow
class MyTask(task.Task):  
    def execute(self, arg1):    
        print('execute() = %s arg1=%r.' % (self.name, arg1))    
        if self.name == 'task-repeat' and arg1 in (101, 102):      
            raise Exception('Occur Error!')    
        return True  
    def revert(self, arg1, result, flow_failures):    
        print('revert() name =%s arg1=%r' % (self.name, arg1))    
        if result:      
            print('Undo the side-effect.')
        
       
f = linear_flow.Flow('top-flow').add(linear_flow.Flow('sub-flow',retry=retry.ParameterizedForEach(rebind= {'values':'args'}, provides='arg1')).add(MyTask('task-repeat')),MyTask('task-b'))

args = [101, 102, 103, 104, 105]
engines.run(f, store={'args': args})
```

　　程序输出：

```python
execute() = task-repeat arg1=101.
revert() name =task-repeat arg1=101
Undo the side-effect.
execute() = task-repeat arg1=102.
revert() name =task-repeat arg1=102
Undo the side-effect.
execute() = task-repeat arg1=103.
execute() = task-b arg1=103.
```



**类Retry的继承关系**


　　类Retry继承于类Atom。

![image-20191014214207256](./images/atom.png)