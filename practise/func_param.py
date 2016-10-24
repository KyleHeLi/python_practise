#!/usr/bin/python
# Filename: func_param.py

def printMax(a, b):
	c = "is maximum";
	if a > b:
		print a, c
	else:
		print b, c

# directly give literal values
printMax(3, 4) 

# give variables as arguments
x = 5
y = 7

printMax(x, y)