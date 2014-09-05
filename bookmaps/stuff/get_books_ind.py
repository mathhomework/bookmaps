import json
import re
from sys import argv
import urllib2

__author__ = 'Andrew'

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
        print "---------------"
        data_time = json_data["docs"][0]["time"][0]
        time = int(re.findall(r'\d{4}', data_time)[0]) #gets first year of the returned list of times from.
        print "---------------"
        place = json_data["docs"][0]["place"][0]
        print "==============================================="
        # print time


    except:
        print "{} No work!".format(title)
        #prints out the titles of all the books, based off of json get requests.
        #need to write addition part to uppercase all words that are not "of and the"
        #for example, "The sun also rises"is returned instead of "The Sun Also Rises"


# def get_place(search_place):
#     search_place = search_place.replace(" ", "+")
#     data = urllib2.urlopen('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk'.format(search_place)).read()
#     json_data = json.loads(data)
#     print json_data["results"][0]["geometry"]["location"]["lat"]
#     print json_data["results"][0]["geometry"]["location"]["lng"]
#
# get_place("Southern States")