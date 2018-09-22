import threading
'''	
两个线程同时工作，一个存钱，一个取钱

可能导致数据异常

思路：加锁

'''

# 锁对象
lock = threading.Lock()

num = 10

def run(n):
	global num
	for i in range(10000000):
		# 锁
		# 确保了这段代码只能由一个线程从头到尾的完整执行
		# 阻止了多线程的并发执行，要比不加锁时候效率低。包含锁的代码段只能以单线程模式执行
		# 由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁导致多个线程挂起，只能靠操作系统强制终止

		
		'''
		lock.acquire()
		try:
			num = num + n
			num = num - n
		finally:
			# 修改完释放锁
			lock.release()
		'''

		# 与上面代码功能相同,with lock可以自动上锁与解锁
		with lock:
			num = num + n
			num = num - n

if __name__ == "__main__":
	t1 = threading.Thread(target=run, args=(6,))
	t2 = threading.Thread(target=run, args=(9,))

	t1.start()
	t2.start()
	t1.join()
	t2.join()

	print("num = ",num)