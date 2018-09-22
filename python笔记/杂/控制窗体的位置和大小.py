import win32con
import win32gui
import random
import time


# 找出窗体的编号
QQwin = win32gui.FindWindow("TXGuiFoundation", "QQ")


# 参数1：控制的窗体
# 参数2：大致的方位
# 参数3：位置x
# 参数4：位置y
# 参数5：长度
# 参数6：宽度

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQwin, win32con.HWND_TOPMOST, x,
                          y, 600, 300, win32con.SWP_SHOWWINDOW)
