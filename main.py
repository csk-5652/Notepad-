# Importing the tkinter module 
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os 




# defining  the function here
def New_file():
    global file
    root.title("untitled-Notepad")
    file=None
    textarea.delete(1.0, END)

def OPen_file():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+' - Notepad')
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
    
    
        

def save_file():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+' - Notepad')
            print("Your file is saved")
     
    else:
         f=open(file,"w")
         f.write(textarea.get(1.0,END))
         f.close()
                

def quit_application():
    root.destroy()

def cut():
    textarea.event_generate(("<<cut>>"))

def copy():
    textarea.event_generate(("<<copy>>"))

def paste():
    textarea.event_generate(("<<paste>>"))

def about_notepad():
    showinfo("Notepad","Notepad by csk ")




# main start 
if __name__ =='__main__':
    # basic tkinter setup 
    root=Tk()
    root.title("Notepad")
    # before uncommenting below line first you have to download .ico file then change name notes.ico to your img name
    # root.wm_iconbitmap('notes.ico')

    
    root.geometry("1280x768")
    
    # Add textarea 
    textarea=Text(root,font="lucida 13")
    file=None
    textarea.pack(expand=True,fill=BOTH)
    
    # lets create a menubar 
    menubar=Menu(root)
    
    # create a file menu 
    filemenu=Menu(menubar,tearoff=0)
    
    # To open a new file 
    filemenu.add_command(label="New",command=New_file)
    # To open a existing file   
    filemenu.add_command(label="Open",command=OPen_file)
    # To save a file 
    filemenu.add_command(label="Save as",command=save_file)
    # To create horizontal line  
    filemenu.add_separator()
    
    # To Exit window   
    filemenu.add_command(label="Exit",command=quit_application)
    

    menubar.add_cascade(label="File",menu=filemenu)
    # file menu end    
    
    # To create a Editmenu 
    editmenu=Menu(menubar,tearoff=0)
    
    # To cut the text  
    editmenu.add_command(label="Cut",command=cut())
    # To copy the text 
    editmenu.add_command(label="copy",command=copy())
    # To paste the copy text     
    editmenu.add_command(label="Paste",command=paste())
    
    
    
    menubar.add_cascade(label="Edit",menu=editmenu)
    # edit menu end 
    
    # To create a helpmneu 
    helpmenu=Menu(menubar,tearoff=0)
    
    helpmenu.add_command(label="About Notepad",command=about_notepad)
    
    menubar.add_cascade(label="Help",menu=helpmenu)
    # help menu end 
    
    root.config(menu=menubar)
    # menubar end   
    
    # adding scrolltext 
    
    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    
    # end    
    root.mainloop()



