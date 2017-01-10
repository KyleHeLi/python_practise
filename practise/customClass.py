<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Chain( object ):
	"""Dynamically call the Chain class"""
	
	def __init__( self, path='' ):
		super(Chain, self).__init__()
		self._path = path

	def __getattr__( self, path ):
		return Chain( "%s/%s" % ( self._path, path ) )

	def user( self, name ):
		self._user = name
		return self.__getattr__( self._user ) 

	def __str__( self ):
		return self._path
		
if __name__ == '__main__':
	t = Chain()
	print t.status.user.timeline.list
=======
=======
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Chain( object ):
	"""Dynamically call the Chain class"""
	
	def __init__( self, path='' ):
		super(Chain, self).__init__()
		self._path = path

	def __getattr__( self, path ):
		return Chain( "%s/%s" % ( self._path, path ) )

	def user( self, name ):
		self._user = name
		return self.__getattr__( self._user ) 

	def __str__( self ):
		return self._path
		
if __name__ == '__main__':
	t = Chain()
	print t.status.user.timeline.list
<<<<<<< HEAD
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
=======
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
	print t.status.user('Mike').timeline.list