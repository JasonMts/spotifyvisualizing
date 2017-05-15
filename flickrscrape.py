#library imports
from flickrapi import FlickrAPI
from pprint import pprint
from urllib.request import urlretrieve
from collections import Counter
from nltk.corpus import wordnet as wn

#keys
FLICKR_PUBLIC = '0ba5a62e543bd1a4b2c8f662a16577ac'
FLICKR_SECRET = '74261c8a79410e10'
#holds all possible nouns
allnouns = []

#function that gets pictures given a list of words
def getpictures(keywords):
    counter = 0

    #Make API call and get results in JSON format
    for word in keywords:
        flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
        extras='url_c, url_m'
        results = flickr.photos.search(text=word, per_page=6, extras=extras)

        #get the photos information from the JSON
        photos = results['photos']
        pprint(photos['photo'][0]['url_m'])

        #Keep just the picture URL
        pic = photos['photo'][0]['url_m']

        #Save the picture
        counter += 1
        urlretrieve(pic, "pic" + str(counter) + ".jpg")


def getbestwords(filename):
    #open file passed as argument
    f = open(filename, 'r')
    idx = {}
    top = []

    #Read lyrics, convert them to lowercase and take out apostrophes
    contents = f.read().lower().replace("'", "")

    #create a dict with word frequency
    for word in contents.split():
        if word in idx and len(word) > 4:
            idx[word] += 1
        else:
            idx[word] = 1

    #use Counter library to find the most common words
    countable = Counter(idx)
    mostcommon = countable.most_common(15)

    #get just the words
    for i in range(len(mostcommon)):
        top.append(mostcommon[i][0])

    return(top)

def getnouns():
    #get list of nouns from database
    for i in wn.all_synsets('n'):
        allnouns.append(i.name().split('.',1)[0])

#This function checks if the top words are nouns returns them
def checknouns(top):
    search = []

    #check if the words are noun and print them out if they are
    for j in top:
        if j in allnouns:
            search.append(j)

    #search results
    print(search)
    return(search)

getnouns()
getpictures(checknouns(getbestwords("tunnelvision.txt")))
