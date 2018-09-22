from multiprocessing import Process, Pool
import os
import time


class myProcess(Process):

	def __init__(self, name):
		Process.__init__(self)
		self.name = name

	def run(self):
		print("子进程(%s-%s)启动" % (self.name, os.getpid()))
		time.sleep(2)
		print("子进程(%s-%s)结束" % (self.name, os.getpid()))