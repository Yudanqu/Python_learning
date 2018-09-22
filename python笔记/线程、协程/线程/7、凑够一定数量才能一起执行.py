import threading
import time


# 凑够一定数量的线程才会执行，否则一直等着
bar = threading.Barrier(4)

def run():
    print("%s--start" % (threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    print("%s--end" % (threading.current_thread().name))


if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()
