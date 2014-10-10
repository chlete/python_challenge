#!/usr/bin/python

import string
import sys

"""
Alternative to substitution cipher solution; build a map of translation
http://www.pythonchallenge.com/pc/def/map.html
"""

print "type in the code"
challenge = raw_input()



alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 2   # the problem demands this amount of shifts            


trans_map = string.maketrans(alphabet, alphabet[2:] + alphabet[:2]) # alphabet[2:] + alphabet[:2] = cdefghijklmnopqrstuvwxyzab

print challenge.translate(trans_map)

