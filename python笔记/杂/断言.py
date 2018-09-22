def func(num, div):
    assert (div != 0), "div不能为0"
    return num / div

func(10, 0)
# 函数本身分母不为零，如果为零那么将报错
