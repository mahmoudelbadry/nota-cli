#!/usr/bin/env python
import requests
import xerox
import sys

def getTextFromFile(fileName):
	f = open(fileName , 'r')
	text = f.read()
	return text

if __name__ == '__main__':
	reqURL = 'http://nota.cc/nota.py'
	fileName = sys.argv[1]
	text = getTextFromFile(fileName)
	res = requests.post(reqURL , {"textcontent": text})
	notaURL = res.headers['refresh'][7:]
	xerox.copy(notaURL)

	print 'URL of the note is:',notaURL
	print 'The URL has been copied to your clipboard.'
