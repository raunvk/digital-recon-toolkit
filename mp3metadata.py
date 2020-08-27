import filetype
import audio_metadata
import eyed3
import mutagen
import tinytag
from tinytag import TinyTag
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('mp3metadata.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
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




