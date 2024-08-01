# import tkinter as t
# root=t.Tk()
# l=t.Label(text='Hello , PYthon !',bg='black',fg='white',width=20,height=10)
# l.pack()

# from tkinter import *
# r=Tk()
# l2=Label(text='Atikur ', bg='green',fg='red',width=15,height=5)
# l2.pack()

# root.mainloop()


# import tkinter as tk
# window=tk.Tk()
# l=tk.Label(text='Name',)
# e=tk.Entry()
# l.pack()
# e.pack()
# window.mainloop()

# import tkinter as t
# window=t.Tk()
# l=t.Label(text='Name')
# e=t.Entry()
# l.pack()
# e.pack()
# e2=t.Entry(show='Real Pytnon')
# e2.pack()
# n=e.get()
# n
# 'atikur Rahman'
# n=e2.get()
# n
# 'My email is  : Atikur@email.com'

# Python program to create a simple GUI
# Simple Quiz using Tkinter


from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

import json

#import json to use json file for data

#class to define the components of the GUI
class Quiz:
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		
		# set question number to 0
		self.q_no=0
		
		# assigns ques to the display_question function to update later.
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for
		# selected option in a question.
		self.opt_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(question)
		
		# keep a counter of correct answers
		self.correct=0

	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True


	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			gui.destroy()
		else:
			# shows the next question
			self.display_question()
			self.display_options()




	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=700,y=50)

	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question on the screen
	def display_question(self):
		
		# setting the Question properties
		q_no = Label(gui, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(gui, text="GeeksforGeeks QUIZ",
		width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=0, y=2)


	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("800x450")

# set the title of the Window
gui.title("GeeksforGeeks Quiz")

# get the data from the json file
with open('a.json') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()


# expression = "" 


# # Function to update expression 
# # in the text entry box 
# def press(num): 
# 	# point out the global expression variable 
# 	global expression 

# 	# concatenation of string 
# 	expression = expression + str(num) 

# 	# update the expression by using set method 
# 	equation.set(expression) 


# # Function to evaluate the final expression 
# def equalpress(): 
# 	# Try and except statement is used 
# 	# for handling the errors like zero 
# 	# division error etc. 

# 	# Put that code inside the try block 
# 	# which may generate the error 
# 	try: 

# 		global expression 

# 		# eval function evaluate the expression 
# 		# and str function convert the result 
# 		# into string 
# 		total = str(eval(expression)) 

# 		equation.set(total) 

# 		# initialize the expression variable 
# 		# by empty string 
# 		expression = "" 

# 	# if error is generate then handle 
# 	# by the except block 
# 	except: 

# 		equation.set(" error ") 
# 		expression = "" 


# # Function to clear the contents 
# # of text entry box 
# def clear(): 
# 	global expression 
# 	expression = "" 
# 	equation.set("") 


# # Driver code 
# if __name__ == "__main__": 
# 	# create a GUI window 
# 	gui = Tk() 

# 	# set the background colour of GUI window 
# 	gui.configure(background="light green") 

# 	# set the title of GUI window 
# 	gui.title("Simple Calculator") 

# 	# set the configuration of GUI window 
# 	gui.geometry("270x150") 

# 	# StringVar() is the variable class 
# 	# we create an instance of this class 
# 	equation = StringVar() 

# 	# create the text entry box for 
# 	# showing the expression . 
# 	expression_field = Entry(gui, textvariable=equation) 

# 	# grid method is used for placing 
# 	# the widgets at respective positions 
# 	# in table like structure . 
# 	expression_field.grid(columnspan=4, ipadx=70)

# 	# create a Buttons and place at a particular 
# 	# location inside the root window . 
# 	# when user press the button, the command or 
# 	# function affiliated to that button is executed . 
# 	button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
# 					command=lambda: press(1), height=1, width=7) 
# 	button1.grid(row=2, column=0) 

# 	button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
# 					command=lambda: press(2), height=1, width=7) 
# 	button2.grid(row=2, column=1) 

# 	button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
# 					command=lambda: press(3), height=1, width=7) 
# 	button3.grid(row=2, column=2) 

# 	button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
# 					command=lambda: press(4), height=1, width=7) 
# 	button4.grid(row=3, column=0) 

# 	button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
# 					command=lambda: press(5), height=1, width=7) 
# 	button5.grid(row=3, column=1) 

# 	button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
# 					command=lambda: press(6), height=1, width=7) 
# 	button6.grid(row=3, column=2) 

# 	button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
# 					command=lambda: press(7), height=1, width=7) 
# 	button7.grid(row=4, column=0) 

# 	button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
# 					command=lambda: press(8), height=1, width=7) 
# 	button8.grid(row=4, column=1) 

# 	button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
# 					command=lambda: press(9), height=1, width=7) 
# 	button9.grid(row=4, column=2) 

# 	button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
# 					command=lambda: press(0), height=1, width=7) 
# 	button0.grid(row=5, column=0) 

# 	plus = Button(gui, text=' + ', fg='black', bg='red', 
# 				command=lambda: press("+"), height=1, width=7) 
# 	plus.grid(row=2, column=3) 

# 	minus = Button(gui, text=' - ', fg='black', bg='red', 
# 				command=lambda: press("-"), height=1, width=7) 
# 	minus.grid(row=3, column=3) 

# 	multiply = Button(gui, text=' * ', fg='black', bg='red', 
# 					command=lambda: press("*"), height=1, width=7) 
# 	multiply.grid(row=4, column=3) 

# 	divide = Button(gui, text=' / ', fg='black', bg='red', 
# 					command=lambda: press("/"), height=1, width=7) 
# 	divide.grid(row=5, column=3) 

# 	equal = Button(gui, text=' = ', fg='black', bg='red', 
# 				command=equalpress, height=1, width=7) 
# 	equal.grid(row=5, column=2) 

# 	clear = Button(gui, text='Clear', fg='black', bg='red', 
# 				command=clear, height=1, width=7) 
# 	clear.grid(row=5, column='1') 

# 	Decimal= Button(gui, text='.', fg='black', bg='red', 
# 					command=lambda: press('.'), height=1, width=7) 
# 	Decimal.grid(row=6, column=0) 
# 	# start the GUI 
# 	gui.mainloop() 
