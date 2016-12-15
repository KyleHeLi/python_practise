<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

class student( object ):

	@property
	def score( self ):
		return self._score

	@score.setter
	def score( self, value ):
		if not isinstance( value, int ):
			raise ValueError( 'score must be an integer!' )
		if value < 0 or value > 100:
			raise ValueError( 'score must between 0 ~ 100!' )
		self._score = value

	@property
	def birth( self ):
		return self._birth

	@birth.setter
	def birth( self, value ):
		self._birth = value

	@property
	def age( self ):
		return int( time.strftime( "%Y", time.localtime() ) ) \
			- self._birth
 	

if __name__ == '__main__':
	test = student()
	test.score = 60
	print test.score
	# test.score( 9999 )
	print( "=======" )
	print( "birth date is:" )
	test.birth = 1990
	print test.birth
=======
=======
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

class student( object ):

	def __init__( self, name ):
		self.name = name

	def __str__( self ):
		return "Student object (name: %s)" % self.name
	__repr__ = __str__

	@property
	def score( self ):
		return self._score

	@score.setter
	def score( self, value ):
		if not isinstance( value, int ):
			raise ValueError( 'score must be an integer!' )
		if value < 0 or value > 100:
			raise ValueError( 'score must between 0 ~ 100!' )
		self._score = value

	@property
	def birth( self ):
		return self._birth

	@birth.setter
	def birth( self, value ):
		self._birth = value

	@property
	def age( self ):
		return int( time.strftime( "%Y", time.localtime() ) ) \
			- self._birth
 	

if __name__ == '__main__':
	test = student()
	test.score = 60
	print test.score
	# test.score( 9999 )
	print( "=======" )
	print( "birth date is:" )
	test.birth = 1990
	print test.birth
<<<<<<< HEAD
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
=======
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
	print test.age