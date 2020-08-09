import os
import requests
import PIL
import geopy.geocoders
from PIL import Image
from PIL.ExifTags import TAGS
from geopy.geocoders import Here

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('imgmetadata.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!')


def get_exif(img):
    image = Image.open(img)
    image.verify()
    return image._getexif()


def get_labeled_exif(exif):
    if (not exif):
        print("\n No Metadata found because Metadata has been stripped!\n")
	print("\n Try another image!\n")
	exit(0)
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val
    return labeled


img = input("\nEnter image filepath: ")
imgf = Image.open(img)

exif = get_exif(img)
labeled = get_labeled_exif(exif)
print("\n Raw Metadata:\n")
print(labeled,"\n")


exifdata = imgf.getexif()
print("\n Labelled Metadata:\n")
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")






