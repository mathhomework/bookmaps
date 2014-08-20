import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from bookmapsapp.models import Book


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
        print data["book"]
        books = Book.objects.filter(title__icontains=data["book"])

        print books
        new_data = serializers.serialize('json', books, use_natural_keys = True)
        return HttpResponse(new_data, content_type='application/json')