import tkinter

win = tkinter.Tk()
win.title("yudanqu")
# win.geometry("400x400+200+50")

# EXTENDED：可以使listbox支持shift和Ctrl
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)
lb.pack()

for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)

# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# 配置
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# 额外给属性赋值
sc["command"] = lb.yview

win.mainloop()