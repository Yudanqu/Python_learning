'''
进程：

对于操作系统而言，一个任务就是一个进程

进程是系统中程序执行和资源分配的基本单元，每个进程都有自己的数据段、代码段、堆栈段

'''


'''
单任务现象：


'''

# from time import sleep
# # 只能执行到那一个循环，执行不了run，所以叫单任务
# def run():
# 	while True:
# 		print("&&&&&&&&&&&&&&&")
# 		sleep(1.2)

# if __name__ == "__main__":
# 	while True:
# 		print("**********")
# 		sleep(1)
# 	run()


'''
启动进程实现多任务

multiprocessing库：跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象（fork仅适用于Linux）

'''

from multiprocessing import Process
from time import sleep
import os

# 子进程需要执行的代码


def run(str):
    # os.getpid()获取当前进程id号
    # os.getppid()获取当前进程的父进程id号
    print("&&&&&&&&&&&&&&&%s--%s--%s" % (str, os.getpid(), os.getppid()))
    sleep(0.5)

if __name__ == "__main__":
    print("主（父）进程启动 %s" % (os.getpid()))
    # 创建子进程
    # target说明进程执行的任务
    p = Process(target=run, args=("nice",))
    # 启动进程
    p.start()

    while True:
        print("**********")
        sleep(1)


