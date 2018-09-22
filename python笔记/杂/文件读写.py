# ********读文件*********
1、打开文件
open(path, flag[, encoding][, errors])
path:
    要打开文件的路径
flag:
    打开方式
r   以只读的方式打开文件，文件的描述符放在文件的开头
rb  以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
r + 打开一个文件用于读写，文件的描述符放在文件的开头
w   打开一个文件只用于写入，如果该文件已经存在会覆盖，不存在则创建新文件
wb  打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，不存在则创建新文件
w + 打开一个文件用于读写，如果该文件已经存在会覆盖，不存在则创建新文件
a   打开一个文件用于追加如果文件存在，文件描述符将会放到文件末尾
a+
encoding：编码方式（一般utf - 8）
errors：错误处理（一般不处理）


f = open(path, "r", encoding="utf-8", errors="ignore")
# ignore 忽略错误，一般不写后两个参数


2、读文件内容

# 读取文件全部内容
str1 = f.read()  # 度文件比较小的，大的内存放不下

# 读取指定字符数（按字符数）
str2 = f.read(10)

# 读取整行，包括"\n"字符
str3 = d.readline()

# 读取指定字符数
str4 = f.readline(10)

# 读取所有行并返回列表
str5 = f.readlines()

# 若给定的数字大于0，返回实际size字节的行数
str6 = f.readlines(25)

# 修改描述符的位置
f.seek(10)  # 改到第几个字符的位置


3、关闭文件
f.close()


# 一个完整的过程

try:
    f1.open(path, "r", encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

# 简单方法：

with open(path, "r", encoding="utf-8") as f2:
    print(f2.read())


# *************写文件*****************

f = open(path, "w")


# 将信息写入缓冲区
f.write("glabscufn")

# 刷新缓冲区
f.flush()  # 直接把内部缓冲区的数据立刻写入文件，而不是被打的等待关闭自动刷新缓冲区写入
# 缓冲区的刷新：1、文件关闭自动刷新 2、手动flush刷新 3、缓冲区满了也可以自动刷新 4、再有就是遇到'\n'也会刷新


f.close()


# ************编码与解码****************

# 编码
with open(path, "wb") as f1:
    str = "asdasdasdasd"
    f1.write(str.encode('utf-8'))
# 解码
with open(path, "rb") as f2:
    data = f2.read()
    new_data = data.decode("utf-8")
    print(type(data))  # byte
    print(type(new_data))  # str
# 主要是在有中文的情况下，其他情况不同的码可能也译码正确
# 如果是二进制的字符串，要记得编码解码


'''
list,tuple,dict,set的文件读写
'''

import pickle  # 数据持久性模块
# 就是把数据存到磁盘


mylist = [1, 2, 3, 4, 5, "sadd"]
f = open(path, "wb")

pickle.dump(mylist, f)

f.close()

# 读
f1 = open(path, "rb")
templist = pickle.load(f1)
print(templist)
f1.close()
