import threading
import time


# 线程条件变量
cond = threading.Condition()


def run():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.wait()  # 阻塞
            cond.notify()  # 告诉另一个线程可以执行


def run2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.notify()
            cond.wait()


threading.Thread(target=run).start()
threading.Thread(target=run2).start()
