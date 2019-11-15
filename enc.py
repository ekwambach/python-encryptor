#!/usr/bin/python

#Emily Wambach
#Lab8
#Encrpytion program

import string
import readline
import pickle
from sys import argv

#Encryption key dictionary
key = {'a':'m', 'b':'n', 'c':'b', 'd':'v', 'e':'c', 'f':'x', 'g':'z', 'h':'l', 'i':'k', 'j':'h', 'k':'j', 
  'l':'g', 'm':'f', 'n':'d', 'o':'s', 'p':'a', 'q':'p', 'r':'o', 's':'i', 't':'u', 'u':'y', 'v':'t', 
  'w':'r', 'x':'e', 'y':'w', 'z':'q'}

#Function to encode words with key dictionary values
def encode(words, key):
  result = ''
  for letter in words:
    if letter in key:
      result = result + key[letter]
    else:
      result = result + letter
  return result

f = open(argv[1]) #open the given file from argv[1]
fOut = open("encrypted_" + argv[1], "w") #open a write out file  
lst = f.read() #read file contents to a variable
encrypted = encode(lst, key) #assigned encoded contents to encrypted 
fOut.write(encrypted) #write encrypted to out file
f.close() #close the file

