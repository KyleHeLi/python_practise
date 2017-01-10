#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import poplib

def main():
	# Input email address, password and pop3 server address
	email = '406392360@qq.com'#raw_input('Email: ')
	password = 'lh1357986420'#raw_input('Password: ')
	pop3_server = 'pop.qq.com'#raw_input('POP3 server: ')

	# Connect to pop3 server
	server = poplib.POP3(pop3_server)
	# Turn on debug info
	server.set_debuglevel(1)
	# Print pop3 server welcom message
	print(server.getwelcome())
	# Authentication
	server.user(email)
	server.pass_(password)
	# Return the amount and disk usage of email
	print("Messages: %s. Size: %s" % server.stat())
	# Return all the list of email
	resp, mails, octets = server.list()
	print mails
	# Obtain the newest email
	index = len(mails)
	resp, lines, octets = server.retr(index)
	# Lines store each line of the original text
	# Get the original text of the entire email
	msg_content = '\r\n'.join(lines)
	# Analyze the email
	msg = Parser().parsestr(msg_content)
	# Delete the email from the server according to the index
	server.dele(index)
	# Close connection
	server.quit()
