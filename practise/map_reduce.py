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

def str2num( strNum ):
	numDict = { '1':1, '2':2, '3':3, \
				'4':4, '5':5, '6':6, \
				'7':7, '8':8, '9':9, \
				'0':0 }

def add( x, y ):
	return x + y

def standardizeName( strName ):
	formalizedName = ''
	# Dict of letters in lower case to upper case
	luDict = { 'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E',\
				'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J',\
				'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', \
				'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', \
				'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', \
				'z':'Z' }
	# Dict of letters in upper case to lower case
	ulDict = { 'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e',\
				'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j',\
				'K':'k', 'L':'l', 'M':'m', 'N':'n', 'O':'o', \
				'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', \
				'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', \
				'Z':'z' }
	# Change the first letter to upper case
	if strName[0] in luDict:
		formalizedName += luDict[strName[0]]
	else:
		formalizedName += strName[0]

	for i in range( 1, len(strName) ):
		if strName[i] in ulDict:
			formalizedName += ulDict[strName[i]]
		else:
			formalizedName += strName[i]

	return formalizedName

def prod( numList ):
	if len(numList):
		return reduce( multiply, numList )
	else:
		return False

def multiply( x, y ):
	return x * y


if __name__ == '__main__':
	testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	# Calculate the results from function f(x)=x^2
	print( "Calculated function:" )
	print map( f, testList )

	# Change the integer list to string list
	print( "Changed list:" )
	print map( num2str, testList )

	# Sum up all the numbers in the list by reduce
	print( "Summation:" )
	print reduce( add, testList )

	print( "#############" )
	# Test the name-standardized function
	testNameList = ['adam', 'LISA', 'barT']

	print( "Before test:" )
	print testNameList
	print( "After test:" )
	print map( standardizeName, testNameList )

	testList2 = [1, 2]
	print( "Test the function prod:" )
	print prod( testList2 )
