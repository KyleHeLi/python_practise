<<<<<<< HEAD
<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import json

class Student( object ):
	"""docstring for Student"""
	def __init__( self, name, age, score ):
		super( Student, self ).__init__()
		self.name = name
		self.age = age
		self.score = score
		
def student2dict( std ):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

if __name__ == '__main__':
	s = Student( 'Bob', 20, 88 )
	try:
		print( "Cannot change from Student Class to json" )
		print json.dumps( s )
	except Exception, e:
		print e
	print( "=========" )
	print( "After changing the default parameter of json.dump" )
	print json.dumps( s, default=student2dict )

	# d = dict( name='Bob', age=20, score=88 )
	# beforeS = json.dumps( d )
	# print( "Before pickling:" )
	# print beforeS
	# print( "=================" )
	# afterS = json.loads( beforeS )
	# print( "After pickling:" )
=======
=======
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import json

class Student( object ):
	"""docstring for Student"""
	def __init__( self, name, age, score ):
		super( Student, self ).__init__()
		self.name = name
		self.age = age
		self.score = score
		
def student2dict( std ): 
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

def dict2student( d ):
	return Student( d['name'], d['age'], d['score'] )

if __name__ == '__main__':
	s = Student( 'Bob', 20, 88 )
	try:
		print( "Cannot change from Student Class to json" )
		print json.dumps( s )
	except Exception, e:
		print e
	print( "=========" )
	print( "After changing the default parameter of json.dump" )
	print json.dumps( s, default=student2dict )

	# d = dict( name='Bob', age=20, score=88 )
	# beforeS = json.dumps( d )
	# print( "Before pickling:" )
	# print beforeS
	# print( "=================" )
	# afterS = json.loads( beforeS )
	# print( "After pickling:" )
<<<<<<< HEAD
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
=======
>>>>>>> 221a1bab85b6aa034f6b0658e5364eedd8183a33
	# print afterS