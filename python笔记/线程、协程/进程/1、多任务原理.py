'''

现代操作系统

什么叫做多任务？
操作系统同时可以运行多个任务


单核CPU实现多任务原理：操作系统轮流让各个任务交替执行

多核CPU实现多任务原理：真正的执行多任务只能在多核CPU上实现，多出来的任务轮流调度到每个核心上执行

并发：看上去一起执行，任务数多于CPU核心数
并行：真正的一起执行，任务数小于等于CPU核心数


实现多任务的方式：
1、多进程模式
2、多线程模式
3、协程模式
4、多进程+多线程模式


'''
