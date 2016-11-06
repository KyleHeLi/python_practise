#!/usr/bin/env python
# -*- encoding:utf-8 -*-

class Solution( object ):
	def convert( self, s, numRows ):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		result = ''
		if numRows <= 0:
			return False
		elif numRows == 1 or numRows >= len( s ):
			return s	
		zigzag = [ [] for i in range( numRows ) ]
		row, step = 0, 1
		for letter in s:
			zigzag[row] += letter
			if row == 0:
				step = 1
			elif row == numRows - 1:
				step = -1
			row += step
		for x in zigzag:
			result += ''.join( x )

		return result



if __name__ == '__main__':

	string = "PAYPALISHIRING"
	# string = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
	# print len( string )
	test = Solution()
	# print test.convert( string, 10 )

	for i in range( 15 ):
		print test.convert( string, i )