from tkinter import*
root = Tk()

from PIL import ImageTk,Image

root.title("Title 321th time")

root.geometry("1000x1000")

root.configure(background = "yellow")

img = ImageTk.PhotoImage(Image.open("download1.png"))
img = ImageTk.PhotoImage(Image.open("download2.png"))
img = ImageTk.PhotoImage(Image.open("download3.png"))
img = ImageTk.PhotoImage(Image.open("download4.png"))
img = ImageTk.PhotoImage(Image.open("download5.jpg"))
img = ImageTk.PhotoImage(Image.open("download6.jpg"))
img = ImageTk.PhotoImage(Image.open("download7.png"))
img = ImageTk.PhotoImage(Image.open("download8.png"))
img = ImageTk.PhotoImage(Image.open("download9.jpg"))
img = ImageTk.PhotoImage(Image.open("download10.png"))
img = ImageTk.PhotoImage(Image.open("download11.jpg"))
img = ImageTk.PhotoImage(Image.open("download12.jpg"))

q1 = Label(root,bg = "light blue",text = "Player 1",fg = "black")

q2 = Label(root,bg = "light blue",text = "Player 2",fg = "black")

q3 = Label(root,bg = "light blue",fg = "black")

q4 = Label(root,bg = "light blue",fg = "black")

q5 = Label(root,bg = "orange",fg = "black")

q1.place(relx = 0.2,rely = 0.3,anchor = CENTER)
q2.place(relx = 0.8,rely = 0.3,anchor = CENTER)
q3.place(relx = 0.2,rely = 0.5,anchor = CENTER)
q4.place(relx = 0.8,rely = 0.5,anchor = CENTER)
q5.place(relx = 0.5,rely = 0.7,anchor = CENTER)

root.mainloop()