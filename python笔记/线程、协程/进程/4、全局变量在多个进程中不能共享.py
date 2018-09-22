from multiprocessing import Process
from time import sleep


num = 100


def run():
    print("子进程开始")

    global num  # 相当于 num=100
    num += 1

    print("子进程结束--%d" % num)

if __name__ == "__main__":
    print("父进程开始")

    p = Process(target=run)
    p.start()
    p.join()
    # 在子进程中修改的全局变量对父进程中的全局变量没有影响
    # 在创建子进程时对全局变量做了一个备份，父进程中的和子进程中的num是完全不同的两个变量
    print("父进程结束--%d" % num)

# 全局变量在多个进程中不能共享
