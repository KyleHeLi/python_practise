#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		# self.helloLabel = Label(self, text='Hello, world!')
		# self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world!'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)


def main():
	app = Application()
	# Set the title of window
	app.master.title('Hello World')
	# Let the main message box loop
	app.mainloop()


if __name__ == '__main__':
	main()