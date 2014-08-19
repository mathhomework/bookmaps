from sys import argv
import json
import urllib2
import re


from django.core.management.base import BaseCommand, CommandError
from bookmapsapp.models import *


class Command(BaseCommand):

    def get_place(self, search_place):
        search_place = search_place.replace(" ", "+")
        data = urllib2.urlopen('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk'.format(search_place)).read()
        json_data = json.loads(data)
        lat = json_data["results"][0]["geometry"]["location"]["lat"]
        lng = json_data["results"][0]["geometry"]["location"]["lng"]
        coords = {
            "lat": lat,
            "lng": lng
        }

        return coords
        # get_place("Southern States")
        # returns the gps coordinates of these two places

    def get_info_image(self, query, isbn):
        data = urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q={}&isbn={}&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk'.format(query, isbn)).read()
        json_data = json.loads(data)
        try:
            image = json_data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        except:
            image = "no_image"
        try:
            info = json_data['items'][0]['volumeInfo']['description']
        except:
            info = "no info"
        return {"image": image, "info": info}

    def handle(self, *args, **options):

        reformatted = []

        txt = open(*args)

        lines = [i for i in txt.readlines()]

        for x in lines:
            x = x[:-1]
            reformatted.append(x.replace(" ", "+").split('+by+'))

        for x in xrange(0, len(reformatted)):
            title = reformatted[x][0]
            author = reformatted[x][1]
            print title
            print author
            # setting fields to None and also adding if statements above is to prevent previously set variables
            # being set as fields for the next book that does not have those variables defined from the json request
            final_title = None
            final_author = None
            time = None
            lat = None
            lng = None
            place = None
            info = None
            image = None
            subjects = None

            try:
                data = urllib2.urlopen('http://openlibrary.org/search.json?title={0}&author={1}'.format(title, author)).read()
                json_data = json.loads(data)

                print "=========TITLE====="
                final_title = json_data["docs"][0]["title_suggest"]
                final_author = json_data["docs"][0]["author_name"][0]

                current_author, author_created = Author.objects.get_or_create(name=final_author)
                current_book, book_created = Book.objects.get_or_create(title=final_title)
                current_book.author = current_author


                data_time = json_data["docs"][0]["time"][0]
                print data_time
                isbn = json_data["docs"][0]["isbn"][0]
                print "========ISBN=================="
                print isbn
                time = int(re.findall(r'\d{3,4}', data_time)[0]) #gets first year of the returned list of times from.
                print final_title

                print "========Subject:==========="
                subjects = json_data["docs"][0]["subject"]
                print subjects
                print "=====Place:======"
                place = json_data["docs"][0]["place"][0]
                print place
                coords = self.get_place(place)

                lat = coords["lat"]
                lng = coords["lng"]

                print lat
                print lng
                print "========INFO IMG==========="
                info_image = self.get_info_image(title, isbn)
                print"}}}}}}}}}}}}}}}}}}}}INFO IMG SUCCESS{{{{{{{{{{{{{{{{{{{{{{"
                print info_image
                info = info_image["info"]
                image = info_image["image"]
                print "=========================================================================================="

            except:
                print "{} No work!".format(title)
                #prints out the titles of all the books, based off of json get requests.
                #need to write addition part to uppercase all words that are not "of and the"
                #for example, "The sun also rises"is returned instead of "The Sun Also Rises"

            if time is not None:
                try:
                    time
                except:
                    pass
                else:
                    current_time, time_created = Time.objects.get_or_create(time=time)
                    current_book.time.add(current_time)
            if place is not None:
                try:
                    place
                except:
                    pass
                else:
                    current_place, place_created = Place.objects.get_or_create(name=place, lat=lat, lng=lng)
                    current_book.place = current_place
            if info is not None:
                try:
                    info
                except:
                    pass
                else:
                    current_book.info = info
            if image is not None:
                try:
                    image
                except:
                    pass
                else:
                    current_book.image = image
            if subjects is not None:
                try:
                    subjects
                except:
                    pass
                else:
                    for subject in subjects:
                        current_subject, subject_created = Subject.objects.get_or_create(name=subject)
                        current_book.subject.add(current_subject)
            current_book.save()
            print "+++++++++++++++++++++++++++++++++++++++++DONE+++++++++++++++++++++++++++++++++++++++++++++++++++"








