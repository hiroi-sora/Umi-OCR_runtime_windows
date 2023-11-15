# =========================================
# =============== 生成发布包 ===============
# =========================================

import os
import shutil
import argparse
import subprocess

# 定义参数
parser = argparse.ArgumentParser(description="Umi-OCR Release 生成发布包")
# 发布目录
parser.add_argument("--path", default="./release", help="[选填] 发布包存放路径，默认为 /release")
# 版本文件路径
parser.add_argument(
    "--version", default="./UmiOCR-data/version.py", help="[选填] 版本文件 version.py 的路径"
)
# 启动器路径
parser.add_argument(
    "--run",
    default="Umi-OCR.exe",
    help="[选填] 启动器，默认为 Umi-OCR.exe",
)
# 保留的内容
parser.add_argument(
    "--datas",
    default="i18n,plugins,py_src,qt_res,runtime,site-packages,main.py,RUN_CLI.bat,RUN_GUI.bat,test_speed.bat,version.py,帮助.txt",
    help="[选填] 内容目录文件选取，格式：文件1,文件2,文件3……",
)
# 插件区分
parser.add_argument(
    "--plugins",
    default="Paddle,win7_x64_PaddleOCR-json|Rapid,win7_x64_RapidOCR-json",
    help="[选填] 插件选取，格式：打包名1,插件1,插件2|打包名2,插件2,插件3",
)
# 7z工具路径
parser.add_argument(
    "--path_7z",
    default="7zr.exe",
    help="[选填] 7z 命令行工具的路径，打压缩包要用",
)
# 是否打压缩包
parser.add_argument("--to_7z", action="store_true", help="[选填] 是否生成压缩包")
# 压缩类型
parser.add_argument(
    "--args_7z",
    default="-mx=7 -t7z",
    help="[选填] 7z工具参数，可指定压缩包类型和压缩率等。如-t7z等指定压缩类型参数必须放在最后",
)
args = parser.parse_args()

# 工作路径改为当前文件路径
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


# 拷贝所有文件
def copy_all():
    # 目标路径
    target = args.path + "/temp"
    # 清理/重新创建目标路径
    if os.path.exists(target):
        shutil.rmtree(target)
        print("删除temp")
    os.makedirs(target + "/UmiOCR-data")
    print("开始拷贝基础文件")
    # 拷贝启动器
    shutil.copy(args.run, target)
    print("   ", args.run)
    # 拷贝data
    datas = args.datas.split(",")
    data_target = target + "/UmiOCR-data"
    for data in datas:
        path = "UmiOCR-data/" + data
        if os.path.isfile(path):
            shutil.copy(path, data_target)
            print("   ", path)
        elif os.path.isdir(path):
            print("   ", path)
            shutil.copytree(path, data_target + "/" + data)
    print("结束拷贝基础文件")
    # 清理缓存
    cache_n = 0
    files_n = 0
    files_size = 0
    for root, dirs, files in os.walk(target):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path)
                cache_n += 1
        for f in files:
            file_path = os.path.join(root, f)
            files_size += os.path.getsize(file_path)
            files_n += 1
    print(f"清理缓存：{cache_n}")
    print(f"文件总数：{files_n}，总大小：{files_size//1048576}MB")


copy_all()


# 获取版本号信息
def get_version():
    v = args.version
    with open(v, "r", encoding="utf-8") as f:
        code = f.read()
    exec(code)
    print("读取版本信息")
    v1, v2, v3, p1, p2 = (
        locals().get("MAJOR_VERSION"),  # 主版本号
        locals().get("MINOR_VERSION"),  # 次版本号
        locals().get("PATCH_VERSION"),  # 修订版本号
        locals().get("PRE_RELEASE"),  # 预发布阶段
        locals().get("PRE_RELEASE_VERSION"),  # 预发布版本号
    )
    return v1, v2, v3, p1, p2


v1, v2, v3, p1, p2 = get_version()
print("解析版本信息：", v1, v2, v3, p1, p2)


# 获取插件信息
def get_plugins(v1, v2, v3, p1, p2):
    version = f"_v{v1}.{v2}.{v3}"
    if p1 and p2:
        version += f"_{p1}_{p2}"
    plug = args.plugins
    plug = plug.split("|")
    plugs = {}
    for v in plug:
        ps = v.split(",")
        name = ps[0]
        f = "Umi-OCR_" + name + version
        plugs[name] = {"name": f, "plugins": ps[1:]}
    return plugs


plugs = get_plugins(v1, v2, v3, p1, p2)
print("解析插件信息：", plugs)


# 拷贝生成插件版本文件
def copy_plugins(plugs):
    for key, value in plugs.items():
        print("开始创建插件区分：", key)
        # 目标路径
        target = args.path + "/" + value["name"]
        # 清理/重新创建目标路径
        if os.path.exists(target):
            shutil.rmtree(target)
            print("    删除上次", target)
        # 拷贝文件
        shutil.copytree(args.path + "/temp", target)
        print("    重新创建", target)
        # 删除无关插件目录
        plug_dir = target + "/UmiOCR-data/plugins"
        plugins = os.listdir(plug_dir)
        for plug in plugins:
            if plug not in value["plugins"]:
                path = plug_dir + "/" + plug
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print("    删除", path)


copy_plugins(plugs)

# 检测 7zr.exe 存在
if not os.path.exists(args.path_7z):
    print("未找到 7zr.exe ，停止后续压缩步骤。")


# 生成压缩包
def to_zip(plugs):
    for key, value in plugs.items():
        print("开始创建插件7z压缩包：", key)
        # 目标路径
        target = args.path + "/" + value["name"]
        # 构建7-Zip命令行参数
        command = [
            args.path_7z,
            "a",
            *args.args_7z.split(" "),  # 参数
            target + ".7z",
            target,
        ]
        # 调用7-Zip命令行工具
        subprocess.run(command)


if args.to_7z:
    to_zip(plugs)
