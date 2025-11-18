from tkinter import *
def Cong():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a+b))
def Tru():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a-b))
def Nhan():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a*b))

def Chia():
    a=float(stringA.get())
    b=float(stringB.get())
    if b==0:
        stringKQ.set("khong the chia")
    else:
        stringKQ.set(str(a/b))
root = Tk()
stringA =StringVar()
stringB= StringVar()
stringKQ=StringVar()
root.title("tk")
root.minsize(150,200)
root.resizable(True,True)

Label(root,text =" Cong Tru Nhan Chia",font =("tahoma",16),justify = CENTER).grid(row =0,column= 0,columnspan= 3)

frameButton = Frame()
Button(frameButton,text ="Cong",command= Cong).pack(side=TOP,fill= X)
Button(frameButton,text ="Tru",command= Tru).pack(side=TOP,fill =X)
Button(frameButton,text ="Nhan",command= Nhan).pack(side=TOP,fill= X)
Button(frameButton,text ="Chia",command =Chia).pack(side=TOP,fill =X)
frameButton.grid(row=1,column=0,rowspan=4)
Label(root,text ="so a: ").grid(row=1,column =1)
Entry(root,width=15,textvariable= stringA).grid(row=1,column =2)

Label(root,text ="so b: ").grid(row=2,column =1)
Entry(root,width=15,textvariable= stringB).grid(row=2,column =2)

Label(root,text ="ket qua: ").grid(row=3,column =1)
Entry(root,width=15,textvariable= stringKQ).grid(row=3,column =2)

Button(root,text="Thoat",command = root.quit).grid(row=4,column =2)

root.mainloop()

