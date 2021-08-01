import hashlib
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('hashcrack-header.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
	file1.close()
except IOError:
	print('\nBanner File not found!')

response = input("\nEnter the type of hash encrypt you want to crack: \n\n1)MD5 \n2)SHA-256 \n3)SHA-512 \n\n")

if (response == '1'):

    flag = 0
    passhash = input("\nEnter md5 hash: ")
    wordlist = input("\nEnter passlist: ")

    try:
        passfile = open(wordlist, "r")
    except:
        print("\nNo file found !")
        quit()

    for word in passfile:
        encword = word.encode('utf-8')
        digest = hashlib.md5(encword.strip()).hexdigest()

        if digest == passhash:
            print("\nPassword Found :D")
            print("\nPassword is: " + word)
            flag = 1
            break

    if flag == 0:
        print("\nPassword not found :(")
        print("\nPlease modify your wordlist !")


elif (response == '2'):

    flag = 0
    passhash = input("\nEnter SHA256 hash: ")
    wordlist = input("\nEnter passlist: ")

    try:
        passfile = open(wordlist, "r")
    except:
        print("\nNo file found !")
        quit()

    for word in passfile:
        encword = word.encode('utf-8')
        digest = hashlib.sha256(encword.strip()).hexdigest()

        if digest == passhash:
            print("\nPassword Found :D")
            print("\nPassword is: " + word)
            flag = 1
            break

    if flag == 0:
        print("\nPassword not found :(")
        print("\nPlease modify your wordlist !")


elif (response == '3'):

    flag = 0
    passhash = input("\nEnter SHA512 hash: ")
    wordlist = input("\nEnter passlist: ")

    try:
        passfile = open(wordlist, "r")
    except:
        print("\nNo file found !")
        quit()

    for word in passfile:
        encword = word.encode('utf-8')
        digest = hashlib.sha512(encword.strip()).hexdigest()

        if digest == passhash:
            print("\nPassword Found :D")
            print("\nPassword is: " + word)
            flag = 1
            break

    if flag == 0:
        print("\nPassword not found :(")
        print("\nPlease modify your wordlist !")


else:
	print("\nWrong Option!")
	exit(0)
