#!/usr/bin/python

import urllib
import xml.etree.ElementTree
import sys

def url():
	url = "http://papodelouco.com/feed/podcast"
	f = urllib.urlopen(url)
	e = xml.etree.ElementTree.parse(f).getroot()

	for item in e.iter('item'):
		title = item.find('title').text
		print title

def list():
	for x in range(0, 3):
	    print "We're on time %d" % (x)

def main():
	while True:
		x = input()

		if x == 3:
			list()
		elif x == 1:
			url()
		elif x == 'exit':
			exit()

main()