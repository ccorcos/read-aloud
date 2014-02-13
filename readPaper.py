#!/usr/bin/env python
# -*- coding: utf-8 -*- 

text = u"""

nd landmarks (see e.g [78]). Less readily appreciated is the fact t

"""

import re

def removeAllRegex(text, p, replace=''):
	# remove paper references
	while 1:
		if (p.search(text)):
			text = p.sub(replace,text)
		else:
			break
	return text

p = re.compile(r'\s\[[0-9 ,]*\]')
text = removeAllRegex(text,p)

p = re.compile('[^\x00-\x7F]+')
text = removeAllRegex(text,p)

p = re.compile(r'\n[0-9]+[A-Za-z0-9 _,]+[0-9]+\n')
text = removeAllRegex(text,p, ' ')

p = re.compile(r'\(\s*see e\.g\.?\s*\)')
text = removeAllRegex(text,p, ' ')



import os
# print "say -i -r 250 "+text
os.system("say -i -r 200 \""+text+"\"")

# print repr(text)

