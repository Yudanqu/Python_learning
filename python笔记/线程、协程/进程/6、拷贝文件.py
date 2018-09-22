from multiprocessing import Pool
import time
import os

# 实现文件的拷贝

def copyFile(rPath, wPath):
	fr = open(rPath, 'rb')
	fw = open(wPath, 'wb')
	context = fr.read()
	fw.write(context)
	fr.close()
	fw.close()

path = r'F:\python_note\线程、协程'
toPath = r'F:\python_note\test'

# 读取path下的所有文件
filesList = os.listdir(path)

# 启动for循环处理每一个文件
start = time.time()
for fileName in filesList:
	copyFile(os.path.join(path,fileName), os.path.join(toPath,fileName))

end = time.time()
print('总耗时：%.2f' % (end-start))