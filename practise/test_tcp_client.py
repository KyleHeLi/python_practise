#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import socket

def main():
	# Create a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 9999))
	print s.recv(1024)
	for data in ['Michael', 'Tracy', 'Sarah']:
		# Send data
		s.send(data)
		print s.recv(1024)
	s.send('exit')
	s.close()

	# # Create a connection
	# s.connect(('www.sina.com.cn', 80))
	# # Send data
	# s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

	# # Receive data
	# buffer = []
	# while True:
	# 	# Maximum 1k bytes
	# 	d = s.recv(1024)
	# 	if d:
	# 		buffer.append(d)
	# 	else:
	# 		break
	# data = ''.join(buffer)
	# # Close the connection
	# s.close()
	# header, html = data.split('\r\n\r\n', 1)
	# print header
	# # Write the received data into files
	# with open('sina.html', 'wb') as f:
	# 	f.write(html)


if __name__ == '__main__':
	main()