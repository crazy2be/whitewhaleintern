#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import io

dprint = lambda *_: None
#dprint = lambda *a: print(*a)

def scramble(word):
	if len(word) <= 2: return word
	new = [''] * len(word)
	new[0], new[-1] = word[0], word[-1]
	shuffleable = []
	for i in range(1, len(word)-1):
		c = word[i]
		if c.isupper() or not c.isalpha():
			new[i] = c
		else:
			shuffleable.append(c)
	random.shuffle(shuffleable)
	dprint(new)
	for i in range(1, len(word)-1):
		if new[i] == '':
			new[i] = shuffleable.pop()
	assert(len(shuffleable) == 0)
	return ''.join(new)

dprint(scramble("Foobar"))
dprint(scramble("am"))
dprint(scramble("♙┶⍥⚕"))
dprint(scramble("foo-bar"))
dprint(scramble("1234 Dundas Street"))

def read_from(f, d):
	word = ""
	while True:
		c = f.read(1)
		if c.isspace() or c == '':
			d.write(scramble(word))
			d.write(c)
			word = ""
			if c == '':
				break # EOF
		else:
			word += c

if len(sys.argv) <= 1:
	read_from(sys.stdin, sys.stdout)
else:
	for arg in sys.argv[1:]:
		print(arg)
		read_from(io.StringIO(arg), sys.stdout)
