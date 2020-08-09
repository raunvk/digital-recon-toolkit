import string
import random

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('passgen.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!')


s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
#s4 = string.punctuation

l = int(input("Enter password length: "))
n = int(input("Enter no. of passwords to generate: "))
name = input("Enter text file name to store passwords: ")
name1 = name + ".txt"
print("Saved passwords in: " + name1)

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

