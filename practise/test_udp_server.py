<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# Bind port
	s.bind(('127.0.0.1', 9999))

	print("Bind UDP on 9999...")
	while True:
		# Accept data, udp does not need to use listen() funcition
		data, addr = s.recvfrom(1024)
		print("Received from %s:%s." % addr)
		# connect() is for tcp, sendto() is for udp
		s.sendto("Hello, %s!" % data, addr)

if __name__ == '__main__':
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# Bind port
	s.bind(('127.0.0.1', 9999))

	print("Bind UDP on 9999...")
	while True:
		# Accept data, udp does not need to use listen() funcition
		data, addr = s.recvfrom(1024)
		print("Received from %s:%s." % addr)
		# connect() is for tcp, sendto() is for udp
		s.sendto("Hello, %s!" % data, addr)

if __name__ == '__main__':
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
	main()