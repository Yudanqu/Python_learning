#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter


def func():
    print("aaaaaaaaaaaaaaaaaaaaaaa")


win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")


# 创建按钮
button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=10)
button1.pack()

button2 = tkinter.Button(win, text="按钮", command=lambda: print("bbbbbbbbbbbb"))
button2.pack()

button3 = tkinter.Button(win, text="退出", command=win.quit)
button3.pack()

win.mainloop()
