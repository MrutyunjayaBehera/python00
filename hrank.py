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