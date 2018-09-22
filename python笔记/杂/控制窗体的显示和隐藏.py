import win32con
import win32gui
import time


# 找出窗体的编号
QQwin = win32gui.FindWindow("TXGuiFoundation", "QQ")

# 隐藏窗体
win32gui.ShowWindow(QQwin, win32con.SW_HIDE)

time.sleep(5)

# 显示窗体
win32gui.ShowWindow(QQwin, win32con.SW_SHOW)
