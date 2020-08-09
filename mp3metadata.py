import filetype
import audio_metadata
import eyed3
import mutagen
import tinytag
from tinytag import TinyTag

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('mp3metadata.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!')


audio = input("\nEnter audio filepath: ")


metadata = audio_metadata.load(audio)
print("\nRaw Metdata:\n\n", metadata,"\n\n")

atag = TinyTag.get(audio)
print("Artist:\t", atag.albumartist,"\n\n")
print("No. of channels:\t", atag.channels,"\n\n")
print("Genre:\t", atag.genre,"\n\n")

aud = eyed3.load(audio)
print("Album:\t", aud.tag.album,"\n\n")


