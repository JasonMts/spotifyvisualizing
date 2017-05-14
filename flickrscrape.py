from flickrapi import FlickrAPI
from pprint import pprint
from urllib.request import urlretrieve

#keys
FLICKR_PUBLIC = '0ba5a62e543bd1a4b2c8f662a16577ac'
FLICKR_SECRET = '74261c8a79410e10'

#function that gets pictures given a list of words
def getpictures(keywords):
    counter = 0

    for word in keywords:
        flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
        extras='url_c, url_m'
        results = flickr.photos.search(text=word, per_page=6, extras=extras)

        photos = results['photos'] #get the photos information
        pprint(photos['photo'][0]['url_m'])
        pic = photos['photo'][0]['url_m']
# print(pic)
# pprint(photos['photo'][1]['url_m'])
# pprint(photos['photo'][2]['url_m'])
        counter += 1
        urlretrieve(pic, "pic" + str(counter) + ".jpg")

# def main():

def getbestwords(filename):
    f = open(filename, 'r')
    idx = {}
    contents = f.read().lower()
    print(contents)

    for word in contents.split():
        if word in idx:
            idx[word] += 1
        else:
            idx[word] = 1

    print(idx)

#list = ['yellow', 'blue', 'black']
#getpictures(list)
getbestwords("file.txt")
