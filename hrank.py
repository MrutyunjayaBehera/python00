#THIS IS THE FIRST PROBLEM IN HACKERRANK PYTHON IF-ELSE SET

#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 5 to 20 , print Weird
#If  is even and greater than 20 , print Not Weird

# The only catch in the problem is, the input function gives a string which can not go through arithmetic operations
# so i converted the string to integer in line 25, then everything is easy



import math
import os
import random
import re
import sys


n = input("enter the  number: ")
print(type(n))
n = int(n)
print(type(n))

if n % 2 != 0:
	print("Weird")
else:
	if n > 2 and n < 5:
		print("Not Weird")
	elif n > 6 and n < 20:
		print("Weird")
	elif n > 20:
		print("Not Weird")
		
		
#ENJOY
