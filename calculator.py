import tkinter as tk
import ttkbootstrap as tb

w=tb.Window(themename="superhero")
global var
var=tk.StringVar()
global entry
var.set(0)
def window():
    w.title("Calculator")
    w.geometry('350x400+100+100')
    w.resizable(False, False)
    photo = tk.PhotoImage(file="calculator3.png")
    w.iconphoto(False, photo)

equation=""
def get_val(ns):
    global equation,entry
    equation+=ns
    var.set("")
    var.set(equation)

def clear():
    global equation
    equation=""
    var.set("")
def calculation():
    try:
        result=equation
        var.set(eval(result))
    except Exception:
        var.set("Syntaxerror !")
def cal_body():
    global entry
    entry=tb.Entry(w,bootstyle="info",font=("Helvetica",14,"bold"),width=24,foreground="white",textvariable=var)
    entry.pack(pady=60)

    #buttons
    button_style,another=tb.Style(),tb.Style()
    another2=tb.Style()
    button_style.configure("info.Outline.TButton",font=("Helvetica",14,"bold"),foreground="gray")
    another.configure("info.TButton",font=("Helvetica",14,"bold"))
    another2.configure("success.Outline.TButton", font=("Helvetica", 14, "bold"))
    #row1
    b1=tb.Button(w,text="9",width=3,bootstyle="info,outline",style="info.Outline.TButton",command=lambda:get_val("9")).place(x=40,y=130)
    b2 = tb.Button(w, text="8", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("8")).place(x=110, y=130)
    b3 = tb.Button(w, text="7", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("7")).place(x=180, y=130)
    b4 = tb.Button(w, text="AC", width=3, bootstyle="info", style="info.TButton",command=lambda:clear()).place(x=250, y=130)

    #row  2
    b5 = tb.Button(w, text="6", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("6")).place(x=40, y=180)
    b6 = tb.Button(w, text="5", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("5")).place(x=110, y=180)
    b7 = tb.Button(w, text="4", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("4")).place(x=180, y=180)
    b8 = tb.Button(w, text="÷", width=3, bootstyle="info", style="info.TButton",command=lambda:get_val("/")).place(x=250, y=180)
    #row3
    b9 = tb.Button(w, text="3", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("3")).place(x=40, y=230)
    b10 = tb.Button(w, text="2", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("2")).place(x=110, y=230)
    b11= tb.Button(w, text="1", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("1")).place(x=180, y=230)
    b12= tb.Button(w, text="×", width=3, bootstyle="info", style="info.TButton",command=lambda:get_val("*")).place(x=250, y=230)
    #row4
    b13 = tb.Button(w, text=".", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val(".")).place(x=40, y=280)
    b14 = tb.Button(w, text="0", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("0")).place(x=110, y=280)
    b15 = tb.Button(w, text="%", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("%")).place(x=180, y=280)
    b16= tb.Button(w, text="−", width=3, bootstyle="info", style="info.TButton",command=lambda:get_val("-")).place(x=250, y=280)
    #row5
    b17 = tb.Button(w, text="(", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val("(")).place(x=40, y=330)
    b18 = tb.Button(w, text=")", width=3, bootstyle="info,outline", style="info.Outline.TButton",command=lambda:get_val(")")).place(x=110, y=330)
    b19 = tb.Button(w, text="=", width=3, bootstyle="success,outline",style="success.Outline.TButton",command=calculation).place(x=180, y=330)
    b20 = tb.Button(w, text="+", width=3, bootstyle="info", style="info.TButton",command=lambda:get_val("+")).place(x=250, y=330)

    w.mainloop()


window()
cal_body()