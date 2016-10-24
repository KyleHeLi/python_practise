#!/usr/bin/python
# Filename: str_methods.py

name = ("Kyle")	# This is a string object

if name.startswith("Ky"):
	print("Yes, the string starts with \"Ky\"")

if 'y' in name:
	print("Yes, it contains the string \"a\"")

if name.find("le") != -1:
	print("Yes, it contains the string \"le\"")

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
print delimiter
print mylist