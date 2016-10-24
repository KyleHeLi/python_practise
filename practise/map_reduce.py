#!/usr/bin/env python
# -*- encoding- utf-8 -*-

def f( x ):
	return x * x

def num2str( intNum ):
	strDict = { 1:'1', 2:'2', 3:'3', \
				4:'4', 5:'5', 6:'6', \
				7:'7', 8:'8', 9:'9', \
				0:'0' }
	return strDict[intNum]


if __name__ == '__main__':
	testList = [1, 2, 3, 4, 5, 6, 7, 8, 9];

	# Calculate the results from function f(x)=x^2
	print( "Calculated function:" )
	print map( f, testList )

	# Change the integer list to string list
	print( "Changed list:" )
	print map( num2str, testList )
