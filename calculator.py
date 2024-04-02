# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:08:00 2024
build a calculator 
pg no 388
23.03.2024
@author: Riyaz
"""
import tkinter as tk
w=tk.Tk()
def window():
    w.title('SIMPLE CALCULATOR') 
    w.geometry('435x450+0+0')
    w.resizable(False,False)
    w.configure(bg='black')
    photo=tk.PhotoImage(file='D:\exe\\calculator3.png')
    w.iconphoto(False,photo)
def click1():
    global s
    s+="1"
    l1.configure(text=s)
def click2():
    global s
    s+="2"
    l1.configure(text=s)
def click3():
    global s
    s+="3"
    l1.configure(text=s)
def clickadd():
    global s 
    s+='+'
    l1.configure(text=s)
def click4():
    global s
    s+="4"
    l1.configure(text=s)
def click5():
    global s
    s+="5"
    l1.configure(text=s)
def click6():
    global s
    s+="6"
    l1.configure(text=s)
def click7():
    global s
    s+="7"
    l1.configure(text=s)
def clicksub():
    global s
    s+='-'
    l1.configure(text=s)
def click8():
    global s
    s+="8"
    l1.configure(text=s)
def click9():
    global s
    s+="9"
    l1.configure(text=s)
def click0():
    global s
    s+="0"
    l1.configure(text=s)
def clickproduct():
    global s
    s+='*'
    l1.configure(text=s)
def clickpoint():
    global s
    s+='.'
    l1.configure(text=s)
def clickequals():
    global s
    x=eval(s)
    tot=str(x)
    s=""
    s+=tot
    l1.configure(text=s)
def clickdivide():
    global s 
    s+='/'
    l1.configure(text=s)
def design():
    global l1
    l1=tk.Label(w,font=('arial',24),fg='black',bg='white',width=18)
    l1.place(x=40,y=50)
    b1=tk.Button(w,text='1',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click1)
    b1.place(x=40,y=125)
    b2=tk.Button(w,text='2',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click2)
    b2.place(x=130,y=125)
    b3=tk.Button(w,text='3',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click3)
    b3.place(x=220,y=125)
    b4=tk.Button(w,text='+',font=('times new roman',24,'bold'),bg='orange',fg='black',width=4,bd=0,command=clickadd)
    b4.place(x=310,y=125)
    b5=tk.Button(w,text='4',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click4)
    b5.place(x=40,y=200)
    b6=tk.Button(w,text='5',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click5)
    b6.place(x=130,y=200)
    b7=tk.Button(w,text='6',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click6)
    b7.place(x=220,y=200)
    b8=tk.Button(w,text='-',font=('times new roman',24,'bold'),bg='orange',fg='black',width=4,bd=0,command=clicksub)
    b8.place(x=310,y=200)
    b9=tk.Button(w,text='7',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click7)
    b9.place(x=40,y=275)
    b10=tk.Button(w,text='8',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click8)
    b10.place(x=130,y=275)
    b11=tk.Button(w,text='9',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click9)
    b11.place(x=220,y=275)
    b12=tk.Button(w,text='×',font=('times new roman',24,'bold'),bg='orange',fg='black',width=4,bd=0,command=clickproduct)
    b12.place(x=310,y=275)
    b13=tk.Button(w,text='0',font=('times new roman',24),bg='black',fg='white',width=4,bd=1,command=click0)
    b13.place(x=40,y=350)
    b14=tk.Button(w,text='.',font=('times new roman',24,'bold'),bg='black',fg='white',width=4,bd=1,command=clickpoint)
    b14.place(x=130,y=350)
    b15=tk.Button(w,text='=',font=('times new roman',24,'bold'),bg='black',fg='white',width=4,bd=1,command=clickequals)
    b15.place(x=220,y=350)
    b16=tk.Button(w,text='÷',font=('times new roman',24,'bold'),bg='orange',fg='black',width=4,bd=0,command=clickdivide)
    b16.place(x=310,y=350)
    w.mainloop()
global s
s=""
window()
design()

