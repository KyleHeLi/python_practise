<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	for data in ['Michael', 'Tracy', 'sarah']:
		# Send data
		s.sendto(data, ('127.0.0.1', 9999))
		# Receive data
		print s.recv(1024)
	s.close()

if __name__ == '__main__':
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	for data in ['Michael', 'Tracy', 'sarah']:
		# Send data
		s.sendto(data, ('127.0.0.1', 9999))
		# Receive data
		print s.recv(1024)
	s.close()

if __name__ == '__main__':
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
	main()