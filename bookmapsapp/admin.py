from django.contrib import admin

# Register your models here.
from bookmapsapp.models import *

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lng')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'place', 'info')

admin.site.register(Time)
admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Book, BookAdmin)