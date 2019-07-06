## Linux的nohup和&用法和区别

在应用Unix/Linux时，我们一般想让某个程序在后台运行，于是我们将常会用 **&** 在程序结尾来让程序自动运行。

比如我们要运行mysql在后台： /usr/local/mysql/bin/mysqld_safe –user=mysql &

可是有很多程序并不像mysqld一样，这样我们就需要nohup命令，怎样使用nohup命令呢？这里讲解nohup命令的一些用法。

nohup ./start.sh &

&的意思是在后台运行， 什么意思呢？ 意思是说， 当你在执行 ./start.sh & 的时候， 即使你用ctrl C, 那么start.sh照样运行（因为对SIGINT信号免疫）。 但是要注意， 如果你直接关掉shell后， 那么，start.sh进程同样消失。 可见， &的后台并不硬（因为对SIGHUP信号不免疫）。(对SIG类信号不了解的，可戳[lGET]()进行了解)

nohup的意思是忽略SIGHUP信号， 所以当运行nohup ./start.sh的时候， 关闭shell, 那么start.sh进程还是存在的（对SIGHUP信号免疫）。 但是， 要注意， 如果你直接在shell中用Ctrl C, 那么start.sh进程也是会消失的（因为对SIGINT信号不免疫）

所以， &和nohup没有半毛钱的关系， 要让进程真正不受shell中Ctrl C和shell关闭的影响， 那该怎么办呢？ 那就用nohup ./start.sh &吧， 两全其美。

如果你懂守护进程， 那么nohup ./start.sh &有点让start.sh成为守护进程的感觉。

nohup

不挂断地运行命令。no hangup的缩写，意即“不挂断”。一般理解&记住一个命令最简单的方法是记住它是什么缩写，就自然理解了这个命令。 nohup运行由 Command参数和任何相关的 Arg参数指定的命令，忽略所有挂断（SIGHUP）信号；

语法

nohup Command [ Arg ... ] [　& ]

nohup 命令运行由 Command参数和任何相关的 Arg参数指定的命令，忽略所有挂断（SIGHUP）信号。在注销后使用 nohup 命令运行后台中的程序。要运行后台中的 nohup 命令，添加 & （ 表示“and”的符号）到命令的尾部。 如果不将 nohup 命令的输出重定向，输出将附加到当前目录的 nohup.out 文件中。如果当前目录的 nohup.out 文件不可写，输出重定向到 $HOME/nohup.out 文件中。



nohup和&的区别

&是指在后台运行

运行 nohup --help Run COMMAND, ignoring hangup signals. 可以看到是“运行命令，忽略挂起信号”就是不挂断的运行，注意没有后台运行功能。

就是指，用nohup运行命令可以使命令永久的执行下去，和用户终端没有关系，例如我们断开SSH连接都不会影响他的运行，注意了nohup没有后台运行的意思；&才是后台运行

**&是指在后台运行，但当用户退出(挂起)的时候，命令自动也跟着退出**

那么，我们可以巧妙的吧他们结合起来用就是

nohup COMMAND &

这样就能使命令永久的在后台执行 例如：

sh test.sh & 将sh test.sh任务放到后台 ，即使关闭xshell退出当前session依然继续运行，但标准输出和标准错误信息会丢失

nohup sh test.sh 将sh test.sh任务放到后台，关闭标准输入，前台不再能够接收任何输入（标准输入），重定向标准输出和标准错误到当前目录下的nohup.out文件，即使关闭xshell退出当前session依然继续运行。

nohup sh test.sh & 将sh test.sh任务放到后台，但是依然可以使用标准输入，前台能够接收任何输入，重定向标准输出和标准错误到当前目录下的nohup.out文件，即使关闭xshell退出当前session依然继续运行。


资源转载于[insmoin](https://www.jianshu.com/p/93a45927f013)