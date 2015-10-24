# -*- coding: utf-8 -*-

# Tkinter for Python 2.*, tkinter for Python 3.*
from Tkinter import *

class Application(Frame):
	
	def foo(self):
		print 'foo'
	
	def createWidgets(self):
		menubar = Menu(root)
		file = Menu(menubar)
		file.add_command(label="File", command=self.foo)
		file.add_command(label="Quit", command=self.foo)
		menubar.add_cascade(label="File", menu=file)
		root.config(menu=menubar)
		text = Entry(self, background = 'red')
		text.grid()
		
		
	def __init__(self, master=None):
		Frame.__init__(self, master)
		master.geometry('400x300')
		
		self.grid()
		self.createWidgets()
			
def foo():
	print 'foo'
	
root = Tk()
root.title("WTF")
app = Application(master=root)
app.mainloop()
#root.mainloop()