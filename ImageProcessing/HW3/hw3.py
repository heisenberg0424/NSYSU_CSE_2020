import tkinter
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
from PIL import Image,ImageTk
from PIL import ImageEnhance
import math
#Functions
def hilo(a, b, c):
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c
def complement(r, g, b):
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))
def complement_btn_func():
    global temp,mod

    size = mod.size
    mode = mod.mode
    data = mod.getdata()

    temp = Image.new(mode, size)
    temp.putdata([complement(*rgb) for rgb in data])
    refresh()

def load_btn_func():
    global load,temp,mod
    load=Image.open('Lenna_512_color.tif') #open image
    load=load.resize((300,300))
    origin_image=ImageTk.PhotoImage(load) #show original picture in label
    origin_image_lbl.config(image=origin_image,width=300,height = 300)
    mod=load.copy()    #copy image for modifying
    modify_image=ImageTk.PhotoImage(mod) #show modify image
    modify_image_lbl.config(image=modify_image,width=300,height=300)
    origin_image_lbl.Image=origin_image
    modify_image_lbl.Image=modify_image
    temp=load.copy()   

def refresh():
    global temp
    modify_image=ImageTk.PhotoImage(temp) #refresh pic
    modify_image_lbl.config(image=modify_image,width=300,height=300)
    modify_image_lbl.Image=modify_image

def red_btn_func():
    global mod,temp
    data = mod.getdata()
    r = [(d[0], 0, 0) for d in data]
    temp.putdata(r)
    refresh()
def green_btn_func():
    global mod,temp
    data = mod.getdata()
    r = [(0, d[1], 0) for d in data]
    temp.putdata(r)
    refresh()
def blue_btn_func():
    global mod,temp
    data = mod.getdata()
    r = [(0, 0, d[2]) for d in data]
    temp.putdata(r)
    refresh()

def hue_btn_func():
    global mod, temp
    mod_array=np.asarray(mod)
    HSI=np.zeros([300, 300])
    for i in range(300):
        for j in range(300):
            r, g, b=mod_array[i][j]
            r/=255; g/=255; b/=255
            up=0.5*((r-g)+(r-b))
            down=math.sqrt(pow((r-g),2)+(r-b)*(g-b))
            theta=np.arccos(up/down)/3.14*180
            if b<=g: 
                HSI[i][j]=theta
            else: 
                HSI[i][j]=360-theta
    HSI=HSI/360*255
    temp = Image.fromarray(np.uint8(HSI),'L')
    refresh()
def saturation_btn_func():
    global mod, temp
    mod_array=np.asarray(mod)
    HSI=np.zeros([300, 300])
    for i in range(300):
        for j in range(300):
            r, g, b=mod_array[i][j]
            r=int(r);g=int(g);b=int(b)
            sum=r+g+b
            if (sum==0):
                HSI[i][j]=1
            else:
                HSI[i][j]=1-3/sum*min(r,g,b)
    HSI*=255
    temp = Image.fromarray(np.uint8(HSI),'L')
    refresh()
def intensity_btn_func():
    global mod, temp
    mod_array=np.asarray(mod)
    HSI=np.zeros([300, 300])
    for i in range(300):
        for j in range(300):
            r, g, b=mod_array[i][j]
            r=int(r);g=int(g);b=int(b)
            sum=r+g+b
            HSI[i][j]=sum/3
    temp = Image.fromarray(np.uint8(HSI),'L')
    refresh()


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

#Button
load_btn=tkinter.Button(window,text='LOAD',command=load_btn_func)
red_btn=tkinter.Button(window,text='RED',command=red_btn_func)
blue_btn=tkinter.Button(window,text='BLUE',command=blue_btn_func)
green_btn=tkinter.Button(window,text='GREEN',command=green_btn_func)
complement_btn=tkinter.Button(window,text='Complement',command=complement_btn_func)
hue_btn=tkinter.Button(window,text='H',command=hue_btn_func)
saturation_btn=tkinter.Button(window,text='S',command=saturation_btn_func)
intensity_btn=tkinter.Button(window,text='I',command=intensity_btn_func)
#Listbox

#Pack
origin_image_lbl.place(relx=0.3,rely=0.02)
modify_image_lbl.place(relx=0.6,rely=0.02)
load_btn.place(relx=0.1,rely=0.1)
red_btn.place(relx=0.02,rely=0.2)
blue_btn.place(relx=0.1,rely=0.2)
green_btn.place(relx=0.19,rely=0.2)
complement_btn.place(relx=0.07,rely=0.3)
hue_btn.place(relx=0.02,rely=0.4)
saturation_btn.place(relx=0.1,rely=0.4)
intensity_btn.place(relx=0.19,rely=0.4)
window.mainloop()