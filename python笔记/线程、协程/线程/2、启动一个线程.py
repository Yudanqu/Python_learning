import threading
import time


def run():
	print("子线程(%s)启动" % (threading.current_thread().name))

	# 实现线程的功能
	time.sleep(1)
	print("打印")
	time.sleep(2)

	print("子线程(%s)结束" % (threading.current_thread().name))


if __name__ == "__main__":
	# 任何进程都默认会启动一个线程，称为主线程，主线程可以启动新的子线程
	# current_thread()：返回线程的实例
	print("主线程(%s)启动" % (threading.current_thread().name))

	# 创建子线程
	t = threading.Thread(target=run, name="runThread")
	t.start()

	# 等待线程结束
	t.join()

	print("主线程(%s)结束" % (threading.current_thread().name))