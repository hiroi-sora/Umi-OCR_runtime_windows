<p align="center">
  <a href="https://github.com/hiroi-sora/Umi-OCR">
    <img width="200" height="128" src="https://tupian.li/images/2022/10/27/icon---256.png" alt="Umi-OCR">
  </a>
</p>

<p align="left">
    平台：
    <span>
        <b>Windows</b>
    </span>
    <span> • </span>
    <span>
    <a href="https://github.com/hiroi-sora/Umi-OCR_runtime_linux">
        Linux
    </a>
    </span>
</p>

<h1 align="center">Umi-OCR windows 运行环境</h1>

本仓库为 [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) 的代码 提供Windows运行环境。

开发者你好，探索和参与 Umi-OCR 项目。下文将会指导你搭建起适用于Windows的开发环境。

### 系统支持

最低支持 win7 64位。

### 运行环境组成

运行环境分为三部分。将这三部分放置于 Umi-OCR v2 项目源代码中，就可以跑起来。

1. 启动器exe
2. python解释器 `runtime` (3.8.10)
3. python第三方库 `site-packages`

## 开始搭建windows开发环境

搭建windows开发环境分为四步：下载主仓库代码、放置运行环境、放置插件、搭建开发环境。

## 0. 下载主要代码

fork / clone [主仓库](https://github.com/hiroi-sora/Umi-OCR) 。

## 1. 放置运行环境

<!-- 1. 从 [本仓库Release](https://github.com/hiroi-sora/Umi-OCR_runtime_windows/releases) 下载压缩包。 -->
1. 下载本仓库的所有内容。建议直接下载 [Github自动打包的zip压缩包](https://github.com/hiroi-sora/Umi-OCR_runtime_windows/archive/refs/heads/main.zip) 。
2. 解压压缩包，将所有内容拷贝到 Umi-OCR 项目路径下。

（环境仓库的目录结构，与主仓库的项目结构是一一对应的。理论上直接拷贝，可以直接将文件放置到合适的位置。）

## 2. 放置插件

在 [插件仓库](https://github.com/hiroi-sora/Umi-OCR_plugins) 下载需要的插件，根据提示放置在指定目录下。

## 3. 搭建开发环境

### 3.1. 工欲善其事，必先利其器

- 系统要求：建议 Win10/11 。Win7也成。
- 编辑器：建议 [VS Code](https://code.visualstudio.com/)
  - Tips：VS Code最后一个支持Win7的版本：[v1.70](https://code.visualstudio.com/updates/v1_70)
- VS Code 插件推荐：
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) （Python规范格式化）
  - [QML](https://marketplace.visualstudio.com/items?itemName=bbenoist.QML) （提供qml语法高亮）
  - [QML Snippets](https://marketplace.visualstudio.com/items?itemName=ThomasVogelpohl.vsc-qml-snippets) （提供qml代码补全）

与常见的Python项目不同，本项目内嵌了所有PY运行环境及第三方库文件。故你不需要额外安装Python和QT等东西，也不需要pip安装任何包。只需一个趁手的编辑器即可。

如果你不喜欢 VS Code ，也可以用任何编辑器——甚至记事本来开发本项目。

### 3.2. 部署开发环境

1. 回到主项目根目录，点击 `Umi-OCR.exe` 测试运行项目。不出意外的话，能正常打开软件界面。
2. `.vscode` 目录是编辑器配置文件目录，已经填写好了必要的环境参数。用 VS Code 打开其中的工作区文件 `Umi-OCR_v2.code-workspace` 。
3. 在 VS Code 内随便打开一个python文件，如 `UmiOCR-data/py_src/run.py` 。不出意外的话，能够显示代码高亮。
4. 尝试点击 F5 调试程序。如果已经能跑起来了，则项目开发环境已经搭建成功。
5. 如果 VS Code 报错 `The Python path in your debug configuration is invalid.` ，则重新指定一下PY解释器路径。按快捷键 `Ctrl+Shift+P` ，然后输入 `Python:Select Interpreter` 。点第一个，然后 `+ Enter inter preter path...` 。
6. 在弹出的文件选择弹窗中，选择 `项目目录/UmiOCR-data/runtime/python.exe` 。
7. 再度点击 F5 调试程序，此时应该肯定能跑起来了。
8. Vs Code 的断点调试等开发工具应该也能正常使用。（注：只能对python代码进行断点调试，qml代码不行。只能用`console`大法来调试qml。）

注意，如果你本地已经安装过python，则建议**不要用本地环境**运行本项目。请使用本项目**内置的py环境**。

### 4. 一键打包脚本 `release.py`

完成开发工作后，可以使用一键打包脚本。功能包括：
- 提取程序文件
- 生成7z或zip压缩包
- 生成自解压exe可执行程序

#### 使用方法：

本地已安装Python：
```
python release.py
```

本地未安装Python：
```
UmiOCR-data/runtime/python.exe release.py
```

一般情况下，无需设定任何参数，一键运行即可。

可定制参数（均非必填）：
```
--to_7z      是否生成压缩包，默认1
--to_sfx     是否生成自解压文件，默认1
--path       发布包存放路径，默认为 /release
--version    版本文件 version.py 的路径
--run        启动器路径，默认为 Umi-OCR.exe
--datas      内容目录文件选取，格式：文件1,文件2,文件3……
--plugins    插件选取，格式：打包名1,插件1,插件2|打包名2,插件2,插件3……
--path_7z    7z 命令行工具的路径，打压缩包要用，默认 dev-tools/7z/7zr.exe
--path_sfx   sfx 自解压工具的路径，创建自解压文件要用，默认 dev-tools/7z/7z.sfx
--args_7z    7z 参数，可指定压缩包类型和压缩率等。如-t7z等指定压缩类型参数必须放在最后
```
可通过 `release.py --help` 查看最新参数，或浏览 `release.py` 源码的注释。

---

## 关于第三方包

如果你正在对 Umi-OCR 进行二次开发，并希望载入第三方python包，请参照以下步骤。

1. 下载

由于这个运行环境基于嵌入式python解释器，所以不支持pip安装。请在你的电脑上安装另外的完整python环境，然后使用下列命令下载适用于本环境的包：

```
pip download --only-binary=:all: --platform win_amd64 [包名]
```
或
```
pip download --only-binary=:all: --platform win_amd64 --python-version 38 [包名]
```

例如，我想下载 `PySide2` 库，则使用命令：
```
pip download --only-binary=:all: --platform win_amd64 PySide2
```

当然，如果你本地安装的python版本也是3.8.10 x64，那么可以尝试直接pip安装到本地python环境（或虚拟环境），然后将安装好的包文件拷贝出来用。

2. 安装

将下载的whl包解压，然后塞到 `UmiOCR-data/site-packages` 目录下即可。

有部分包直接放置不能运行，请根据报错信息见机行事。常见的原因有：
- import层级错误。将包内代码修改为相对导入。
- python版本或系统平台错误。请确保此包兼容win 64位、python 3.8 。
大部分包在调整之后可以正常运行，与pip安装无异。

如果某些包有大量依赖、难以安装，如某些大型机器学习库。那么你要思考，将这几百MB塞进项目，会不会影响Umi-OCR的轻便易用性。也许更应该以 [插件](https://github.com/hiroi-sora/Umi-OCR_plugins) 的形式提供这些功能。

3. 删减

第三方包含有大量无需使用的功能和dll文件。完全可以删减这些文件以节省空间。

4. 贡献

如果你为Umi-OCR主仓库贡献了代码，且这些代码必须引入一个新的第三方包，请：
- 确保该包已经删减到最小
- fork本仓库
- 将文件放置于 `site-packages` 中
- push到本仓库

# Umi-OCR 项目结构

### 各仓库：

- [主仓库](https://github.com/hiroi-sora/Umi-OCR)
- [插件库](https://github.com/hiroi-sora/Umi-OCR_plugins)
- [Win 运行库](https://github.com/hiroi-sora/Umi-OCR_runtime_windows) 👈

### 工程结构：

`**` 后缀表示本仓库(`Windows 运行库`)包含的内容。

```
Umi-OCR
├─ Umi-OCR.exe **
└─ UmiOCR-data
   ├─ main.py
   ├─ version.py
   ├─ site-packages **
   │  └─ python包
   ├─ runtime **
   │  └─ python解释器
   ├─ qt_res
   │  └─ 项目qt资源，包括图标和qml源码
   ├─ py_src
   │  └─ 项目python源码
   ├─ plugins
   │  └─ 插件
   └─ i18n
      └─ 翻译文件
```

