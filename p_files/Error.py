'''
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
temp_convert("xyz");'''
import os
#coding:utf8
filename = raw_input('input your filename:')
try:
   f = open(filename)
   print 'hello'
except IOError,msg:
   print "the file doesn't exsit"
except NameError,msg:
   print "the var wasn't defined"

print 'over'

