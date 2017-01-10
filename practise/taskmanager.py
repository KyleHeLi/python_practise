<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import random, time, Queue
from multiprocessing.managers import BaseManager

# The queue sending task
task_queue = Queue.Queue()
# The queue receiving task
result_queue = Queue.Queue()

# The QueueManager inheritting from BaseManager
class QueueManager( BaseManager ):
	"""docstring for QueueManager"""
	pass

# Register two queues to the network, connecting Queue object
QueueManager.register( 'get_task_queue', callable=lambda: task_queue )
QueueManager.register( 'get_result_queue', callable=lambda: result_queue )
# Bind with port 5000, setting auth code as 'abc'
manager = QueueManager( address=( '', 5000 ), authkey='abc' )
# Start Queue
manager.start()
# Acquire the Queue object from the network
task = manager.get_task_queue()
result = manager.get_result_queue()
# Put some tasks inside the queue
for i in range( 10 ):
	n = random.randint( 0, 10000 )
	print( "Put task %d..." % n )
	task.put( n )
# Get the results from the result Queue
print( "Try get results..." )
for i in range( 10 ):
	r = result.get( timeout=10 )
	print( "Result: %s" % r )
# Shut down
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import random, time, Queue
from multiprocessing.managers import BaseManager

# The queue sending task
task_queue = Queue.Queue()
# The queue receiving task
result_queue = Queue.Queue()

# The QueueManager inheritting from BaseManager
class QueueManager( BaseManager ):
	"""docstring for QueueManager"""
	pass

# Register two queues to the network, connecting Queue object
QueueManager.register( 'get_task_queue', callable=lambda: task_queue )
QueueManager.register( 'get_result_queue', callable=lambda: result_queue )
# Bind with port 5000, setting auth code as 'abc'
manager = QueueManager( address=( '', 5000 ), authkey='abc' )
# Start Queue
manager.start()
# Acquire the Queue object from the network
task = manager.get_task_queue()
result = manager.get_result_queue()
# Put some tasks inside the queue
for i in range( 10 ):
	n = random.randint( 0, 10000 )
	print( "Put task %d..." % n )
	task.put( n )
# Get the results from the result Queue
print( "Try get results..." )
for i in range( 10 ):
	r = result.get( timeout=10 )
	print( "Result: %s" % r )
# Shut down
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
manager.shutdown()