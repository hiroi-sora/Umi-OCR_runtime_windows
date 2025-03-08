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

### 运行环境说明

在设计上， Umi-OCR 采用业务代码与运行环境分离的结构。业务代码（即 [主仓库](https://github.com/hiroi-sora/Umi-OCR) ）兼容所有平台，但不能单独执行；必须和运行环境支持库（即 [Windows](https://github.com/hiroi-sora/Umi-OCR_runtime_windows)/[Linux](https://github.com/hiroi-sora/Umi-OCR_runtime_linux) 库）、OCR引擎插件（[Umi-OCR_plugins](https://github.com/hiroi-sora/Umi-OCR_plugins)）组合在一起，才能得到一个完整的 **可执行程序** 。

对于 Windows 系统，需要以下组件才能得到完整程序：

1. 业务代码，包括但不限于： `UmiOCR-data\py_src`、`UmiOCR-data\qt_res`
2. 启动器exe： `Umi-OCR.exe`
3. python解释器 (3.8.10)： `UmiOCR-data/runtime` 
4. python第三方库： `UmiOCR-data/site-packages`
5. OCR引擎插件，例如： `UmiOCR-data/plugins/win7_x64_RapidOCR-json`

请根据后续步骤，搭建起完整程序及开发环境。

## 搭建 Windows 运行环境

### 1. 命令行操作（推荐）

请确保安装了 Git 。创建一个工程目录，如 `Umi-OCR Project` 。在工程目录中启动 Git Bash ，执行以下指令。

```bash
# 当前位于一个空的工程目录下，如 Umi-OCR Project

# 克隆主仓库
git clone https://github.com/hiroi-sora/Umi-OCR.git

# 克隆Windows运行库仓库
git clone https://github.com/hiroi-sora/Umi-OCR_runtime_windows.git

# 创建临时目录
mkdir -p temp

# 下载运行库的额外二进制文件
curl -L -o temp/Umi-OCR_runtime_win7_x64.zip 'https://github.com/hiroi-sora/Umi-OCR_runtime_windows/releases/download/2.1.5/Umi-OCR_runtime_win7_x64.zip'
# 解压
unzip temp/Umi-OCR_runtime_win7_x64.zip -d temp/
# 额外文件复制到Windows运行库仓库，不覆盖已存在的文件
cp -rn temp/Umi-OCR_runtime_win7_x64/. Umi-OCR_runtime_windows/
# 运行库整体复制到主仓库下，不覆盖
cp -rn Umi-OCR_runtime_windows/. Umi-OCR

# 下载 RapidOCR-json 引擎插件。更多插件可见 https://github.com/hiroi-sora/Umi-OCR_plugins
curl -L -o temp/win7_x64_RapidOCR-json.7z https://github.com/hiroi-sora/Umi-OCR_plugins/releases/download/2.0.0/win7_x64_RapidOCR-json.7z
# 使用仓库自带的7zr，解压引擎插件。注意 -o后面没有空格
Umi-OCR/dev-tools/7z/7zr x temp/win7_x64_RapidOCR-json.7z -otemp/win7_x64_RapidOCR-json
# 在主仓库中创建插件目录 UmiOCR-data/plugins ，将插件复制到里面。
mkdir -p Umi-OCR/UmiOCR-data/plugins
cp -rn temp/win7_x64_RapidOCR-json/. Umi-OCR/UmiOCR-data/plugins
# 如果后续启动有问题，确保此文件存在且位置正确： plugins/win7_x64_RapidOCR-json/__init__.py, RapidOCR-json.exe

# 进入主仓库
cd Umi-OCR
```

完成后，跳转到 [运行测试](#运行测试) 。

### 2. 手动操作

以下展示没有安装 Git 时，如何手动完成上述操作。

1. 创建一个空的工程目录，如 `Umi-OCR Project` 。
2. 用浏览器下载主仓库压缩包，并解压到工程目录。 https://github.com/hiroi-sora/Umi-OCR/archive/refs/heads/main.zip
3. 下载运行环境仓库压缩包，并解压到工程目录。 https://github.com/hiroi-sora/Umi-OCR_runtime_windows/archive/refs/heads/main.zip
4. 下载运行环境辅助包，并解压到工程目录。 https://github.com/hiroi-sora/Umi-OCR_runtime_windows/releases/download/2.1.5/Umi-OCR_runtime_win7_x64.zip
5. 下载 RapidOCR-json 引擎插件包，并解压到工程目录。 https://github.com/hiroi-sora/Umi-OCR_plugins/releases/download/2.0.0/win7_x64_RapidOCR-json.7z
6. 此时，你应该得到了这4个解压后的文件夹：
    ```
    Umi-OCR-main - 主仓库
    Umi-OCR_runtime_win7_x64 - 运行环境辅助包
    Umi-OCR_runtime_windows-main - 运行环境仓库
    win7_x64_RapidOCR-json - 引擎插件包
    ```
7. 将辅助包（`Umi-OCR_runtime_win7_x64`）内部的所有东西，复制到运行环境仓库（`Umi-OCR_runtime_windows-main`）里。如果存在同名文件，则 **跳过这些文件** 。
8. 将运行环境仓库（`Umi-OCR_runtime_windows-main`）内部的所有东西，复制到主仓库（`Umi-OCR-main`）里。如果存在同名文件，则 **跳过这些文件** 。
9. 将引擎插件的内层目录（`win7_x64_RapidOCR-json/win7_x64_RapidOCR-json`）复制到主仓库的插件目录（`Umi-OCR-main/UmiOCR-data/plugins`）里。如果plugins目录不存在，则创建。
   - 请确保复制后，这个文件的位置正确：`plugins/win7_x64_RapidOCR-json/__init__.py`。
   - **错误示例**：`plugins/win7_x64_RapidOCR-json/win7_x64_RapidOCR-json/__init__.py` 或 `plugins/__init__.py`。
10. 此时，主仓库中应该包含这些文件：
    ```
    Umi-OCR Project\Umi-OCR-main\.vscode
    Umi-OCR Project\Umi-OCR-main\dev-tools
    Umi-OCR Project\Umi-OCR-main\docs
    Umi-OCR Project\Umi-OCR-main\UmiOCR-data
    Umi-OCR Project\Umi-OCR-main\.gitignore
    Umi-OCR Project\Umi-OCR-main\release.py
    Umi-OCR Project\Umi-OCR-main\Umi-OCR.exe
    ……
    ```

### 3. 运行测试

如果已完成上述操作，那么请进入主仓库（`Umi-OCR`或`Umi-OCR-main`），运行`Umi-OCR.exe`，打开`截图OCR`标签页并截一张图。如果一切正确，那么能得到OCR结果。

如果在 Windows 7 环境中遇到 `Failed to create OpenGL context……` 的弹窗，请参照 [win7_x64_opengl32sw](dev-tools/win7_x64_opengl32sw/README.md) 。

## 搭建 Windows 开发环境

经过上述步骤，已经可以运行 Umi-OCR 了。以下的步骤介绍如何搭建开发环境，便于进行代码调试和修改。

### 1. 工欲善其事，必先利其器

- 开发环境系统要求：建议 Win10/11 。Win7也成。
- 编辑器：建议 [VS Code](https://code.visualstudio.com/) 。
  - Tips：VS Code 最后一个支持Win7的版本：[v1.70](https://code.visualstudio.com/updates/v1_70)
- VS Code 插件推荐：
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) （Python规范格式化）
  - [QML](https://marketplace.visualstudio.com/items?itemName=bbenoist.QML) （提供qml语法高亮）
  - [QML Snippets](https://marketplace.visualstudio.com/items?itemName=ThomasVogelpohl.vsc-qml-snippets) （提供qml代码补全）

与常见的Python项目不同，本项目内嵌了所有PY运行环境及第三方库文件。故你不需要额外安装Python和QT等东西，也不需要pip安装任何包。只需一个趁手的编辑器即可。

如果你不喜欢 VS Code ，也可以用任何编辑器——甚至记事本来开发本项目。

### 2. 搭建开发环境

1. 回到主仓库根目录，点击 `Umi-OCR.exe` 测试运行项目。不出意外的话，能正常打开软件界面。
2. 主仓库中的 `.vscode` 目录 VS Code 配置文件目录，已经填写好了必要的环境参数。用 VS Code 打开其中的工作区文件 `Umi-OCR.code-workspace` 。
3. 在 VS Code 内随便打开一个python文件，如 `UmiOCR-data/py_src/run.py` 。不出意外的话，能够显示代码高亮。
4. 尝试点击 F5 调试程序。如果已经能跑起来了，则项目开发环境已经搭建成功。
5. 如果 VS Code 报错 `The Python path in your debug configuration is invalid.` ，则重新指定一下PY解释器路径。按快捷键 `Ctrl+Shift+P` ，然后输入 `Python:Select Interpreter` 。点第一个，然后 `+ Enter inter preter path...` 。
6. 在弹出的文件选择弹窗中，选择 `项目目录/UmiOCR-data/runtime/python.exe` 。
7. 再度点击 F5 调试程序，此时应该肯定能跑起来了。
8. Vs Code 的断点调试等开发工具应该也能正常使用。
   - 注1：只能对python代码进行断点调试，qml代码不行。只能用`console`大法来调试qml。
   - 注2：只能对主线程的代码进行断点。如果有一些代码，如批量OCR任务管理模块，打了断点也没有触发调试；那么说明它运行在子线程。

注意，如果你本地已经安装过python，则建议**不要用本地环境**运行本项目。请使用本项目**内置的py环境**。

### 3. 一键打包脚本 `release.py`

完成开发工作后，你会希望将项目打包为一个便于发布的软件包 。可以使用主仓库根目录下的一键打包脚本`release.py` 。其功能包括：

- 提取必要的代码和依赖库文件
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

### 1. 下载

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

### 2. 安装

将下载的whl包解压，然后塞到 `UmiOCR-data/site-packages` 目录下即可。

有部分包直接放置不能运行，请根据报错信息见机行事。常见的原因有：
- import层级错误。将包内代码修改为相对导入。
- python版本或系统平台错误。请确保此包兼容win 64位、python 3.8 。
大部分包在调整之后可以正常运行，与pip安装无异。

如果某些包有大量依赖、难以安装，如某些大型机器学习库。那么你要思考，将这几百MB塞进项目，会不会影响Umi-OCR的轻便易用性。也许更应该以 [插件](https://github.com/hiroi-sora/Umi-OCR_plugins) 的形式提供这些功能。

### 3. 删减

第三方包含有大量无需使用的功能和dll文件。完全可以删减这些文件以节省空间。

### 4. 贡献

如果你为 Umi-OCR 主仓库贡献了代码，且这些代码必须引入一个新的第三方包，请：

- 确保该包已经删减到最小
- 通过 `release.py` 生成一个发布包
- fork本仓库，将发布包上传到你的仓库的release
- 为 Umi-OCR 主仓库提交代码PR时，附上你的release的链接

# Umi-OCR 项目结构

### 各仓库：

- [主仓库](https://github.com/hiroi-sora/Umi-OCR)
- [插件库](https://github.com/hiroi-sora/Umi-OCR_plugins)
- [Windows 运行库](https://github.com/hiroi-sora/Umi-OCR_runtime_windows) 👈
- [Linux 运行库](https://github.com/hiroi-sora/Umi-OCR_runtime_linux)

### 工程结构：

`**` 后缀表示本仓库(`Windows 运行库`)包含的内容。

```
Umi-OCR
├─ Umi-OCR.exe **
├─ umi-ocr.sh
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

