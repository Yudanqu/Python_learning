'''

在一个进程内部，要同时干多件事，就需要运行多个"子任务"，我们把进程内的多个"子任务"叫做线程

线程通常叫做轻型的进程，线程是共享内存空间，并发执行的多任务，每一个线程都共享一个进程的资源

线程是最小的执行单元而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统来决定，程序自己不能决定什么时候执行，执行多长时间

模块：
1、_thread模块      低级模块（更接近底层）
2、threading模块	   高级模块，对_thread进行了封装

'''