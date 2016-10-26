#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from logbook import Logger, StreamHandler, FileHandler
import sys
import os

def f( x, y ):
	return x + y

if __name__ == '__main__':
	StreamHandler(sys.stdout).push_application()
	logger = Logger( 'Test Logbook' )
	log = logbook.FileHandler( 'test.log' )
	log.push_application()

	try:
		f(1, '2')
		logger.info( 'called ' + f.__name__ )
	except:
		logger.warn( 'failed on' )

	try:
		f(1, 2)
		logger.info( 'called ' + f.__name__ )
	except:
		logger.warn( 'choked on, ' )
	