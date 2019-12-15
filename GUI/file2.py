import tkinter as tk

def write():
    print("Tkinter is easy to use!")

root=tk.Tk()

tk.Label(root,text="Red text in Times Font",fg="red",font="Times").pack()
tk.Label(root,text="Green text in Helvetica Font",fg="light green",bg="dark green",font="Helvetica 16 bold italic").pack()
tk.Label(root,text="Blue text in Verdana Font",fg="blue",bg="yellow",font="Verdana 10 bold").pack()



root.mainloop()
