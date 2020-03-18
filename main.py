import tkinter as tk
from tkinter import  *

window = tk.Tk()
window.title('Excel文件对比异同程序')

#left区
#--------变量确定
file_address1 = tk.StringVar() #地址
excel_sheet1 = tk.StringVar()#excel 工作表

file_address2 = tk.StringVar() #地址
excel_sheet2 = tk.StringVar()#excel 工作表

#---------布局
#left-top
frame_left_top = Frame(width = 250,height = 150)
frame_left_top.grid(row = 0,column = 0,padx = 1,pady = 3)

frame_left_mid = Frame(width = 250,height = 150,bg = 'red')
frame_left_mid.grid(row = 0,column = 0,padx = 1,pady = 3)

frame_left_bot = Frame(width = 250,height = 80,bg = 'blue')
frame_left_bot.grid(row = 0,column = 0,padx = 1,pady = 3)

#right区
frame_right = Frame(width =280,height = 380,bg = 'white' )
frame_right.grid(row = 0,column = 1,padx = 1,pady = 3,)
window.mainloop()