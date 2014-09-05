from sys import argv
import json
import urllib2
import re

reformatted = []
script, filename = argv

txt = open(filename)

lines = [i for i in txt.readlines()]

for x in lines:
    x = x[:-1]
    # re.sub('[^A-Za-z0-9]+', '', x)

    reformatted.append(x.replace(" ", "+").split('+by+'))

for x in xrange(0, len(reformatted)):
    title = reformatted[x][0]
    author = reformatted[x][1]

    try:
        data = urllib2.urlopen('http://openlibrary.org/search.json?title={0}&author={1}'.format(title, author)).read()
        json_data = json.loads(data)
        print json_data["docs"][0]["title_suggest"]
    except:
        print "{} No work!".format(title)
        #prints out the titles of all the books, based off of json get requests.
        #need to write addition part to uppercase all words that are not "of and the"
        #for example, "The sun also rises"is returned instead of "The Sun Also Rises"
