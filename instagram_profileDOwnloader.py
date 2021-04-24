from tkinter import *
import instaloader
from PIL import ImageTk,Image
import os
import glob
import time
from tkinter import messagebox
from instaloader.exceptions import InstaloaderException

root=Tk()
root.title("Instagram Profile Downloader--BY SARTHAK PATEL")
root.geometry("460x670")
root.resizable(False,False)
#LOGO
img1=Image.open("F:\\logo instagram.jpg")
resized1 = img1.resize((100,100), Image.ANTIALIAS)
new_img=ImageTk.PhotoImage(resized1)
my_label=Label(image=new_img)
my_label.pack(padx=5)

#TITLE
img2=Image.open("F:\\instagram.png")
resized2 = img2.resize((160,70), Image.ANTIALIAS)
new_img1=ImageTk.PhotoImage(resized2)
label1=Label(image=new_img1)
label1.pack()

label2=Label(root,text="ENTER INSTAGRAM USERNAME BELOW",font=("Georgia",15),fg="White",bg="#3053a2")
label2.pack(fill=BOTH)

box=Entry(root,width=40,font=("Georgia",15),borderwidth=4)
box.pack(ipady=10)


img3=ImageTk.PhotoImage(Image.open("F:\\scanner.png"))
label3=Label(root,image=img3)
label3.pack()


def function():
    global img3,label2,label3  
    text=box.get()
    print(text)
    get=instaloader.Instaloader()

    try: 
        get.download_profile(text,profile_pic_only=True) 
        a=glob.glob("C:\\Instagram Profile Downloader\\"+str(text)+"\*.jpg")
        path1=a[0]
        print(path1)
        label3.pack_forget()
        img3=ImageTk.PhotoImage(Image.open(str(path1)))
        label3=Label(root,image=img3)
        label3.pack()
        mylist.insert(END,text)
    except InstaloaderException as error:
        messagebox.showerror("Error Detected", error) 
       
    
    
button_1=Button(root,text="DOWLOAD NOW",width=30,font=("Georgia",20),fg="Black",bg="#399973",borderwidth=4,command=function)
button_1.pack()

global mylist
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set ,bg="lightgrey")
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

def get():
    global label3,img3
    label3.pack_forget()
    x=mylist.get(ACTIVE)
    a=glob.glob("C:\\Instagram Profile Downloader\\"+str(x)+"\*.jpg")
    path2=a[0]
    img3=ImageTk.PhotoImage(Image.open(str(path2)))
    label3=Label(root,image=img3)
    label3.pack()
    
view_button=Button(root,text="VIEW SELECTED",width=25,font=("Georgia",15),fg="black",bg="#0098d2",borderwidth=4,command=get)
view_button.pack(side=BOTTOM)

 

directory = "Instagram Profile Downloader"
parent_dir = "C:/"
path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path) 
except OSError as error: 
    pass


os.chdir("C:/Instagram Profile Downloader")
    
root.mainloop()
