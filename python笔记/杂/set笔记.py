set：类似于dict，是一组key的集合，不存储value
本质：无序和无重复元素的集合


创建：
创建set需要一个list或者tuple或者dict作为输入集合
重复元素在set中会自动过滤

添加：
s.add(6)  # 若添加重复的则无效果
s.add([7, 8, 9])  # 报错，因为列表不能作为key，list是可变对象，以及dict
元组可以作为添加的对象，因为元组不可变

s.update() 可以将列表元组等拆分开打碎存入set

删除：
s.remove() 参数为里面的元素，不能通过下标删除

set没有索引，但可以遍历输出
也可以通过 for index，data in enumeration(s):
貌似是有索引，但是没有用

交集：
a1 = s1 & s2
求交集并输出新的set

并集：
a2 = s1 | s2
求并集返回新的set

set本身不常用，但可以利用他的类型转换：
    利用其无重复的特性
