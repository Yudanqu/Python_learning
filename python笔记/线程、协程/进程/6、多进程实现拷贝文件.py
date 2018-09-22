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


if __name__ == "__main__":
    # 读取path下的所有文件
    filesList = os.listdir(path)

    start = time.time()
    pp = Pool(4)
    for fileName in filesList:
        pp.apply_async(copyFile, args=(os.path.join(
            path, fileName), os.path.join(toPath, fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print("总耗时：%.2f" % (end - start))
