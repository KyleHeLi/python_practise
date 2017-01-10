#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from email.mime.text import MIMEText
import smtplib

def main():
	# Input Email address and password
	from_addr = '406392360@qq.com'#raw_input('From: ')
	password = raw_input('Password: ')
	# Input SMTP server address and port
	smtp_server = 'smtp.qq.com'#raw_input('SMTP server: ')
	port = 465
	# Input receiver's address
	to_addr = 'kyle_heli@163.com'#raw_input('To: ')
	msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
	msg['From'] = "{}".format(from_addr)
	msg['To'] = to_addr
	msg['Subject'] = 'Python SMTP Mail Test'

	try:
		smtpObj = smtplib.SMTP_SSL(smtp_server, port)
		smtpObj.set_debuglevel(1)
		smtpObj.login(from_addr, password)
		smtpObj.sendmail(from_addr, [to_addr], msg.as_string())
		print("Mail has been sent successfully")
	except Exception, e:
		raise e



if __name__ == '__main__':
	main()
