import tkinter as tk
from tkinter import  *
import tkinter.font as tkFont
from tkinter.filedialog import askdirectory
window = tk.Tk()
window.title('Excel文件对比异同程序')

#left区
#--------变量确定
file_address1 = tk.StringVar() #地址
excel_sheet1 = tk.StringVar()#excel 工作表

file_address2 = tk.StringVar() #地址
excel_sheet2 = tk.StringVar()#excel 工作表

xsd_adress = tk.StringVar()

message = tk.StringVar()
def selectPath():
    path_ = askdirectory()
    xsd_adress.set(path_)

#---------布局
#left-top
#字体设置
ft = tkFont.Font(size=10, weight=tkFont.BOLD)
#第一个文件
frame_left_top = Frame(width = 250,height = 120)
frame_left_top.grid(row = 0,column = 0,padx = 1,pady = 1)
Label(frame_left_top,text = "选择原文件：",font=ft).grid(row = 0,column = 0,pady = 20,sticky = W)
btn_add_adress = Button(frame_left_top, text='+',width = 2,font = ft,bg = 'CornflowerBlue',command = selectPath).grid(row=1, pady = 20,column=0,sticky = W)
Entry(frame_left_top,textvariable = file_address1,width = 28,insertbackground = 'blue').grid(row=1, column=0,padx = 30)
#第二个文件
frame_left_mid = Frame(width = 250,height = 120)
frame_left_mid.grid(row = 2,column = 0,padx = 1,pady = 1)
Label(frame_left_mid,text = "选择对比文件：",font=ft).grid(row = 2,column = 0,pady = 20,sticky = W)
btn_add_adress1 = Button(frame_left_mid, text='+',width = 2,font = ft,bg = 'CornflowerBlue',command = selectPath).grid(row=3, pady = 20,column=0,sticky = W)
Entry(frame_left_mid,textvariable = file_address2,width = 28,insertbackground = 'blue').grid(row=3, column=0,padx = 30)
#确定按钮
frame_left_bot = Frame(width = 250,height = 140)
frame_left_bot.grid(row = 4,column = 0,padx = 1,pady = 1)
Button(frame_left_bot, text='取消', height=1, width=10, command="#").grid(row = 0,column = 0,padx = 10,pady = 20)
Button(frame_left_bot, text='确定', height=1, width=10, command="#").grid(row = 0,column = 1,padx = 10,pady = 20)

window.mainloop()