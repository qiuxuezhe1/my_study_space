其实在这之前，我也像很多人一样不知道cask是什么，但当我困扰于sequel pro这个mac上极具活跃的数据库管理工具的安装和使用方式而困惑时，遇见了cask这个堪称神级的工具。既往下来讲解homebrew和cask。

Homebrew 是一款开源的软件包管理系统，用以简化 macOS 上的软件安装过程，可以类比于 Windows 上软件管家的一键安装。Homebrew 在 2009 年由马克斯·霍威尔（Max Howell）写成，它在 GitHub 上拥有大量贡献者，目前仍处于活跃状态。

Homebrew Cask 是 Homebrew 的扩展，借助它可以方便地在 macOS 上安装图形界面程序，即我们常用的各类应用。Homebrew 中文含义为自制、自酿酒，Cask 中文含义为桶、木桶，桶装酒是一种成品，也就是说每一个 `homebrew cask` 都可以直接使用的，比如安装的 Cask 名称为 sequel pro，那么就可以使用如下命令安装：

```shell
brew cask install sequel-pro
```

安装成功之后，sequel pro会出现在你的application里面，是不是感觉比以前使用



homebrew目前的mac电脑应该都默认安装了，反正我不记得我手动安装过homebrew，知识升级过。

接下来使用homebrew安装cask

```shell
brew tap caskroom/cask
```

注意，请完整执行以上语句，我第一次也都以为是可选，结果必须写完整

## 如何使用 Homebrew Cask

```
brew cask install 应用名称
brew cask install <甲应用名称> <乙应用名称> <丙应用名称>
```

前文已经讲过这个安装命令，但一个问题是：如何确认它支持所要安装的应用？

```
brew cask search 关键字
```

比如要确定是否支持应用 gooooooogle，可搜索关键字 goo，即可显示所有包含 goo 的应用。如果不加关键字，会显示出所有支持的应用名称。



由于 Homebrew Cask 还不支持更新应用，故建议使用应用自带的方式进行更新。欲要查看其他命令，可在终端执行 `brew cask help` 以显示所有 commands，比如发现查看应用 Cask 信息的命令是 `info`，则在终端执行 `brew cask info 应用名称` 即可显示该应用信息。



## Homebrew Cask 原理

之前，是用软链接的方式将应用链接到 Application 文件夹，有人说这样的方式会导致 Spotlight 无法检索到。但现在，它是将应用直接移动到 Application 文件夹，这与我们自己去ß官网下载应用再安装是完全一致的，后续更新或卸载也按平常的方式即可。

当然，也可以用 `brew cask uninstall 应用名称` 的方式，这种方式才会删除路径 `/usr/local/Caskroom` 中保留的应用信息文件，这样当我们用命令 `brew cask list` 查询已安装列表时，已卸载的应用才不会仍显示。也就是说，如果按照平常的方式，比如直接移到废纸篓，那么还需手动删除 Caskroom 中的应用信息文件。当然，不删除也没啥影响，因为一般没必要查看已安装列表，已安装应用在 Launchpad 中查看就好。

## 总结

我们可以查阅 [官方使用说明](https://link.jianshu.com?t=https%3A%2F%2Fgithub.com%2Fcaskroom%2Fhomebrew-cask%2Fblob%2Fmaster%2FUSAGE.md) 以了解 Homebrew Cask 命令别名、高级搜索语法等用法。通过这种方式安装应用，与我们平时的方式安装应用，两者除了方式没有任何其他区别，那为何不尝试尝试这种轻松的方式呢？只一句命令，没有那些点击，没有那些拖动…… Homebrew Cask 让非 Mac App Store 应用的安装更轻松，若你也想以更轻松的方式安装和更新 Mac App Store 应用，请参阅 [终端上的 Mac App Store「mas」让应用的安装与更新无比轻松](https://link.jianshu.com?t=https%3A%2F%2Fsspai.com%2Fpost%2F40382)。

本文摘抄于：唐小筑链接：https://www.jianshu.com/p/5f7c188b7ad1ßß