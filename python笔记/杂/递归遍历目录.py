import os

path = r"E:\通工1614课件"

# 递归遍历目录


def getAllDir(path, sp=''):
    # 得到当前目录下的所有文件
    filesList = os.listdir(path)

    sp += "  "
    # 处理每一个文件
    for fileName in filesList:
        # 判断是否是路径（要用绝对路径）
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：", fileName)
            getAllDir(fileAbsPath, sp="  ")
        else:
            print(sp + "普通文件：", fileName)


getAllDir(path)


# 栈模拟递归遍历目录（深度遍历）

def getAllDirDFS(path):
    stack = []
    stack.append(path)

    # 处理栈，当栈为空时结束循环
    while len(stack) != 0:
        # 从栈中取出数据
        dirPath = stack.pop()
        # 目录下所有文件
        filesList = os.listdir(dirPath)

        # 处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录地址压栈
        for fileName in filesList:
            # print(dirPath)
            fileAbsPath = os.path.join(dirPath, fileName)
            # print(fileAbsPath)
            if os.path.isdir(fileAbsPath):
                # 是目录就压栈
                print("目录：" + fileName)
                stack.append(fileAbsPath)
            else:
                # 打印普通文件
                print("普通：" + fileName)

getAllDirDFS(path)


# 队列模拟递归遍历目录（广度遍历）

import collections


def getAllDirBFS(path):
    queue = collections.deque()
    queue.append(path)

    while len(queue) != 0:
        dirPath = queue.popleft()
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print('目录：' + fileName)
                queue.append(fileAbsPath)
            else:
                print('文件：' + fileName)

getAllDirBFS(path)
