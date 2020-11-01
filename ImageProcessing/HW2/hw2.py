import tkinter
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from PIL import ImageEnhance
import math
# Functions


def load_btn_func():
    global mod, temp
    slice_flag=0
    openfile = fd.askopenfilename(title='open file')  # select file
    load = Image.open('elaine.512.tiff')  # open image
    load = load.convert('L')  # convert to gray scale
    load = load.resize((300,300))
    origin_image = ImageTk.PhotoImage(load)  # show original picture in label
    origin_image_lbl.config(image=origin_image, width=300, height=300)
    mod = load.copy()  # copy image for modifying
    modify_image = ImageTk.PhotoImage(mod)  # show modify image
    modify_image_lbl.config(image=modify_image, width=300, height=300)
    origin_image_lbl.Image = origin_image
    modify_image_lbl.Image = modify_image
    temp = load.copy()


def save_btn_func():
    global temp, mod
    mod = temp
    mod = mod.save('output.jpg')  # save file


def slicing_func():
    global temp,mod,slice_flag
    range_min,range_max=entry_output.get().split('-')
    range_min=int(range_min)
    range_max=int(range_max)
    I = np.asarray(mod)
    x, y = I.shape
    z = np.zeros((x, y))
    for i in range(0, x):
        for j in range(0, y):
            if(I[i][j] > range_min and I[i][j] < range_max):
                z[i][j] = 255
            else:
                if modeselect.get():
                    z[i][j]=I[i][j]
                else:
                    z[i][j] = 0
    temp = Image.fromarray(np.uint8(z))
    refresh()
    slice_flag=1

def refresh():
    global temp
    modify_image = ImageTk.PhotoImage(temp)  # refresh pic
    modify_image_lbl.config(image=modify_image, width=300, height=300)
    modify_image_lbl.Image = modify_image


# window setting
window = tkinter.Tk()
window.title('DIP HW1')
window.geometry('1280x720')
icon = ImageTk.PhotoImage(file="ICON.ico")
window.tk.call('wm', 'iconphoto', window._w, icon)
# IMGlabel


origin_image_lbl = tkinter.Label(window)
modify_image_lbl = tkinter.Label(window)

# text import
entry_label = tkinter.Label(window, text='Enter Range: E.g. 10-213')
entry_output = tkinter.StringVar()
slicing_entry = tkinter.Entry(window, textvariable=entry_output, width=7)


# Scale


# Button
load_btn = tkinter.Button(window, text='LOAD', command=load_btn_func)
save_btn = tkinter.Button(window, text='SAVE', command=save_btn_func)
refresh_btn = tkinter.Button(window, text='Apply', command=slicing_func)
# Listbox
modeselect=tkinter.IntVar()
black_btn=tkinter.Radiobutton(window, text='Black',variable=modeselect, value=0)
original_btn=tkinter.Radiobutton(window, text='Original',variable=modeselect, value=1)

# Pack
origin_image_lbl.place(relx=0.3, rely=0.02)
modify_image_lbl.place(relx=0.6, rely=0.02)
load_btn.place(relx=0.1, rely=0.1)
save_btn.place(relx=0.1, rely=0.2)
entry_label.place(relx=0.4, rely=0.5)
slicing_entry.place(relx=0.4, rely=0.56)
black_btn.place(relx=0.6,rely=0.56)
original_btn.place(relx=0.7,rely=0.56)
refresh_btn.place(relx=0.5, rely=0.55)
window.mainloop()
