#!/usr/bin/python
from string import lowercase

def shift2toright (line,shift):
   """
   Shifts the letter a given number
   """
   outline = ""
   for char in line:
          decimal = (ord(char) + shift) % 26 # convert letter into decimal and shift
          char = chr(decimal )          # convert the decimal back into char
          outline += str(char)          # append the result to a string
   return(outline) 


theline = raw_input()

#convert to string
str(theline)

shifted = shift2toright(theline,2)

print shifted


