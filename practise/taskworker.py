<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time, sys, Queue
from multiprocessing.managers import BaseManager

# Create the QueueManager similar to the one in taskmanager.py
class QueueManager( BaseManager ):
	pass

# Since the QueueManager only gets the Queue from network, the registration only requires name
QueueManager.register( 'get_task_queue' )
QueueManager.register( 'get_result_queue' )

# Connect to the server, which is running taskmanager
server_addr = '127.0.0.1'
print( "Connect to server %s..." % server_addr )
# Keep the port and auth code as same as those in taskmanager.py
m = QueueManager( address=( server_addr, 5000 ), authkey='abc' )
# Connect to network
m.connect()
# Get the Queue object
task = m.get_task_queue()
result = m.get_result_queue()
# Get the task from queue, and put the results into results queue
for i in range( 10 ):
	try:
		n = task.get( timeout=1 )
		print( "run task %d * %d..." % (n, n) )
		r = '%d * %d = %d' % ( n, n, n*n )
		time.sleep( 1 )
		result.put( r )
	except Queue.Empty:
		print( "task queue is empty." )
# Process ended
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time, sys, Queue
from multiprocessing.managers import BaseManager

# Create the QueueManager similar to the one in taskmanager.py
class QueueManager( BaseManager ):
	pass

# Since the QueueManager only gets the Queue from network, the registration only requires name
QueueManager.register( 'get_task_queue' )
QueueManager.register( 'get_result_queue' )

# Connect to the server, which is running taskmanager
server_addr = '127.0.0.1'
print( "Connect to server %s..." % server_addr )
# Keep the port and auth code as same as those in taskmanager.py
m = QueueManager( address=( server_addr, 5000 ), authkey='abc' )
# Connect to network
m.connect()
# Get the Queue object
task = m.get_task_queue()
result = m.get_result_queue()
# Get the task from queue, and put the results into results queue
for i in range( 10 ):
	try:
		n = task.get( timeout=1 )
		print( "run task %d * %d..." % (n, n) )
		r = '%d * %d = %d' % ( n, n, n*n )
		time.sleep( 1 )
		result.put( r )
	except Queue.Empty:
		print( "task queue is empty." )
# Process ended
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
print( "worker exit." )