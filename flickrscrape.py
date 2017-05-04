from flickrapi import FlickrAPI
from pprint import pprint
from urllib.request import urlretrieve

FLICKR_PUBLIC = '0ba5a62e543bd1a4b2c8f662a16577ac'
FLICKR_SECRET = '74261c8a79410e10'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_c, url_m'
results = flickr.photos.search(text='blue sky', per_page=6, extras=extras)

photos = results['photos'] #get the photos information
pprint(photos['photo'][0]['url_m'])

pic = photos['photo'][0]['url_m']
# print(pic)
# pprint(photos['photo'][1]['url_m'])
# pprint(photos['photo'][2]['url_m'])
# pprint(photos['photo'][3]['url_m'])
# pprint(photos['photo'][4]['url_m'])

urlretrieve(pic, "pic1.jpg")
