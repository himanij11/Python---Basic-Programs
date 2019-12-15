import tkinter as tk

def write():
    print("Tkinter is easy to use!")

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text="Quit",fg="red",command=quit)
button.pack(side=tk.LEFT)

slogan=tk.Button(frame,text="Hello",command=write)
slogan.pack(side=tk.LEFT)

root.mainloop()
