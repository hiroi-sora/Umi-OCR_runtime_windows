# Umi-OCR windows 运行环境

为 [Umi-OCR_v2](https://github.com/hiroi-sora/Umi-OCR_v2) 的代码 提供Windows运行环境。

### 系统支持

理论上最低支持 win7 32位。

（32位系统未做测试，且没有支持的离线OCR组件。64位有完整支持。）

### 运行环境组成

运行环境分为三部分。将这三部分放置于 Umi-OCR v2 项目源代码中，就可以跑起来。

1. 启动器exe
2. python解释器 `runtime` (3.8.10, 32位)
3. python第三方库 `site-packages`

# Umi-OCR 搭建windows开发环境

开发者你好，探索和参与 Umi-OCR 项目。下文将会指导你搭建起适用于 Umi-OCR V2 的开发环境。

搭建windows开发环境分为三步：放置运行环境、放置插件、搭建开发环境。

## 1. 放置运行环境

clone [主仓库](https://github.com/hiroi-sora/Umi-OCR_v2) ，然后按下列方法导入运行环境

#### 从Release（推荐）

1. 从本仓库Release下载压缩包
2. 解压压缩包，将其中的内容拷贝到 Umi-OCR v2 项目路径下。

（压缩包的目录结构，与 Umi-OCR 的项目结构是一一对应的，理论上直接拷贝，可以直接将文件放置到合适的位置。）

#### 从clone

1. clone本仓库
2. 将 `Umi-OCR.exe` 放置到Umi-OCR项目目录。
3. 将 `UmiOCR-data/runtime.zip` 解压，并放置于Umi-OCR项目相同位置。
4. 将 `UmiOCR-data/site-packages` 中的所有 `zip` 解压，并将整个 `site-packages` 放置于Umi-OCR项目相同位置。

## 2. 放置插件

在 [插件仓库](https://github.com/hiroi-sora/Umi-OCR_plugins) 下载需要的插件，根据提示放置在Umi-OCR指定目录下。

## 3. 搭建开发环境

### 工欲善其事，必先利其器

- 系统要求：建议 Win10/11 。win7也成。
- 编辑器：建议 [VS Code](https://code.visualstudio.com/)
- VS Code 插件推荐：
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) （Python规范格式化）
  - [QML](https://marketplace.visualstudio.com/items?itemName=bbenoist.QML) （提供qml语法高亮）
  - [QML Snippets](https://marketplace.visualstudio.com/items?itemName=ThomasVogelpohl.vsc-qml-snippets) （提供qml代码补全）

本项目内嵌了所有前端运行环境及第三方库，故你不再需要安装Python和QT等开发环境；只需一个趁手的编辑器即可。

如果你不喜欢 VS Code ，也可以用任何编辑器——甚至记事本来开发本项目。

### 部署开发环境

1. 回到主项目根目录，点击 `Umi-OCR.exe` 测试运行项目。不出意外的话，能正常打开软件界面。
2. `.vscode` 目录是编辑器配置文件目录，已经填写好了必要的环境参数。用 VS Code 打开其中的工作区文件 `Umi-OCR_v2.code-workspace` 。
3. 在 VS Code 内随便打开一个python文件，如 `UmiOCR-data/pyapp/run.py` 。不出意外的话，能够显示代码高亮。
4. 尝试点击 F5 调试程序。如果已经能跑起来了，则项目开发环境已经搭建成功。
5. 如果 VS Code 报错 `The Python path in your debug configuration is invalid.` ，则重新指定一下PY解释器路径。按快捷键 `Ctrl+Shift+P` ，然后输入 `Python:Select Interpreter` 。点第一个，然后 `+ Enter inter preter path...` 。
6. 在弹出的文件选择弹窗中，选择 `项目目录/UmiOCR-data/.runtime/python.exe` 。
7. 再度点击 F5 调试程序，此时应该肯定能跑起来了。

注意，如果你本地已经安装过python，则建议不要用你的本地解释器运行本项目。请使用本项目内置的解释器。

---

## 关于第三方包

如果你正在对 Umi-OCR 进行二次开发，并希望载入第三方python包，请参照以下步骤。

1. 下载

由于这个运行环境基于嵌入式python解释器，所以不支持pip安装。请在你的电脑上安装另外的完整python环境，然后使用下列命令下载适用于本环境的包：

```
pip download --only-binary=:all: --platform win32 PySide2 [包名]
```
或
```
pip download --only-binary=:all: --python-version 38 --platform win32 [包名]
```

例如，我想下载 `PySide2` 库，则使用命令：
```
pip download --only-binary=:all: --platform win32 PySide2
```

2. 安装

将下载的whl包解压，然后塞到 `UmiOCR-data/site-packages` 目录下即可。

有部分包直接放置不能运行，请根据报错信息见机行事。常见的原因有：
- import层级错误。将包内代码修改为相对导入。
- python版本或系统平台错误。请确保此包兼容win 32位、python 3.8 。
大部分包在调整之后可以正常运行，于pip安装无异。

如果某些包有大量依赖、难以安装，如某些大型机器学习库。那么你要思考，将这几百MB塞进项目，会不会影响Umi-OCR的轻便易用性。也许更应该以 [插件](https://github.com/hiroi-sora/Umi-OCR_plugins) 的形式提供这些功能。

3. 删减

第三方包含有大量无需使用的功能和dll文件。完全可以删减这些文件以节省空间。

4. 贡献

如果你为Umi-OCR主仓库贡献了代码，且这些代码必须引入一个新的第三方包，请：
- 确保该包已经删减到最小
- 压缩为zip，放置于 `site-packages` 中
- push到本仓库