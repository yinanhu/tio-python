# -*- coding: utf-8 -*-
#Author Yinan Hu

from tkinter import *
import tldevice
import time

csb = tldevice.Device('COM5')
'''Building the communication'''

root = Tk()
root.geometry("600x600+300+0")
root.title('Current Supply Control Twinleaf')  # title
v = StringVar()
s1 = Scale(root,from_ = -40,
      to = 40,#max value
      orient = HORIZONTAL,# direction
      label='X channel:',
      resolution=0.001,#step
      tickinterval = 10,
      length = 600)
s1.pack()
s2 = Scale(root,
      from_ = -40,#min value
      to = 40,
      orient = HORIZONTAL,
      label='Y channel:',
      resolution=0.001,
      tickinterval = 10,
      length = 600)

s2.pack()
s3 = Scale(root,
      from_ = -40,#
      to = 40,#
      orient = HORIZONTAL,#
      label='Z channel:',
      resolution=0.001,#
      tickinterval = 10,#
      length = 600,# 
      variable = v)#
s3.pack()
print(v.get())


def xshow():
    print(s1.get(),s2.get(),s3.get())
    print(csb.coil.x.current(),csb.coil.y.current(),csb.coil.z.current())
    csb.coil.x.current(-s1.get())  # mA


def yshow():
    print(s1.get(),s2.get(),s3.get())
    print(csb.coil.x.current(),csb.coil.y.current(),csb.coil.z.current())
    csb.coil.y.current(-s2.get())  # mA


def zshow():
    print(s1.get(),s2.get(),s3.get())
    print(csb.coil.x.current(),csb.coil.y.current(),csb.coil.z.current())
    csb.coil.z.current(s3.get())  # mA
Output_btn=Button(root,text = 'X_Current_output',command = xshow,anchor='w') #
Output_btn.pack()
Output_btn=Button(root,text = 'Y_Current_output',command = yshow,anchor='w') #
Output_btn.pack()
Output_btn=Button(root,text = 'Z_Current_output',command = zshow,anchor='w') 
Output_btn.pack()

l1 = Label(root, text="X input(mA)：",anchor='w')
l1.pack(side=TOP, anchor=W, fill=X, expand=YES)  # 
xls_text = StringVar()
xls = Entry(root, textvariable=xls_text)
xls_text.set(" ")
xls.pack(side=TOP, anchor=W, fill=X, expand=NO)

l2 = Label(root, text="Y input(mA)：",anchor='w')
l2.pack(side=TOP, anchor=W, fill=X, expand=YES)  # 
sheet_text = StringVar()
sheet = Entry(root, textvariable=sheet_text)
sheet_text.set(" ")
sheet.pack(side=TOP, anchor=W, fill=X, expand=NO)

l3 = Label(root, text="Z input(mA)：",anchor='w')
l3.pack(side=TOP, anchor=W, fill=X, expand=YES)  
loop_text = StringVar()
loop = Entry(root, textvariable=loop_text)
loop_text.set(" ")
loop.pack(side=TOP, anchor=W, fill=X, expand=NO)

def on_click_X():
    x = xls_text.get()
    print(csb.coil.x.current(),csb.coil.y.current(),csb.coil.z.current())
    csb.coil.x.current(-float(x))  # mA



def on_click_Y():
    s = sheet_text.get()
    print(csb.coil.x.current(),csb.coil.y.current(),csb.coil.z.current())
    csb.coil.y.current(-float(s))  # mA


def on_click_Z():
    l = loop_text.get()
    print(csb.coil.x.current(),csb.coil.y.current(),csb.coil.z.current())
    csb.coil.z.current(float(l))  # mA





Output_btn=Button(root, text="X_Current_output from input", command=on_click_X).pack(side=LEFT)

Output_btn=Button(root, text="Y_Current_output from input", command=on_click_Y).pack(side=LEFT)

Output_btn=Button(root, text="Z_Current_output from input", command=on_click_Z).pack(side=LEFT)



quit_btn = Button(root, text='QUIT', command=root.quit,anchor='s')
quit_btn.pack()



mainloop()



