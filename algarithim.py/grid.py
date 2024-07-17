
# from tkinter import *
# E=Entry
# L=Label
# def Ai():
#     E=Entry
#     L=Label
#     Name_lab=L(text='Enter your Name:',font=('',20),width=17,height=1,background='lightskyblue',foreground='black')
#     Pass_Lab=L(text='Enter your PassWord:',font=('',20),height=1,width=17,background='red',foreground='black')
#     Name_lab.grid(row=0,column=0)
#     Pass_Lab.grid(row=1,column=2)
#     Name_ent=E(font=('',20),foreground='cyan',width=25,)
#     Pass_ent=E(font=('',20,),width=25,foreground='cyan',show='*')

#     Name_ent.insert(0,'Please write your Name here')

#     Pass_ent.insert(1,'Please write your Name here')
#     Name_ent.grid(row=0,column=1)
#     Pass_ent.grid(row=1,column=3)

#     Email_lab=L(text='Enter your Email:',font=('',20),width=17,height=1,background='lightblue',foreground='black')
#     INro_lab=L(text='Your Country Name :',font=('',20),height=1,width=17,background='white',foreground='black')
#     Email_lab.grid(row=1,column=0)
#     INro_lab.grid(row=2,column=0)

#     Email_ent=E(font=('',20),foreground='cyan',width=25,)
#     INro_ent=E(font=('',20,),width=25,foreground='cyan',  )

#     Email_ent.insert(1,'Please give your email here')

#     INro_ent.insert(2,'Please give your Introduction')
#     Email_ent.grid(row=1,column=1)
#     INro_ent.grid(row=2,column=1)
# Ai()
# import tkinter as tk
# from tkinter import messagebox

# class PremiumSoftwareApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Premium Software App")
        
#         self.label = tk.Label(master, text="Welcome to Premium Software App!")
#         self.label.pack(pady=20)
        
#         self.name_label = tk.Label(master, text="Enter your name:")
#         self.name_label.pack()
        
#         self.name_entry = tk.Entry(master)
#         self.name_entry.pack()
        
#         self.greet_button = tk.Button(master, text="Greet Me", command=self.greet)
#         self.greet_button.pack(pady=10)
        
#         self.exit_button = tk.Button(master, text="Exit", command=self.master.quit)
#         self.exit_button.pack()
    
#     def greet(self):
#         name = self.name_entry.get()
#         if name:
#             messagebox.showinfo("Greetings", f"Hello, {name}! Welcome to Premium Software App.")
#         else:
#             messagebox.showerror("Error", "Please enter your name.")

# def main():
#     root = tk.Tk()
#     app = PremiumSoftwareApp(root)
#     root.mainloop()

# if __name__ == "__main__":


#     main()
