import tkinter
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
from PIL import Image,ImageTk
from PIL import ImageEnhance
import math
#Functions
def load_btn_func():
    global mod,temp, zoom_flag,rotate_flag, a, b, a_flag, b_flag
    zoom_flag=rotate_flag=a_flag=b_flag=a=b=0
    openfile=fd.askopenfilename(title='open file',filetypes=(('jepg file','*.jpg'),('tif file','*.tif')))
    load=Image.open(openfile)
    load=load.convert('L')
    origin_image=ImageTk.PhotoImage(load)
    origin_image_lbl.config(image=origin_image,width=300,height = 300)
    mod=load.copy()
    modify_image=ImageTk.PhotoImage(mod)
    modify_image_lbl.config(image=modify_image,width=300,height=300)
    origin_image_lbl.Image=origin_image
    modify_image_lbl.Image=modify_image
    temp=load.copy()

def selection_output_a(tempa):
    global mod, temp, zoom_flag, rotate_flag, a, b, a_flag, b_flag
    if zoom_flag or rotate_flag:
        mod=temp
        zoom_flag=rotate_flag=0
    tempa=float(tempa)
    a=tempa
    if modeselect.get()==0:
        Y=a*1+b
    if modeselect.get()==1:
        Y=math.exp(a*1+b)
    if modeselect.get()==2:
        if b<1: b=1
        Y=math.log(a*1+b)
    
    temp=ImageEnhance.Brightness(mod).enhance(Y)
    refresh()

    b_flag=1

def selection_output_b(tempb):
    global mod, temp, zoom_flag, rotate_flag, a, b, a_flag, b_flag
    if zoom_flag or rotate_flag:
        mod=temp
        zoom_flag=rotate_flag=0
    tempb=float(tempb)
    b=tempb
    if modeselect.get()==0:
        Y=a*1+b
    if modeselect.get()==1:
        Y=math.exp(a*1+b)
    if modeselect.get()==2:
        if b<1: b=1
        Y=math.log(a*1+b)
    
    temp=ImageEnhance.Brightness(mod).enhance(Y)
    refresh()
    b_flag=1
def selection_output_zoom(zoom):
    global mod, temp, zoom_flag,rotate_flag, a_flag, b_flag
    if rotate_flag or a_flag or b_flag :
        mod=temp
        rotate_flag=a_flag=b_flag=0
        slider_rotate.set(0)
    zoom=float(zoom)
    zoom=2**zoom
    new_width=int(mod.width*zoom)
    new_height=int(mod.height*zoom)
    temp=mod.resize((new_width,new_height),Image.BILINEAR)
    refresh()
    zoom_flag=1
def selection_output_rotate(rotate):
    global mod,temp,zoom_flag,rotate_flag,a_flag,b_flag
    if zoom_flag or a_flag or b_flag:
        mod=temp
        zoom_flag=a_flag=b_flag=0
        
    temp=mod.rotate(int(rotate))
    refresh()
    rotate_flag=1

def refresh():
    global temp
    modify_image=ImageTk.PhotoImage(temp)
    modify_image_lbl.config(image=modify_image,width=300,height=300)
    modify_image_lbl.Image=modify_image
#window setting
window = tkinter.Tk()
window.title('DIP HW1')
window.geometry('1280x720')
icon = ImageTk.PhotoImage(file="ICON.ico")
window.tk.call('wm','iconphoto',window._w,icon)
#IMGlabel


origin_image_lbl=tkinter.Label(window)
modify_image_lbl=tkinter.Label(window)


#Scale
slider_a = tkinter.Scale(window, from_=0, to=10, orient=tkinter.HORIZONTAL,\
    length=400, showvalue=0, resolution=0.1, command=selection_output_a,label='a')
slider_b = tkinter.Scale(window, from_=0, to=10, orient=tkinter.HORIZONTAL,\
    length=400, showvalue=0, resolution=0.01, command=selection_output_b,label='b')
slider_zoom = tkinter.Scale(window, from_=-1, to=1, orient=tkinter.HORIZONTAL,\
    length=400, showvalue=0, resolution=0.05, command=selection_output_zoom,label='zoom')
slider_rotate = tkinter.Scale(window, from_=0, to=360, orient=tkinter.HORIZONTAL,\
    length=400, showvalue=0, resolution=5, command=selection_output_rotate,label='rotate')
slider_zoom.set(0)
slider_a.set(1)
slider_b.set(0)

#Button
load_btn=tkinter.Button(window,text='LOAD',command=load_btn_func)

#Listbox
modeselect=tkinter.IntVar()
r1 = tkinter.Radiobutton(window, text='Linearly',variable=modeselect, value=0)
r2 = tkinter.Radiobutton(window, text='Exponentially',variable=modeselect, value=1)
r3 = tkinter.Radiobutton(window, text='Logarithmically',variable=modeselect, value=2)

#Pack
origin_image_lbl.place(relx=0.3,rely=0.02)
modify_image_lbl.place(relx=0.6,rely=0.02)
load_btn.place(relx=0.1,rely=0.1)
r1.place(relx=0.05,rely=0.5)
r2.place(relx=0.05,rely=0.6)
r3.place(relx=0.05,rely=0.7)
slider_a.place(relx=0.3,rely=0.5)
slider_b.place(relx=0.3,rely=0.6)
slider_zoom.place(relx=0.3,rely=0.7)
slider_rotate.place(relx=0.3,rely=0.8)
window.mainloop()