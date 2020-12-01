import tkinter
import cv2
import numpy as np
from PIL import Image,ImageTk,ImageFilter
from PIL import ImageEnhance
import math
import PIL.ImageOps
from time import sleep
#Functions
def complement_btn_func():
    global temp,mod
    temp = PIL.ImageOps.invert(mod) #invert the color
    refresh()

def load_btn_func():
    global load,temp,mod,HSI_arr
    HSI_arr=np.zeros([300,300,3])
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
    data = mod.getdata()    #extract color
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
    global mod, temp, HSI_arr
    mod_array=np.asarray(mod)
    HSI=np.zeros([300, 300])    #new array
    for i in range(300):
        for j in range(300):
            r, g, b=mod_array[i][j] #convert to HSI
            r/=255; g/=255; b/=255
            up=0.5*((r-g)+(r-b))
            down=math.sqrt(pow((r-g),2)+(r-b)*(g-b))
            theta=np.arccos(up/down)/3.14*180
            if b<=g: 
                HSI[i][j]=theta 
                HSI_arr[i][j][0]=theta/360*255 #copy to HSI_arr for further use
            else: 
                HSI[i][j]=360-theta
                HSI_arr[i][j][0]=(360-theta)/360*255
    HSI=HSI/360*255 #convert to 0-255
    temp = Image.fromarray(np.uint8(HSI),'L') #show image
    refresh()
def saturation_btn_func():
    global mod, temp, HSI_arr
    mod_array=np.asarray(mod)   #convert to array
    HSI=np.zeros([300, 300])
    for i in range(300):
        for j in range(300):
            r, g, b=mod_array[i][j]
            r=int(r);g=int(g);b=int(b)
            sum=r+g+b
            if (sum==0):
                HSI[i][j]=1
                HSI_arr[i][j][1]=255    #copy value to HSI_array for furture use
            else:
                HSI[i][j]=1-3/sum*min(r,g,b)
                HSI_arr[i][j][1]=(1-3/sum*min(r,g,b))*255
    HSI*=255    #convert to 0-255

    temp = Image.fromarray(np.uint8(HSI),'L')
    refresh()
def intensity_btn_func():
    global mod, temp, HSI_arr   #average 
    mod_array=np.asarray(mod)
    HSI=np.zeros([300, 300])
    for i in range(300):
        for j in range(300):
            r, g, b=mod_array[i][j]
            r=int(r);g=int(g);b=int(b)
            sum=r+g+b
            HSI[i][j]=sum/3
            HSI_arr[i][j][2]=sum/3
    temp = Image.fromarray(np.uint8(HSI),'L')
    refresh()

def smoothing_btn_func():
    global temp,mod,HSI_arr
    if(mode.get()==1):  #HSI
        temp=Image.fromarray(np.uint8(HSI_arr))
    else:
        temp=mod #RGB
    temp = temp.filter(ImageFilter.Kernel((5,5),(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))) #kernel
    refresh()
def sharpen_btn_func():
    global temp,mod
    if(mode.get()==1):  #HSI
        temp=Image.fromarray(np.uint8(HSI_arr))
    else:
        temp=mod    #RGB
    temp = temp.filter(ImageFilter.Kernel((3,3),(-1,-1,-1,-1,9,-1,-1,-1,-1))) #Kernel
    refresh()

def feather1_btn_func():
    global temp,mod,HSI_arr,tt
    tt=np.zeros([300,300,3])
    temp=np.asarray(mod)
    for i in range(300):
        for j in range(300):
            if HSI_arr[i][j][0]>120 and HSI_arr[i][j][0]<224: #only show pixel that hue in range (120,224)
                tt[i][j]=temp[i][j]
    temp=Image.fromarray(np.uint8(tt))
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


#Radiobutton
mode=tkinter.IntVar()
rgb_radio=tkinter.Radiobutton(window,text='RGB',variable=mode,value=0)
hsi_radio=tkinter.Radiobutton(window,text='HSI',variable=mode,value=1)

#Button
load_btn=tkinter.Button(window,text='LOAD',command=load_btn_func)
red_btn=tkinter.Button(window,text='RED',command=red_btn_func)
blue_btn=tkinter.Button(window,text='BLUE',command=blue_btn_func)
green_btn=tkinter.Button(window,text='GREEN',command=green_btn_func)
complement_btn=tkinter.Button(window,text='Complement',command=complement_btn_func)
hue_btn=tkinter.Button(window,text='H',command=hue_btn_func)
saturation_btn=tkinter.Button(window,text='S',command=saturation_btn_func)
intensity_btn=tkinter.Button(window,text='I',command=intensity_btn_func)
smoothing_btn=tkinter.Button(window,text='Smooth',command=smoothing_btn_func)
sharpen_btn=tkinter.Button(window,text='Sharpen',command=sharpen_btn_func)
feather1_btn=tkinter.Button(window,text='Feather',command=feather1_btn_func)
#feather2_btn=tkinter.Button(window,text='Step 2',command=feather2_btn_func)
#Listbox

#Pack
origin_image_lbl.place(relx=0.3,rely=0.02)
modify_image_lbl.place(relx=0.6,rely=0.02)
load_btn.place(relx=0.1,rely=0.1)
red_btn.place(relx=0.02,rely=0.2)
blue_btn.place(relx=0.1,rely=0.2)
green_btn.place(relx=0.19,rely=0.2)
complement_btn.place(relx=0.07,rely=0.3)
hue_btn.place(relx=0.06,rely=0.4)
saturation_btn.place(relx=0.12,rely=0.4)
intensity_btn.place(relx=0.18,rely=0.4)
rgb_radio.place(relx=0.02,rely=0.5)
smoothing_btn.place(relx=0.15,rely=0.49)
hsi_radio.place(relx=0.02,rely=0.6)
sharpen_btn.place(relx=0.15,rely=0.59)
feather1_btn.place(relx=0.1,rely=0.7)
#feather2_btn.place(relx=0.1,rely=0.8)
window.mainloop()
