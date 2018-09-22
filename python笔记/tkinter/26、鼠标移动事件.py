
import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")


# <B1-Motion>  左键移动
# <B2-Motion>  中键移动
# <B3-Motion>  右键移动


label = tkinter.Label(win, text="*********")
label.pack()

def func(event):
    print(event.x, event.y)

label.bind("<B1-Motion>", func)

win.mainloop()