import tkinter
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance
#window setting
window = tkinter.Tk()
window.title('DIP HW1')
window.geometry('500*500')

#IMGlabel
origin_image_lbl=tkinter.Label(window,image=origin_image,width=300, height = 300)
origin_image=ImageTk.PhotoImage(load)
load=Image.open('test.jpg')

#Pack
origin_image_lbl.pack()

window.mainloop()