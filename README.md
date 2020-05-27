# 声明

作者不属于任何公司、集体。

本项目使用GNU通用公共许可证，基于原木兰语言的逆向工程。使用的所有参考信息均从网络公开资料中合法获得。具体代码与原木兰语言的实现无直接关系。

### 运行

安装此包后, 可启动交互环境如下:
```
$ 木兰
木兰向您问好
更多信息请说'你好'
> func 过(年) {
>> println(年 + 1)
>> }
> 过(2019)
2020
```

错误反馈信息示例:
```
> func f() { f() }
> f()
递归过深。请确认: 1、的确需要递归 2、递归的收敛正确
> 1/0
请勿除以零
> print(某量)
请先定义'某量'再使用
```

相比使用交互平台，建议通过命令行下`木兰 {源码文件名}`运行代码。推荐使用[VS Code 插件](https://marketplace.visualstudio.com/items?itemName=CodeInChinese.ulang)对源码文件进行编辑。

![快排](https://raw.githubusercontent.com/MulanRevive/mulan/dev/%E6%88%AA%E5%9B%BE/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F.png)

### 大事记

#### 0.0.7

通过基于原 exe 的[用户手册](https://github.com/MulanRevive/bounty/tree/master/%E5%A4%8D%E7%8E%B0%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C)编写过程中积累的[测试用例](https://github.com/MulanRevive/bounty/blob/master/%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81/%E6%B5%8B%E8%AF%95.py), 与原型搭建过程中积累至今的[测试](https://github.com/MulanRevive/prototype/blob/master/%E6%B5%8B%E8%AF%95.py)

最近进展详见[《木兰编程语言》知乎专栏](https://zhuanlan.zhihu.com/ulang)。

#### 0.0.6

- [木兰编程语言基本功能摸索 (一)](https://zhuanlan.zhihu.com/p/103916529)
- [为「木兰」编程语言添加对中文命名标识符的支持](https://zhuanlan.zhihu.com/p/103910116)
- [「MulanRevive」编程语言项目启动](https://zhuanlan.zhihu.com/p/103895446)
