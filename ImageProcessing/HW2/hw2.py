import tkinter
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from PIL import ImageEnhance,ImageFilter
import math
# Functions


def load_btn_func():
    global mod, temp, reset_image
    openfile = fd.askopenfilename(title='open file')  # select file
    load = Image.open(openfile)  # open image
    load = load.convert('L')  # convert to gray scale
    load = load.resize((300,300))
    origin_image = ImageTk.PhotoImage(load)  # show original picture in label
    origin_image_lbl.config(image=origin_image, width=300, height=300)
    mod = load.copy()  # copy image for modifying
    modify_image = ImageTk.PhotoImage(mod)  # show modify image
    modify_image_lbl.config(image=modify_image, width=300, height=300)
    origin_image_lbl.Image = origin_image
    modify_image_lbl.Image = modify_image
    temp=reset_image = load.copy()

def save_btn_func():
    global temp, mod
    mod = temp
    mod = mod.convert("L")
    mod = mod.save('output.jpg')  # save file

def slicing_func():
    global temp,mod
    range_min,range_max=entry_output.get().split('-')   #get input val and convert 2 int
    range_min=int(range_min)
    range_max=int(range_max)
    I = np.asarray(mod)
    x, y = I.shape
    z = np.zeros((x, y))    #new array
    for i in range(0, x):       #if in range, set to 255(white)
        for j in range(0, y):
            if(I[i][j] > range_min and I[i][j] < range_max):
                z[i][j] = 255
            else:
                if modeselect.get():    #preserve original color or black selected by user
                    z[i][j]=I[i][j]
                else:
                    z[i][j] = 0
    temp = Image.fromarray(np.uint8(z)) #convert to PIL
    refresh()

def bitplane_func():
    global temp,mod
    #Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
    lst = []
    I = np.asarray(mod)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
          lst.append(np.binary_repr(I[i][j] ,width=8)) # width = no. of bits
    j=bitselect.get()-1
    bit=(np.array([int(i[7-j]) for i in lst],dtype = np.uint8) * 255).reshape(I.shape[0],I.shape[1])
    
    temp = Image.fromarray(bit)
    refresh()

def reset_func():
    global temp,mod,reset_image #reset right IMG to original one
    temp=reset_image.copy()
    refresh()

def smooth_func(val):
    global mod,temp
    val=int(val)
    temptemp=mod.copy() #iterate times
    for i in range(val) :
        temptemp=temptemp.filter(ImageFilter.Kernel((3, 3), (1,2,1,2,4,2,1,2,1))) #filter
    temp=temptemp
    refresh()

def sharp_func(val):
    global mod,temp
    val=int(val)
    temptemp=mod.copy() #same as sharp func
    for i in range(val) :
        temptemp=temptemp.filter(ImageFilter.Kernel((3, 3), (0,-1,0,-1,5,-1,0,-1,0)))
    temp=temptemp
    refresh()

def refresh():
    global temp
    modify_image = ImageTk.PhotoImage(temp)  # refresh pic
    modify_image_lbl.config(image=modify_image, width=300, height=300)
    modify_image_lbl.Image = modify_image

def fft_func():
    global temp,mod
    #openCVim = np.array(PILim)
    #PILim = Image.fromarray(openCVim)
    f = np.array(mod)
    f = np.fft.fft2(f)  #Do fft
    fshift = np.fft.fftshift(f)
    temp = 20*np.log(np.abs(fshift))
    temp=Image.fromarray(temp)
    refresh()

def revfft_func():
    global temp,mod
    #pic=np.array(mod)
    ap=np.fft.fft2(mod)
    apshift=np.fft.fftshift(ap)            #fft first
    As=np.fft.ifftshift(np.abs(apshift))    #Amplitude
    A=np.fft.ifft2(As)                #shift and invert
    A=np.abs(A)         
    temp=Image.fromarray(A)
    refresh()

def homo_func():
    global temp,mod
    r1,rh,c,d0=entry2_output.get().split(',') #input val as parameters
    r1=float(r1)
    rh=float(rh)
    c=float(c)
    d0=float(d0)
    h = 2.0; l = 0.5
    gray=np.asarray(mod)    #cvt
    rows,cols=gray.shape    #shape
    gray_dft = np.fft.fft2(gray)    #do dft
    gray_dftshift = np.fft.fftshift(gray_dft)
    dst_dftshift = np.zeros_like(gray_dftshift)
    M, N = np.meshgrid(np.arange(-cols // 2, cols // 2), np.arange(-rows//2, rows//2))
    D = np.sqrt(M ** 2 + N ** 2)
    Z = (rh - r1) * (1 - np.exp(-c * (D ** 2 / d0 ** 2))) + r1
    dst_dftshift = Z * gray_dftshift
    dst_dftshift = (h - l) * dst_dftshift + l
    dst_idftshift = np.fft.ifftshift(dst_dftshift)
    dst_idft = np.fft.ifft2(dst_idftshift)
    dst = np.real(dst_idft)
    dst = np.uint8(np.clip(dst, 0, 255))
    temp = Image.fromarray(dst)
    refresh()
# window setting
window = tkinter.Tk()
window.title('DIP HW2')
window.geometry('1280x720')
icon = ImageTk.PhotoImage(file="ICON.ico")
window.tk.call('wm', 'iconphoto', window._w, icon)
# IMGlabel
origin_image_lbl = tkinter.Label(window)
modify_image_lbl = tkinter.Label(window)

# text import
entry_label = tkinter.Label(window, text='Enter Range: E.g. 10-213')
entry2_label = tkinter.Label(window, text='Enter yL,yH,c,D0\nE.g.:0.4,3.0,5,20')
entry_output = tkinter.StringVar()
slicing_entry = tkinter.Entry(window, textvariable=entry_output, width=7)
entry2_output = tkinter.StringVar()
par_entry = tkinter.Entry(window, textvariable=entry2_output, width=10)


# Scale
slider_smooth = tkinter.Scale(window, from_=0, to=20, orient=tkinter.HORIZONTAL,\
    length=300, showvalue=0, resolution=1, command=smooth_func,label='Smooth')
slider_sharp = tkinter.Scale(window, from_=0, to=5, orient=tkinter.HORIZONTAL,\
    length=300, showvalue=0, resolution=1, command=sharp_func,label='Sharp')

# Button
load_btn = tkinter.Button(window, text='LOAD', command=load_btn_func)
save_btn = tkinter.Button(window, text='SAVE', command=save_btn_func)
reset_btn=tkinter.Button(window,text='RESET',command=reset_func)
refresh_btn = tkinter.Button(window, text='Apply', command=slicing_func)
bitplane_btn = tkinter.Button(window, text='bit plane image',command= bitplane_func)
fft_btn=tkinter.Button(window,text='FFT',command=fft_func)
refft_btn=tkinter.Button(window,text='Amplitude',command=revfft_func)
homo_btn=tkinter.Button(window,text='Homomorphic',command=homo_func)
# Option menu
bitselect=tkinter.IntVar()
bit_menu=tkinter.OptionMenu(window,bitselect,1,2,3,4,5,6,7,8)

# Radiobutton
modeselect=tkinter.IntVar()
black_btn=tkinter.Radiobutton(window, text='Black',variable=modeselect, value=0)
original_btn=tkinter.Radiobutton(window, text='Original',variable=modeselect, value=1)

# Pack
origin_image_lbl.place(relx=0.3, rely=0.02)
modify_image_lbl.place(relx=0.6, rely=0.02)
load_btn.place(relx=0.05, rely=0.1)
save_btn.place(relx=0.05, rely=0.2)
reset_btn.place(relx=0.05,rely=0.3)
fft_btn.place(relx=0.05,rely=0.4)
refft_btn.place(relx=0.05,rely=0.5)
entry2_label.place(relx=0.05,rely=0.8)
par_entry.place(relx=0.05,rely=0.9)
homo_btn.place(relx=0.2,rely=0.9)
entry_label.place(relx=0.3, rely=0.5)
slicing_entry.place(relx=0.3, rely=0.56)
black_btn.place(relx=0.5,rely=0.56)
original_btn.place(relx=0.6,rely=0.56)
refresh_btn.place(relx=0.4, rely=0.55)
bit_menu.place(relx=0.3,rely=0.65)
bitplane_btn.place(relx=0.35,rely=0.65)
slider_smooth.place(relx=0.25,rely=0.75)
slider_sharp.place(relx=0.5,rely=0.75)

window.mainloop()
