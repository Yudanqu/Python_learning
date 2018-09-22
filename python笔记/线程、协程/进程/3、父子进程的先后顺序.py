from multiprocessing import Process
from time import sleep
import os


def run():
    print("启动子进程")
    print("子进程结束")
    sleep(3)


if __name__ == "__main__":
    print("父进程启动")
    p = Process(target=run)
    p.start()

    # 父进程的结束不能影响子进程，让进程等待子进程结束再执行父进程
    p.join()

    print("父进程结束")
