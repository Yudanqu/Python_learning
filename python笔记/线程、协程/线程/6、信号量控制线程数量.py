import threading
import time

# 控制并发执行线程的数量
sem = threading.Semaphore(2)

def run():
	with sem:
		for i in range(10):
			print("%s---%d" % (threading.current_thread().name, i))
			time.sleep(1)


if __name__ == "__main__":
	for i in range(5):
		threading.Thread(target=run).start()