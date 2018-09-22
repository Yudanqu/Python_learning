
import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# <ButtonRelease-1> 释放鼠标左键
# <ButtonRelease-2> 释放鼠标中键
# <ButtonRelease-3> 释放鼠标右键


label = tkinter.Label(win, text="*********", bg="red")
label.pack()

def func(event):
    print(event.x, event.y)

label.bind("<ButtonRelease-1>", func)

win.mainloop()