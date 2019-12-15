import tkinter as tk
root=tk.Tk()
v=tk.IntVar()
v.set(0)        #initializing the choice i.e.Python

languages=[("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]

def ShowChoice():
    print(v.get())

tk.Label(root,text="""Choose your favourite programming languages:""",justify=tk.LEFT,padx=20).pack()

for val,language in enumerate(languages):
    tk.Radiobutton(root,text=language,padx=20,variable=v,fg="royal blue",command=ShowChoice,value=val).pack(anchor=tk.W)

root.mainloop()

