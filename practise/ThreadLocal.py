<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import threading

# Create the global ThreadLocal object
local_school = threading.local()

def process_student():
	print( "Hello, %s (in %s)" % ( local_school.student, threading.current_thread().name )  )

def process_thread( name ):
	# The student with binding ThreadLocal
	local_school.student = name
	process_student()

# Some examples for the multi-thread uses 
# def process_student( name ):
# 	std = Student( name )
# 	# std is a local variable, but each function has to use it, thereby it  has to pass that
# 	do_task_1( std )
# 	do_task_2( std )

# def do_task_1( std ):
# 	do_subtask_1( std )
# 	do_subtask_2( std )

# def do_task_2( std ):
# 	do_subtask_2( std )
# 	do_subtask_2( std )

# global_dict = {}

# def std_thread( name ):
# 	std = Student( name )
# 	# Put the std into the global variable in global_dict
# 	global_dict[threading.current_thread()] = std
# 	do_task_1()
# 	do_task_2()

# def do_task_1():
# 	# It looks for the std in the current thread
# 	std = global_dict[threading.current_thread()]

# def do_task_2():
# 	# Any function can find the std variable in the current thread
# 	std = gloabl_dict[threading.current_thread()]

def main():
	t1 = threading.Thread( target=process_thread, args=( 'Alice', ), name='Thread-A' )
	t2 = threading.Thread( target=process_thread, args=( 'bob', ), name='Thread-B' )
	t1.start()
	t2.start()
	t1.join()
	t2.join()


if __name__ == '__main__':
	main()
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import threading

# Create the global ThreadLocal object
local_school = threading.local()

def process_student():
	print( "Hello, %s (in %s)" % ( local_school.student, threading.current_thread().name )  )

def process_thread( name ):
	# The student with binding ThreadLocal
	local_school.student = name
	process_student()

# Some examples for the multi-thread uses 
# def process_student( name ):
# 	std = Student( name )
# 	# std is a local variable, but each function has to use it, thereby it  has to pass that
# 	do_task_1( std )
# 	do_task_2( std )

# def do_task_1( std ):
# 	do_subtask_1( std )
# 	do_subtask_2( std )

# def do_task_2( std ):
# 	do_subtask_2( std )
# 	do_subtask_2( std )

# global_dict = {}

# def std_thread( name ):
# 	std = Student( name )
# 	# Put the std into the global variable in global_dict
# 	global_dict[threading.current_thread()] = std
# 	do_task_1()
# 	do_task_2()

# def do_task_1():
# 	# It looks for the std in the current thread
# 	std = global_dict[threading.current_thread()]

# def do_task_2():
# 	# Any function can find the std variable in the current thread
# 	std = gloabl_dict[threading.current_thread()]

def main():
	t1 = threading.Thread( target=process_thread, args=( 'Alice', ), name='Thread-A' )
	t2 = threading.Thread( target=process_thread, args=( 'bob', ), name='Thread-B' )
	t1.start()
	t2.start()
	t1.join()
	t2.join()


if __name__ == '__main__':
	main()
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
