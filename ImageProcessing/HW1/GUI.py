import tkinter
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
from PIL import ImageEnhance
#Functions
def load_btn_func():
    origin_image_lbl.config(image=origin_image,width=300, height = 300)

#window setting
window = tkinter.Tk()
window.title('DIP HW1')
window.geometry('1280x720')

#IMGlabel
load=Image.open('test.jpg')
origin_image=ImageTk.PhotoImage(load)
origin_image_lbl=tkinter.Label(window)


#Button
load_btn=tkinter.Button(window,text='LOAD',command=load_btn_func)

#Pack
origin_image_lbl.place(relx=0.3,rely=0.02)
load_btn.place(relx=0.1,rely=0.1)

window.mainloop()