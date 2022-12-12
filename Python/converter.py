#Variables ending in 'a' mean they are the answer variable
#Variables ending in 'f' mean they are the frame variable
#Variables ending in 'e' mean they are the entry box variable





""" ---! MODULES !--- """
from tkinter import *


""" ---! FUNCTIONS !--- """
#quicker and neater way of pulling frames
def raise_frame(frame):
    frame.tkraise()

#simple conversions for the convert buttons
def bittobyte():
  bits = bittobytea.get()
  ans = bits * 0.125
  answer = Label(bittobytef, text=ans).pack()
  bits = ""

def bittokilobyte():
  bits = bittokilobytea.get()
  ans = bits * 0.000125
  answer = Label(bittokilobytef, text=ans).pack()
  bits = ""

def bittomegabyte():
  bits = bittomegabytea.get()
  ans = bits * 0.000000125
  answer = Label(bittomegabytef, text=ans).pack()
  bits = ""

def bittogigabyte():
  bits = bittogigabytea.get()
  ans = bits * 0.000000000125
  answer = Label(bittogigabytef, text=ans).pack()
  bits = ""


""" ---! VARIABLES !--- """
#all of the variables that aren't in a function are here
root = Tk()
home = Frame(root)

bittobytef = Frame(root)
bittobytea = IntVar()

bittokilobytef = Frame(root)
bittokilobytea = IntVar()

bittomegabytef = Frame(root)
bittomegabytea = IntVar()

bittogigabytef = Frame(root)
bittogigabytea = IntVar()


""" ---! GUI !--- """
for frame in (home, bittobytef, bittokilobytef, bittomegabytef, bittogigabytef):
    frame.grid(row=0, column=0, sticky='news')


""" --- Home Frame --- """
Label(home, text='Home').pack()
Button(home, text='Bit to Byte', command=lambda:raise_frame(bittobytef)).pack()
Button(home, text='Bit to Kilobyte', command=lambda:raise_frame(bittokilobytef)).pack()
Button(home, text='Bit to Megabyte', command=lambda:raise_frame(bittomegabytef)).pack()
Button(home, text='Bit to Gigabyte', command=lambda:raise_frame(bittogigabytef)).pack()


""" --- Bit To Byte Frame --- """
Label(bittobytef, text='Bit to Byte').pack()
bittobytee = Entry(bittobytef, textvariable= bittobytea, width='15').pack()
Button(bittobytef, text='Convert', command=bittobyte).pack()
Button(bittobytef, text='Back', command=lambda:raise_frame(home)).pack()


""" --- Bit To Kilobyte Frame --- """
Label(bittokilobytef, text='Bit to Kilobyte').pack()
bittokilobytee = Entry(bittokilobytef, textvariable=bittokilobytea, width='15').pack()
Button(bittokilobytef, text='Convert', command=bittokilobyte).pack()
Button(bittokilobytef, text='Back', command=lambda:raise_frame(home)).pack()


""" --- Bit To Megabyte Frame --- """
Label(bittomegabytef, text='Bit to Megabyte').pack()
bittomegabytee = Entry(bittomegabytef, textvariable=bittomegabytea, width='15').pack()
Button(bittomegabytef, text='Convert', command=bittomegabyte).pack()
Button(bittomegabytef, text='Back', command=lambda:raise_frame(home)).pack()


""" --- Bit To Gigabyte Frame --- """
Label(bittogigabytef, text='Bit to Gigabyte').pack()
bittogigabytee = Entry(bittogigabytef, textvariable=bittogigabytea, width='15').pack()
Button(bittogigabytef, text='Convert', command=bittogigabyte).pack()
Button(bittogigabytef, text='Back', command=lambda:raise_frame(home)).pack()


raise_frame(home)
root.mainloop()