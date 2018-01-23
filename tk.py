from tkinter import *
from tkinter.messagebox import showinfo

def replay():
	showinfo(title='popup', message='点击按钮事件！')

window = Tk()
button = Button(window, text='点击我', command = replay)
button.pack()
window.mainloop()