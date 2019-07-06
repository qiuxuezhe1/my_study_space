scp是什么？scp有什么用？

scp是secure copy的简写，用于在Linux下进行远程拷贝文件的命令，和它类似的命令有cp，不过cp只是在本机进行拷贝不能跨服务器，而且scp传输是加密的。

### 1、我们需要获得远程服务器上的某个文件，远程服务器既没有配置ftp服务器，没有开启web服务器，也没有做共享，无法通过常规途径获得文件时，只需要通过scp命令便可轻松的达到目的。

### 2、我们需要将本机上的文件上传到远程服务器上，远程服务器没有开启ftp服务器或共享，无法通过常规途径上传是，只需要通过scp命令便可以轻松的达到目的。

scp使用方法
#### 1.获取远程服务器上的文件

root@192.168.191.32 表示使用root用户登录远程服务器192.168.191.32，

/home/favicon.ico 表示远程服务器上的文件,

/Users/xiao/Documents/favicon.ico 表示保存在本地上的路径和文件名。

#### 2.获取远程服务器上的目录

```html
scp -P 2222 -r root@192.168.191.32:/home/ /Users/xiao/Documents/
```

-r :参数表示递归复制（即复制该目录下面的文件和目录)

root@192.168.191.32 表示使用root用户登录远程服务器192.168.191.32，

/home/ 表示远程服务器上的目录，

/Users/xiao/Documents/ 表示保存在本地上的目录路径。

#### 3.将本地文件上传到服务器上

```html
scp -P 2222 /Users/xiao/Documents/favicon.ico root@192.168.191.32:/home/favicon.ico
```

/Users/xiao/Documents/favicon.ico 表示保存在本地上的路径和文件名。

root@192.168.191.32 表示使用root用户登录远程服务器192.168.191.32，

/home/favicon.ico 表示远程服务器上的文件,

#### 4.将本地目录上传到服务器上

```html
scp -P 2222 -r /Users/xiao/Documents/ root@192.168.191.32:/home/
```

-r :参数表示递归复制（即复制该目录下面的文件和目录)

root@192.168.191.32 表示使用root用户登录远程服务器192.168.191.32，

/home/ 表示远程服务器上的目录，

/Users/xiao/Documents/ 表示保存在本地上的目录路径。

#### 5.可能有用的几个参数 :

-4 : 强行使用 IPV4 地址 .

-6 : 强行使用 IPV6 地址 .

[资源原地址](https://blog.csdn.net/qinyikl/article/details/78598280)