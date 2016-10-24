#!/usr/bin/python
# Filename: func_doc.py

def printMax(x, y):
	'''Prints the maximum of two numbers.

	The two values must be integers.'''
	# convert to integers, if possible
	x = int(x)
	y = int(y)

	c = "is maximum"

	if x > y:
		print x, c
	else:
		print y, c

printMax(3, 5)
print printMax.__doc__