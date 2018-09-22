
import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")


label = tkinter.Label(win, text="*********", bg="red")
# 设置焦点
label.focus_set()
label.pack()

def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)


win.bind("a", func) # 注意前面改成了win，只需要写出按键名即可


win.mainloop()