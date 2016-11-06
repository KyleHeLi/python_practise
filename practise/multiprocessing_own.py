#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from multiprocessing import Process, Pool
import os, time, random

# The function for child process
def run_proc( name ):
	print( "Run child process %s (%s)..." % ( name, os.getpid() ) )

def long_time_task( name ):
	print( "Run task %s (%s)..." % ( name, os.getpid() ) )
	start = time.time()
	time.sleep( random.random() * 3 )
	end = time.time()
	print( "Task %s runs %0.2f seconds." % ( name, ( end - start ) ) )

def main():
	# Test 3
	print( "Parent process %s." % os.getpid() )
	p = Pool( 5 )
	for i in range( 5 ):
		p.apply_async( long_time_task, args=( i, ) )
	print( "Waiting for all subprocesses done..." )
	p.close()
	p.join()
	print( "All subprocesses done." )

	# Test 2
	# print( "Process %s start..." % os.getpid() )
	# p = Process( target=run_proc, args=( 'test', ) )
	# print( "Process will start." )
	# p.start()
	# p.join()
	# print( "Process end." )

	# Test 1
	# print( "Process %s start..." % os.getpid() )
	# pid = os.fork()
	# if pid == 0:
	# 	print( "I am child process (%s) and my parent is %s." % ( os.getpid(), os.getppid() ) )
	# else:
	# 	print( "I (%s) just created a child process (%s)." % ( os.getpid(), pid ) )

if __name__ == '__main__':
	main()