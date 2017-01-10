<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib

class MyHTMLParser(HTMLParser):
	

	# The first version
	def __init__(self):
		HTMLParser.__init__(self)
		self._feature = {'time': None, 'event-title': None, 'event-location': None}
		# self._flag = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'h3' and attrs.__contains__(('class', 'event-title')):
			self._feature['event-title'] = True
			# self._flag = 'event-title'
		elif tag == 'time':
			self._feature['time'] = True
			# self._flag = 'time'
		elif tag == 'span' and attrs.__contains__(('class', 'event-location')):
			self._feature['event-location'] = True
			# self._flag = 'event-location'

	def handle_data(self, data):
		if self._feature['event-title']:
		# if self._flag == 'event-title':
			print("#######")
			print("The name of the conference --- %s" % data)
			self._feature['event-title'] = None
			# self._flag = ''

		if self._feature['time']:
		# if self._flag == 'time':
			print("The time of the conference -- %s" % data)
			self._feature['time'] = None
			# self._flag = ''

		if self._feature['event-location']:
		# if self._flag == 'event-location':
			print("The location of the conference - %s" % data)
			self._feature['event-location'] = None
			# self._flag = ''

		# self._flag = ''


	# def handle_starttag(self, tag, attrs):
	# 	print('<%s>' % tag)

	# def handle_endtag(self, tag):
	# 	print('</%s>' % tag)

	# def handle_startendtag(self, tag, attrs):
	# 	print('<%s/>' % tag)

	# def handle_data(self, data):
	# 	print('data')

	# def handle_comment(self, data):
	# 	print('<!-- -->')

	# def handle_entityref(self, data):
	# 	print('&%s;' % name)

	# def handle_charref(self, name):
	# 	print('&#%s;' % name)


def main():
	parser = MyHTMLParser()
	html = urllib.urlopen("https://www.python.org/events/python-events/").read()
	parser.feed(html)
	# parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')


if __name__ == '__main__':
=======
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib

class MyHTMLParser(HTMLParser):
	

	# The first version
	def __init__(self):
		HTMLParser.__init__(self)
		self._feature = {'time': None, 'event-title': None, 'event-location': None}
		# self._flag = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'h3' and attrs.__contains__(('class', 'event-title')):
			self._feature['event-title'] = True
			# self._flag = 'event-title'
		elif tag == 'time':
			self._feature['time'] = True
			# self._flag = 'time'
		elif tag == 'span' and attrs.__contains__(('class', 'event-location')):
			self._feature['event-location'] = True
			# self._flag = 'event-location'

	def handle_data(self, data):
		if self._feature['event-title']:
		# if self._flag == 'event-title':
			print("#######")
			print("The name of the conference --- %s" % data)
			self._feature['event-title'] = None
			# self._flag = ''

		if self._feature['time']:
		# if self._flag == 'time':
			print("The time of the conference -- %s" % data)
			self._feature['time'] = None
			# self._flag = ''

		if self._feature['event-location']:
		# if self._flag == 'event-location':
			print("The location of the conference - %s" % data)
			self._feature['event-location'] = None
			# self._flag = ''

		# self._flag = ''


	# def handle_starttag(self, tag, attrs):
	# 	print('<%s>' % tag)

	# def handle_endtag(self, tag):
	# 	print('</%s>' % tag)

	# def handle_startendtag(self, tag, attrs):
	# 	print('<%s/>' % tag)

	# def handle_data(self, data):
	# 	print('data')

	# def handle_comment(self, data):
	# 	print('<!-- -->')

	# def handle_entityref(self, data):
	# 	print('&%s;' % name)

	# def handle_charref(self, name):
	# 	print('&#%s;' % name)


def main():
	parser = MyHTMLParser()
	html = urllib.urlopen("https://www.python.org/events/python-events/").read()
	parser.feed(html)
	# parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')


if __name__ == '__main__':
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
	main()