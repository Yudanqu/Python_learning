'''
os:包含了普遍的操作系统的功能
'''

import os

os.name  # 获取操作系统类型
# nt->windows
# posix->Linux\Unix\Mac OS X

os.uname()  # 打印操作系统详细的信息，windows不支持

os.environ  # 获取操作系统所有的环境变量

os.environ.get("name")  # 获取某个环境变量

os.curdir  # 获取当前路径

os.getcwd()  # 获取当前工作目录，即当前python脚本所在目录

os.listdir()  # 列表形式返回指定目录下所有的文件

os.mkdir("name")  # 创建新目录

os.rmdir("name")  # 删除目录

os.stat("name")  # 获取文件属性

os.rename("old", "new")  # 重命名

os.remove("file.txt")  # 删除普通文件

os.system()  # 运行shell命令

os.path.abspath("")  # 查看当前绝对路径

os.path.join(p1, p2)  # 拼接路径，p2里不能有斜杠

os.path.aplit(path)  # 拆分路径
