#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scipy.misc
import sys
import matplotlib.pyplot as plt
import numpy.testing

# 这个脚本用来调整scipy库中图像ascent的大小
if len(sys.argv) != 3:
	print("Usage python %s yfactor xfactor" %(sys.argv[0]))
	sys.exit()

# 加载图像ascent到一个数组中
ascent = scipy.misc.ascent()
# 图像ascent的规格
ASCENT_X = 512
ASCENT_Y = 512
# 检查数组ascent的形状
numpy.testing.assert_equal((ASCENT_X,ASCENT_Y),ascent.shape)

# 获取调整系数
yfactor = float(sys.argv[1])
xfactor = float(sys.argv[2])

# 调整ascent的大小
resized = ascent.repeat(yfactor,axis=0).repeat(xfactor,axis=1)

# 检查大小调整后的数组形状
numpy.testing.assert_equal((yfactor * ASCENT_Y,xfactor * ASCENT_X),resized.shape)

# 绘制数组ascent
plt.subplot(211)
plt.imshow(ascent)

# 绘制大小调整后的数组
plt.subplot(212)
plt.imshow(resized)
plt.show()