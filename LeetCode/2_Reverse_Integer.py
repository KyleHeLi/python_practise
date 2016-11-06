#!/usr/bin/env python
# -*- encoding:utf-8 -*-

class Solution( object ):
	def reverse( self, x ):
		"""
		:type x: int
		:rtype: int
		"""
		xStr = str( abs( x ) )
		xList = list( xStr )
		xLen = len(xList)
		MAXLEN = 2**31

		if x > MAXLEN or x == 0:
			return 0
		else:
			for i in range( xLen ):
				if xList[-1] == '0':
					xList.pop()
				else:
					break

		xLen = len( xList )

		for i in range( xLen / 2 ):
			xList[i], xList[-(i+1)] = xList[-(i+1)], xList[i]

		if x >= 0:
			result = int( ''.join( xList ) )
		else:
			result = -int( ''.join( xList ) )

		if result > MAXLEN or result < -MAXLEN:
			return 0
		else:
			return result



if __name__ == '__main__':

	value1 = 123
	value2 = -123
	value3 = 1000000003
	value4 = 10000
	value = 0
	test = Solution()
	print test.reverse( value1 )
	print test.reverse( value2 )
	print test.reverse( value3 )
	print test.reverse( value4 )
	print test.reverse( value4 )
	print test.reverse( value )