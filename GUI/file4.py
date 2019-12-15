import tkinter as tk

master=tk.Tk()
hi="Hi,how are you?"
msg=tk.Message(master,text=hi)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()
tk.mainloop()       #master.mainloop()

#REPL read,execute,print,loop
