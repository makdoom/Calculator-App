from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("260x400+370+200")
root.wm_iconbitmap('icon.ico')
root.resizable(0,0)
# CLICK FUNCTION
def click(event):
    global txtValue
    text = event.widget.cget('text')
    if text == '=':
        if txtValue.get().isdigit():
            value = int(txtValue.get())
        else:
            try:
                value = eval(txtValue.get())
            except Exception as e:
                print(e)
                value = "Error"

        txtValue.set(value)
        lbl1.update()
    elif text =="C":
        txtValue.set("")
        lbl1.update()
    else:
        if txtValue.get() == '0':
            txtValue.set(text)
        else:
            txtValue.set(txtValue.get() + text)
            lbl1.update()

# LABEL
txtValue = StringVar()
txtValue.set("0")
lbl1 = Label(root, textvar=txtValue, bg="#000000",fg="#ffffff", anchor='se', font='lucida 25', border=0,pady=10,padx=10)
lbl1.pack(expand=TRUE, fill='both',ipadx=0)
# First Frame / 1st Row
frame1 = Frame(root)
frame1.pack(expand=TRUE, fill='both',ipadx=0,ipady=0)
# Second Frame / 2nd Row
frame2 = Frame(root)
frame2.pack(expand=TRUE, fill='both',ipadx=0,ipady=0)
# Third Frame / 3rd Row
frame3 = Frame(root)
frame3.pack(expand=TRUE, fill='both',ipadx=0,ipady=0)
# Fourth Frame / 4th Row
frame4 = Frame(root)
frame4.pack(expand=TRUE, fill='both',ipadx=0,ipady=0)

# ROW ONE
btn9 = Button(frame1,text='9', bg="#000000",fg="#ffffff", font='lucida 20', border=0)
btn9.pack(side=LEFT, expand=TRUE, fill='both')
btn9.bind('<Button-1>', click)
btn8 = Button(frame1,text='8', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn8.pack(side=LEFT, expand=TRUE, fill='both')
btn8.bind('<Button-1>', click)
btn7 = Button(frame1,text='7', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn7.pack(side=LEFT, expand=TRUE, fill='both')
btn7.bind('<Button-1>', click)
btnPlus = Button(frame1,text='+', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btnPlus.pack(side=LEFT, expand=TRUE, fill='both')
btnPlus.bind('<Button-1>', click)

# ROW TWO
btn6 = Button(frame2,text='6', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn6.pack(side=LEFT, expand=TRUE, fill='both')
btn6.bind('<Button-1>', click)
btn5 = Button(frame2,text='5', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn5.pack(side=LEFT, expand=TRUE, fill='both')
btn5.bind('<Button-1>', click)
btn4 = Button(frame2,text='4', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn4.pack(side=LEFT, expand=TRUE, fill='both')
btn4.bind('<Button-1>', click)
btnMin = Button(frame2,text='-', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btnMin.pack(side=LEFT, expand=TRUE, fill='both')
btnMin.bind('<Button-1>', click)

# ROW THREE
btn3 = Button(frame3,text='3', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn3.pack(side=LEFT, expand=TRUE, fill='both')
btn3.bind('<Button-1>', click)
btn2 = Button(frame3,text='2', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn2.pack(side=LEFT, expand=TRUE, fill='both')
btn2.bind('<Button-1>', click)
btn1 = Button(frame3,text='1', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn1.pack(side=LEFT, expand=TRUE, fill='both')
btn1.bind('<Button-1>', click)
btnMul = Button(frame3,text='*', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btnMul.pack(side=LEFT, expand=TRUE, fill='both')
btnMul.bind('<Button-1>', click)

# ROW FOUR
btn0 = Button(frame4,text='0', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btn0.pack(side=LEFT, expand=TRUE, fill='both')
btn0.bind('<Button-1>', click)
btnClear = Button(frame4,text='C', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btnClear.pack(side=LEFT, expand=TRUE, fill='both')
btnClear.bind('<Button-1>', click)
btnEqual = Button(frame4,text='=', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btnEqual.pack(side=LEFT, expand=TRUE, fill='both')
btnEqual.bind('<Button-1>', click)
btnDiv = Button(frame4,text='/', bg="#000000",fg="#ffffff",font='lucida 20', border=0)
btnDiv.pack(side=LEFT, expand=TRUE, fill='both')
btnDiv.bind('<Button-1>', click)


root.mainloop()