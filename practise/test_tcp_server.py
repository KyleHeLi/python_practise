<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket
import threading
import time

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Listen to port
	s.bind(('127.0.0.1', 9999))
	s.listen(5)
	print("Waiting for connection...")

	while True:
		# Accept a new connection
		sock, addr = s.accept()
		# Create a new thread to handle TCP connection
		t = threading.Thread(target=tcplink, args=(sock, addr))
		t.start()

def tcplink(sock, addr):
	print("Accept new connection from %s:%s..." % addr)
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send("Hello, %s!" % data)
	sock.close()
	print("Connection from %s:%s closed." % addr)



if __name__ == '__main__':
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket
import threading
import time

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Listen to port
	s.bind(('127.0.0.1', 9999))
	s.listen(5)
	print("Waiting for connection...")

	while True:
		# Accept a new connection
		sock, addr = s.accept()
		# Create a new thread to handle TCP connection
		t = threading.Thread(target=tcplink, args=(sock, addr))
		t.start()

def tcplink(sock, addr):
	print("Accept new connection from %s:%s..." % addr)
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send("Hello, %s!" % data)
	sock.close()
	print("Connection from %s:%s closed." % addr)



if __name__ == '__main__':
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
	main()