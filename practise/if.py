#!/usr/bin/python
# Filename: if.py

number = 23
guess = int(raw_input('Enter an integer:'))

if guess == number:
	print("Congratulation, you guess it.") # New block starts here
	print("(but you do not win any prize!)") # New block starts here
elif guess < number:
	print("No, it is a little higher than that") # Another block
	# You can do whatever you want in a block
else:
	print("No, it is a littel lower than that") 
	# You must have guess > number to reach here

print("Done") 
# This last statemenet is always executed, after the if statement is 
# executed