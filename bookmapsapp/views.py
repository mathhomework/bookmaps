from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bookmapsapp.models import Book


def bookmap(request):
    return render(request, "map.html")


def get_data(request):
    books = Book.objects.filter(place__isnull=False)
    print books
    data = serializers.serialize('json', books, use_natural_keys=True)
    return HttpResponse(data, mimetype='application/json')
