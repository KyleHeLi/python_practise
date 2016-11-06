#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys

# def search( keyword, pathname='.' ):
# 	for fi in os.listdir( pathname ):
# 		fi_d = os.path.join( pathname, fi )
# 		if os.path.isdir( fi_d ):
# 			search( keyword, fi_d )
# 		elif keyword in os.path.splitext( fi_d )[0]:
# 			print os.path.abspath( fi_d )

def searchFile( keyword, curDir='.' ):
	'''
	This is the a function for searching files.
	The parameter is the whole or partial file name

	For example:
	python search.py test
	'''

	for x in os.listdir( curDir ):
		nextDir = os.path.join( curDir, x )	
		if os.path.isdir( nextDir ):
			searchFile( keyword, nextDir )
		elif os.path.isfile( nextDir ):
			if keyword in nextDir:
				print os.path.abspath( nextDir )

	# for x in os.listdir( curDir ):
	# 	if os.path.isfile(x):
	# 		if keyword in x:
	# 			absPath = os.path.abspath( curDir )
	# 			print os.path.join( absPath, x )
	# 	elif os.path.isdir(x):
	# 		nextDir = os.path.join( curDir, x )			
	# 		print nextDir
	# 		searchFile( keyword, nextDir )


if __name__ == '__main__':
	
	if len( sys.argv ) >= 2:
		searchFile( sys.argv[1], '.' )
	else:
		print( "Please enter parameter like below." )
		print searchFile.__doc__