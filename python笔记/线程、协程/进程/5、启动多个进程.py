from multiprocessing import Pool
import os
import time
import random


def run(name):
    print("子进程%s启动--%s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3,4,5]))
    end = time.time()
    print("子进程%s结束--%s--耗时%.2f" % (name, os.getpid(), end-start))

if __name__ == "__main__":
    print("启动父进程")

    # 创建多个进程
    # Pool 进程池 :括号里的数表示可以同时执行的进程数量
    # Pool()默认大小是CPU核心数
    pp = Pool(4)
    for i in range(5):
    	# 创建进程，放入进程池，统一管理
    	pp.apply_async(run, args=(i,))

    # 在调用join之前必须先调用close，调用close之后就不能再继续添加新的进程了
    pp.close()
    # 进程池对象调用join还等待进程池中所有的子进程结束
    pp.join()

    print("结束父进程")
