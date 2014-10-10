#!/usr/bin/python
from string import lowercase

def shift2right (line,shift):
   """
   Shifts the letter a given number
   """
   outline = ""
   for char in line:
<<<<<<< HEAD
          decimal = (ord(char) + shift) % 26 # convert letter into decimal and shift
          char = chr(decimal )          # convert the decimal back into char
          outline += str(char)          # append the result to a string
=======
       decimal = (ord(char) + shift) % 122  # convert letter into decimal and shift
       if decimal < 97:			   #if ascii < 97 (uppercase and other prints)
          decimal += 96			   #shift them
       char = chr(decimal)         # convert the decimal back into char
       outline += str(char)        # append the result to a string
>>>>>>> a48bcea0b89de477057ca4664b02377cf78f22ac
   return(outline) 


theline = raw_input()

#convert to string
str(theline)

shifted = shift2toright(theline,2)

print shifted


