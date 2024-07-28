# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# frame= ttk.Frame(root)
# def increment():
#    progressBar.step(20)
   
# def decrement():
#    progressBar.step(-20)
   
# def display():
#    print(progressBar["value"])

# progressBar= ttk.Progressbar(frame, mode='determinate')
# progressBar.pack(padx = 10, pady = 10)

# button= ttk.Button(frame, text= "Increase", command= increment)
# button.pack(padx = 10, pady = 10, side = tk.LEFT)

# button= ttk.Button(frame, text= "Decrease", command= decrement)
# button.pack(padx = 10, pady = 10, side = tk.LEFT)
# button= ttk.Button(frame, text= "Display", command= display)
# button.pack(padx = 10, pady = 10, side = tk.LEFT)

# frame.pack(padx = 5, pady = 5)
# root.mainloop()
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
   ["Atikur",17,20000],
   ["Milon",18,23000],
   ["Jaya",18,19000],
   ["sah Alam",40, 20500],
]
index=0
def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("age", "salary")

tree= ttk.Treeview(root, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Name')
tree.heading('age', text='Age')
tree.heading('salary', text='Salary')

read_data()
root.mainloop()

# import tkinter as tk
# import tkinter.ttk as ttk

# root = tk.Tk()

# frame = ttk.Frame(root)
# label = ttk.Label(root, text = "Hello World")
# label.pack(padx = 20, pady = 20)
# sizegrip = ttk.Sizegrip(frame)
# sizegrip.pack(expand = True, fill = tk.BOTH, anchor = tk.SE)
# frame.pack(expand = True, fill = tk.BOTH)

# root.mainloop()
