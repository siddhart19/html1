from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("artist lab")
root.geometry("500x500")
root.maxsize=(650,650)
root.minsize=(650,650)
root.configure(background="lightblue")

run_icon = ImageTk.PhotoImage(Image.open ("run_file.png"))
save_icon = ImageTk.PhotoImage(Image.open ("save_file.png"))
open_icon = ImageTk.PhotoImage(Image.open ("open_file.png"))
file_name=Label(root, text="file name")
file_name.place(relx=0.8,rely=0.9,anchor=CENTER)

label_file_name=Label(root,text="html file name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=input(root, text="")
label_file_name.place(relx=0.48,rely=0.03,anchor=CENTER)
root.mainloop()