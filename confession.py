import tkinter as tk 
from tkinter import ttk
import random
from customtkinter import *
from PIL import Image,ImageTk

#window
window=CTk()
window.geometry('1000x500')
window.title('Confession.exe')
set_appearance_mode('dark')

label=CTkLabel(window, text='Would you go out on a date with me?', fg_color='transparent', font=('helvetica',20))
label.pack(pady=50)

def press(): 
    label.configure(text="I didn't think this far ahead...")
    
    btn.place_forget()
    btn2.place_forget()
    
    label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    
    window.after(1500,window.destroy)

def button_hover(e):
    window.after(0)
    but_pos_x=random.randint(50,950)
    but_pos_y=random.randint(50,450)
    btn.place_configure(x=but_pos_x,y=but_pos_y)

#widgets
btn=CTkButton(
    master=window, 
    text='No',
    font=('Comic Sans',16),
    text_color='#000000',
    corner_radius=32, 
    fg_color='#eea990',
    border_color='#66545e',
    border_width=2,    
    )
    
btn2=CTkButton(
    master=window, 
    text='Yes',
    font=('Comic Sans',16),
    text_color='#000000',
    corner_radius=32, 
    fg_color='#eea990',
    border_color='#66545e',
    border_width=2,
    command=press    
    )
    
btn.place(x=600,y=350,anchor=tk.CENTER)
btn2.place(x=400,y=350,anchor=tk.CENTER)
btn.bind("<Enter>",button_hover)


#run
window.mainloop()