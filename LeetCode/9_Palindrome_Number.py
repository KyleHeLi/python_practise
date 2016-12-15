<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

class Solution( object ):
	def isPalindrome( self, x ):
		"""
		:type x: int
		:rtype: bool
		"""
		if not isinstance( x, int ):
			print( "The input is not integer." )
			return False

		xList = map( int, str( abs( x ) ) )
		for i in range( len( xList ) / 2 ):
			if xList[i] != xList[-(i+1)]:
				return False
		return True


if __name__ == '__main__':

	value1 = 12321
	value2 = 123
	value3 = '11'
	value4 = -12321
	
	test = Solution()
	print test.isPalindrome( value1 )
	print test.isPalindrome( value2 )
	print test.isPalindrome( value3 )
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

class Solution( object ):
	def isPalindrome( self, x ):
		"""
		:type x: int
		:rtype: bool
		"""
		MAXLEN = 2**31

		if x > MAXLEN or x < 0 or not isinstance( x, int ):
			# print( "The input is not integer." )
			return False

		xList = map( int, str( abs( x ) ) )
		for i in range( len( xList ) / 2 ):
			if xList[i] != xList[-(i+1)]:
				return False

		return True


if __name__ == '__main__':

	value1 = 12321
	value2 = 123
	value3 = '11'
	value4 = -12321
	
	test = Solution()
	print test.isPalindrome( value1 )
	print test.isPalindrome( value2 )
	print test.isPalindrome( value3 )
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
	print test.isPalindrome( value4 )