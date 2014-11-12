#!/usr/bin/env python
# -*- coding: utf-8 -*- 

text = u"""

The relation between teaching and research has been a perennial theme in academia as well as the Oersted Lectures, with no apparent progress on re- solving the issues. Physics Education Research (PER) puts the whole matter into new light, for PER makes teaching itself a subject of research. This shifts attention to the relation of education research to scientific research as the central issue.
To many, the research domain of PER is exclusively pedagogical. Course content is taken as given, so the research problem is how to teach it most effec- tively. This approach to PER has produced valuable insights and useful results. However, it ignores the possibility of improving pedagogy by reconstructing course content. Obviously, a deep knowledge of physics is needed to pull off anything more than cosmetic reconstruction. It is here, I contend, in addressing the nature and structure of scientific subject matter, that PER and scientific research overlap and enrich one another with complementary perspectives.
The main concern of my own PER has been to develop and validate a sci- entific Theory of Instruction to serve as a reliable guide to improving physics teaching. To say the least, many physicists are dubious about the possibility. Even the late Arnold Arons, patron saint of PER, addressed a recent AAPT session with a stern warning against any claims of educational theory. Against this backdrop of skepticism, I will outline for you a system of general principles that have guided my efforts in PER. With sufficient elaboration (much of which

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
# os.system("say -i -r 200 \""+text+"\"")
os.system("say -r 250 \""+text+"\"")

# print repr(text)

