import json
import re
import urllib2
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from bookmapsapp.models import *


def bookmap(request):
    return render(request, "map.html")


def get_data(request):
    books = Book.objects.filter(place__isnull=False)
    data = serializers.serialize('json', books, use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def add_book(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title_query = data["book"]
        print
        books = Book.objects.filter(title__icontains=title_query)
        if not books:
            books = [get_user_book(title_query)]
        print books
        new_data = serializers.serialize('json', books, use_natural_keys = True)
        return HttpResponse(new_data, content_type='application/json')


def get_place(search_place):
    search_place = search_place.replace(" ", "+")
    data = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk".format(search_place)).read()
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


def get_info_image(query, isbn):
    data = urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q={}&isbn={}&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk'.format(query, isbn)).read()
    json_data = json.loads(data)
    try:
        image = json_data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except:
        image = "no_image"
    try:
        info = json_data['items'][0]['volumeInfo']['description']
    except:
        info = "No info"
    return {"image": image, "info": info}


@csrf_exempt
def add_place_time(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        place, place_created = Place.objects.get_or_create(name=data["place"], lat=data["lat"], lng=data["lng"])
        print place
        book = Book.objects.get(title=data["title"])
        print book
        book.place = place
        time, time_created = Time.objects.get_or_create(time=data["time"])
        book.time.add(time)
        book.save()
        return HttpResponse(status=201)


def get_user_book(query):

    title = query.replace(" ", "+")

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
        data = urllib2.urlopen('http://openlibrary.org/search.json?title={0}'.format(title)).read()
        json_data = json.loads(data)

        print "=========TITLE====="
        final_title = json_data["docs"][0]["title_suggest"]
        final_author = json_data["docs"][0]["author_name"][0]

        current_author, author_created = Author.objects.get_or_create(name=final_author)
        current_book, book_created = Book.objects.get_or_create(title=final_title)
        current_book.author = current_author

        isbn = json_data["docs"][0]["isbn"][0]
        print "========ISBN=================="
        print isbn

        print "========INFO IMG==========="
        info_image = get_info_image(title, isbn)
        print"}}}}}}}}}}}}}}}}}}}}INFO IMG SUCCESS{{{{{{{{{{{{{{{{{{{{{{"
        print info_image
        info = info_image["info"]
        image = info_image["image"]


        data_time = json_data["docs"][0]["time"][0]
        print data_time

        time = int(re.findall(r'\d{3,4}', data_time)[0]) #gets first year of the returned list of times from.
        print final_title

        print "========Subject:==========="
        subjects = json_data["docs"][0]["subject"]
        print subjects
        print "=====Place:======"
        place = json_data["docs"][0]["place"][0]
        print place
        coords = get_place(place)

        lat = coords["lat"]
        lng = coords["lng"]

        print lat
        print lng

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
    return current_book
    print "+++++++++++++++++++++++++++++++++++++++++DONE+++++++++++++++++++++++++++++++++++++++++++++++++++"
