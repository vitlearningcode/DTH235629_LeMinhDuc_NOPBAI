from tkinter import*
from math import sqrt
def tiepAction():
    stringA.set("")
    stringB.set("")
    stringC.set("")
    stringKQ.set("")

def giaiAction():
    a=float(stringA.get())
    b=float(stringB.get())
    c=float(stringC.get())
    if a==0:
        if b==0:
            if c==0:
                stringKQ.set("Phuong trinh co vo so nghiem")
            else:
                stringKQ.set("Vo nghiem")
        else:
            stringKQ.set("x="+str ((-c/b)))
    else:
        dental= b**2 - 4*a*c
        
        if dental < 0 :
            stringKQ.set("Vo nghiem")
        elif dental ==0 :
            stringKQ.set("Nghiem kep x="+str((-b)/(2*a)))
        else:
            can= sqrt(dental)
            x1= (-b-can)/(2*a)
            x2= (-b+ can)/(2*a)
            stringKQ.set("x1="+str(x1)+" ; x2="+str(x2))






root = Tk()
stringA= StringVar()
stringB= StringVar()
stringC= StringVar()
stringKQ = StringVar()
root.title("PTB2")
root.minsize(height = 130,width=250)
root.resizable(height = True,width =True)

Label(root,text ="Phuong tring Bac 2",fg="red",font=("Times New Roman",16),justify=CENTER).grid(row =0,column =0,columnspan=2)

Label(root,text="He so a:").grid(row =1,column =0)
Entry(root,width =30,textvariable =stringA).grid(row=1,column=1)

Label(root,text="He so b:").grid(row =2,column =0)
Entry(root,width =30,textvariable =stringB).grid(row=2,column=1)

Label(root,text="He so c:").grid(row =3,column =0)
Entry(root,width =30,textvariable =stringC).grid(row=3,column=1)


frameButton = Frame()
Button(frameButton,text =" Giai",command=giaiAction).pack(side= LEFT)
Button(frameButton,text="Tiep",command= tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoat",command= root.quit).pack(side=LEFT)
frameButton.grid(row=4,columnspan=2,padx=5,pady=5)

Label(root,text="Ket qua").grid(row=5,column =0,padx=5,pady=5)
Entry(root,width =30,textvariable=stringKQ).grid(row=5,column =1,padx=5)

root.mainloop()