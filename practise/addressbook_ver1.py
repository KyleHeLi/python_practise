#!/usr/bin/env python
# Filename: addressbook.py

import os
#import pickle as p
import cPickle as p

# static variable
OPENFILEFAIL = -1
NOSUCHPERSON = -2

# The name of the address book
contactBook = 'contact.data'

class Contact:
	'''Represents a contact persone.'''

	tempContent = []

	# def __init__(self, per_info):
	# 	self.name = per_info[0]
	# 	self.sex = per_info[1]
	# 	self.age = per_info[2]
	# 	self.email = per_info[3]
	# 	self.phoneNumber = per_info[4]
	# 	self.group = per_info[5]
	# 	print("Initialize contact person %s") % self.name

	def __init__(self):
		print("Initialize contact person")	# % self.name

	def __del__(self):
		'''Destroy the object'''
		print("Object has been destroyed.")	# % self.name

	def add(self, per_info):
		# self.name = per_info[0]
		# self.sex = per_info[1]
		# self.age = per_info[2]
		# self.email = per_info[3]
		# self.phoneNumber = per_info[4]
		# self.group = per_info[5]
		# person = ['%s', '%s', '%s', '%s', '%s', '%s'] % \
		# (self.name, self.sex, self.age, self.email, self.phoneNumber, self.group)
		f = file(contactBook, 'a')
		# p.dump(person, f)
		p.dump(per_info, f)
		f.close()

	def delete(self, in_name):
		if self.search(in_name, False) == OPENFILEFAIL or \
		self.search(in_name, False) == NOSUCHPERSON:
			print("Nothing we can do since there is no such" + \
				" file or no such person.")
		else:
			self.display(True)
			for i in range(len(self.tempContent)):
				if in_name == self.tempContent[i][0]:
					del self.tempContent[i]
			
			f = file(contactBook, 'w')
			for i in range(len(self.tempContent)):
				p.dump(self.tempContent[i], f)
			f.close()

	def modify(self, in_name):
		if self.search(in_name, False) == OPENFILEFAIL or \
		self.search(in_name, False) == NOSUCHPERSON:
			print("Nothing we can do since there is no such" + \
				" file or no such person.")
		else:
			self.display(True)
			for i in range(len(self.tempContent)):
				if in_name == self.tempContent[i][0]:
					changedInfo = []

					changedInfo.append(raw_input("Name (default unchanged):"))
					changedInfo.append(raw_input("Sex (default unchanged):"))
					changedInfo.append(raw_input("Age (default unchanged):"))
					changedInfo.append(raw_input("Email (default unchanged):"))
					changedInfo.append(raw_input("Phone Number (default unchanged):"))
					changedInfo.append(raw_input("Group (default unchanged): "))

					for j in range(len(changedInfo)):
						if changedInfo[j] == '':
							changedInfo[j] = self.tempContent[i][j]
					self.tempContent[i] = changedInfo[:]
					del changedInfo[:]

			f = file(contactBook, 'w')
			for i in range(len(self.tempContent)):
				p.dump(self.tempContent[i], f)
			f.close()		

	def search(self, in_name, canPrint):
		running = True
		# find_flag = False
		try:
			f = file(contactBook, 'rb')
		except(IOError):
			print("There is no such file, please create one.")
			running = False
		while running:
			try:
				search_find = p.load(f)
				if search_find[0] == in_name:
					if canPrint:
						print search_find
					# find_flag = True
					break
			except(EOFError):
				if canPrint:
					print("No such person")
				return NOSUCHPERSON
				# break
		# if not find_flag:
		# 	print("No such person.")
		if running:
			return search_find
			f.close()
		else:
			return OPENFILEFAIL

	def display(self, useTemp):
		del self.tempContent[:]
		self.tempContent = []

		running = True
		try:
			f = file(contactBook, 'rb')
		except(IOError):
			print("There is no such file, please create one.")
			running = False
		while running:
			try:
				if not useTemp:
					dis_all = p.load(f)
					print dis_all
				else:
					self.tempContent.append(p.load(f))
			except(EOFError):
				break
		if running:
			f.close()

if __name__ == "__main__":
	description = \
'''
(a)dd		: add the new contact person into the address book
(d)elete	: delete the existing contact person
(dis)play	: show all the information of the address book
(m)odify	: modify the information of contact person
(s)earch	: search for the contact person in the address book
(r)ecover	: recover the data file
(q)uit		: exit the application
'''
	running = True
	while running:
		print("==============================================")
		cmd = raw_input("What would you like to do with the address book?\n" \
			+ description)
		test = Contact()
		if cmd == 'a' or cmd == 'A':
			info = raw_input("Input the information as the format below\n" \
			+ "(e.g. name sex age email phoneNumber group)\n").split(" ")
			test.add(info)
		elif cmd == 'd' or cmd == 'D':
			delete_name = raw_input("Enter the name you wanna delete --> ")
			test.delete(delete_name)
		elif cmd == 'dis' or cmd == 'Dis':
			test.display(False)
		elif cmd == 'm' or cmd == 'M':
			modify_name = raw_input("Enter the name you wanna modify --> ")
			test.modify(modify_name)
		elif cmd == 's' or cmd == 'S': 
			search_name = raw_input("Enter the name you wanna search --> ")
			test.search(search_name, True)
		elif cmd == 'q' or cmd == 'Q':
			print("Exit the application.")
			running = False
		elif cmd == 'r' or cmd == 'R':
			cp_command = "cp contact.data.bak contact.data"
			os.system(cp_command)
		else:
			print("No such parameter, please try again.")
