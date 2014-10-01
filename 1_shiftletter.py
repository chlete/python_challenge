#!/usr/bin/python

def shift2toright (line):
   outline = ""
   for char in line:
       decimal = ord(char) + 2
       char = chr(decimal)
       outline += str(char)
   return(outline) 


theline = raw_input()

shifted = shift2toright(theline)

print shifted


