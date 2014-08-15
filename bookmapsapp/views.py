from django.shortcuts import render, redirect

# Create your views here.


def bookmap(request):
    return render(request, "map.html")