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
    zoom_flag=rotate_flag=a_flag=b_flag=a=b=0    #initialize
    openfile=fd.askopenfilename(title='open file',filetypes=(('jepg file','*.jpg'),('tif file','*.tif'))) #select file
    load=Image.open(openfile) #open image
    load=load.convert('L')    #convert to gray scale
    origin_image=ImageTk.PhotoImage(load) #show original picture in label
    origin_image_lbl.config(image=origin_image,width=300,height = 300)
    mod=load.copy()    #copy image for modifying
    modify_image=ImageTk.PhotoImage(mod) #show modify image
    modify_image_lbl.config(image=modify_image,width=300,height=300)
    origin_image_lbl.Image=origin_image
    modify_image_lbl.Image=modify_image
    temp=load.copy()   
def histogram_func():
    global mod, temp 
    mod=temp       #refresh mod pic
    array=np.asarray(mod) #convert to nparray
    hist=[0]*256
    hist=np.array(hist)  #count value
    for x in range(array.shape[0]):
        for y in range (array.shape[1]):
            i = array[x,y]
            hist[i]=hist[i]+1
    plt.clf() #clear plot
    plt.plot(hist,color='darkgrey') #show plot
    plt.axis('off')
    plt.savefig('foo.png')    #save plot to image
    histo=Image.open('foo.png') #open in label
    histo=histo.resize((300,300))
    hist_image=ImageTk.PhotoImage(histo)
    histogram_lbl.config(image=hist_image,width=300,height = 300)
    histogram_lbl.Image=hist_image
def equalize_btn_func():
    global mod, temp
    mod=temp    #refresh
    cvimg=np.array(mod) #transfer from pil to cv2
    eq = cv2.equalizeHist(cvimg)   #equalize
    mod = temp =Image.fromarray(cv2.cvtColor(eq,cv2.COLOR_BGR2RGB)) #save cv2 to pil 
    refresh()
def save_btn_func():
    global temp, mod
    mod=temp
    mod=mod.save('output.jpg') #save file

def selection_output_a(tempa):
    global mod, temp, zoom_flag, rotate_flag, a, b, a_flag, b_flag
    if zoom_flag or rotate_flag or b_flag: #if things changed before
        mod=temp
        zoom_flag=rotate_flag=b_flag=0
    tempa=float(tempa) #str -> float
    a=tempa
    if modeselect.get()==0: #linear
        Y=a*1+b
    if modeselect.get()==1: #exp
        Y=math.exp(a*1+b)
    if modeselect.get()==2: #ln
        if b<1: b=1
        Y=math.log(a*1+b)
    if select.get()==0: #Brightness or Contrast 
        temp=ImageEnhance.Brightness(mod).enhance(Y)
    else:
        temp=ImageEnhance.Contrast(mod).enhance(Y)
    refresh()

    a_flag=1
def selection_output_b(tempb):
    global mod, temp, zoom_flag, rotate_flag, a, b, a_flag, b_flag
    if zoom_flag or rotate_flag or a_flag:
        mod=temp
        zoom_flag=rotate_flag=a_flag=0
    tempb=float(tempb) #str->float
    b=tempb
    if modeselect.get()==0: #same as selection_output_b
        Y=a*1+b
    if modeselect.get()==1:
        Y=math.exp(a*1+b)
    if modeselect.get()==2:
        if b<1: b=1
        Y=math.log(a*1+b)
    if select.get()==0:
        temp=ImageEnhance.Brightness(mod).enhance(Y)
    else:
        temp=ImageEnhance.Contrast(mod).enhance(Y)
    refresh()
    b_flag=1
def selection_output_zoom(zoom):
    global mod, temp, zoom_flag,rotate_flag, a_flag, b_flag
    if rotate_flag or a_flag or b_flag : #if modify before
        mod=temp
        rotate_flag=a_flag=b_flag=0
        slider_rotate.set(0)
    zoom=float(zoom)
    zoom=2**zoom #cal new picture width height
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
        
    temp=mod.rotate(int(rotate)) #rotate pic
    refresh()
    rotate_flag=1

def refresh():
    global temp
    modify_image=ImageTk.PhotoImage(temp) #refresh pic
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
histogram_lbl=tkinter.Label(window)


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
save_btn=tkinter.Button(window,text='SAVE',command=save_btn_func)
histogram_btn=tkinter.Button(window,text='Histogram',command=histogram_func)
equalize_btn=tkinter.Button(window,text='Equalize',command=equalize_btn_func)
#Listbox
modeselect=tkinter.IntVar()
select=tkinter.IntVar()
r1 = tkinter.Radiobutton(window, text='Linearly',variable=modeselect, value=0)
r2 = tkinter.Radiobutton(window, text='Exponentially',variable=modeselect, value=1)
r3 = tkinter.Radiobutton(window, text='Logarithmically',variable=modeselect, value=2)
r4 = tkinter.Radiobutton(window, text='Brightness',variable=select, value=0)
r5 = tkinter.Radiobutton(window, text='Contrast',variable=select, value=1)

#Pack
origin_image_lbl.place(relx=0.3,rely=0.02)
modify_image_lbl.place(relx=0.6,rely=0.02)
histogram_lbl.place(relx=0.7,rely=0.5)
load_btn.place(relx=0.1,rely=0.1)
save_btn.place(relx=0.1,rely=0.2)
r1.place(relx=0.05,rely=0.5)
r2.place(relx=0.05,rely=0.6)
r3.place(relx=0.05,rely=0.7)
r4.place(relx=0.05,rely=0.3)
r5.place(relx=0.05,rely=0.4)
slider_a.place(relx=0.3,rely=0.5)
slider_b.place(relx=0.3,rely=0.6)
slider_zoom.place(relx=0.3,rely=0.7)
slider_rotate.place(relx=0.3,rely=0.8)
histogram_btn.place(relx=0.05,rely=0.8)
equalize_btn.place(relx=0.05,rely=0.9)
window.mainloop()