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

### 运行环境食用方法

#### 从Release（推荐）

1. 从本仓库Release下载压缩包
2. 解压压缩包，将其中的内容拷贝到 Umi-OCR v2 项目路径下。

（压缩包的目录结构，与 Umi-OCR 的项目结构是一一对应的，理论上直接拷贝，可以直接将文件放置到合适的位置。）

#### 从clone

1. clone本仓库
2. 将 `Umi-OCR.exe` 放置到Umi-OCR项目目录。
3. 将 `UmiOCR-data/runtime.zip` 解压，并放置于Umi-OCR项目相同位置。
4. 将 `UmiOCR-data/site-packages` 中的所有 `zip` 解压，并将整个 `site-packages` 放置于Umi-OCR项目相同位置。

### 开发指南：关于第三方包

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