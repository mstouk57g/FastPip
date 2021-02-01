from os import system, _exit
import tkinter
from tkinter import ttk
from time import sleep
a = None
b = None

win = tkinter.Tk()
win.title("pip")
win.geometry("350x200+100+100")
win.iconbitmap("A:/Python39/Scripts/pip.exe")

tkinter.Label(win, text="下载网站:", font=("楷体", 15)).place(x=5, y=5)
tkinter.Label(win, text="模块名称:", font=("楷体", 15)).place(x=5, y=30)
def go(*args):
    global a, b
    a = comvalue.get()  
e1 = tkinter.StringVar()
e2 = tkinter.Entry(win, textvariable=e1, font=("楷体", 15), width=15).place(x=105, y=30)
comvalue=tkinter.StringVar()
comboxlist=ttk.Combobox(win,textvariable=comvalue)
comboxlist.place(x=105, y=5)
comboxlist.pack()
comboxlist["values"]=("清华","阿里","山东理工大学","中国科学技术大学","华中理工大学","豆瓣","PyPI","TestPyPI")
comboxlist.current(6)
comboxlist.bind("<<ComboboxSelected>>",go)


def og(*args):
    b = e1.get() 
    d = {"PyPI":"https://pypi.org",
         "TestPyPI":"https://test.pypi.org",
         "豆瓣":"https://pypi.douban.com/simple/",
         "阿里":"https://mirrors.aliyun.com/pypi/simple/",
         "华中理工大学":"https://pypi.hustunique.com/simple/",
         "山东理工大学":"https://pypi.sdutlinux.org/simple/",
         "中国科学技术大学":"https://pypi.mirrors.ustc.edu.cn/simple/",
         "清华":"https://pypi.tuna.tsinghua.edu.cn/simple"}
    if a == None:
        c = "https://pypi.org"
    else:
        c = d.get(a)
    e = "python -m pip install " + b +" -i " + c
    print("Trying command:" + e)
    system("python -m pip install " + b +" -i " + c)
    print("Program will exit after 5 seconds")
    sleep(5)
    _exit(1)
    
tkinter.Button(win, text="安装模块", font=("楷体", 15), command=og).place(x=100, y=90)
win.mainloop()





#http://pypi.douban.com/simple/ 豆瓣
#http://mirrors.aliyun.com/pypi/simple/ 阿里
#http://pypi.hustunique.com/simple/ 华中理工大学
#http://pypi.sdutlinux.org/simple/ 山东理工大学
#http://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学
#https://pypi.tuna.tsinghua.edu.cn/simple 清华
