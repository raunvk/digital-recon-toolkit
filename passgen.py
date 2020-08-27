import string
import random
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('passgen.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
	file1.close()
except IOError:
	print('\nBanner File not found!')


s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
#s4 = string.punctuation

l = int(input("Enter password length: "))
print("\n")
n = int(input("Enter no. of passwords to generate: "))
print("\n")
name = input("Enter text file name to store passwords: ")
print("\n")
name1 = name + ".txt"
print("Saved passwords in: " + name1)
print("\n")

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
#s.extend(list(s4))
random.shuffle(s)

for i in range(1,50):
	x = open(name1,'a')
	print("".join(random.sample(s,l)),file = x)
	x.close()
