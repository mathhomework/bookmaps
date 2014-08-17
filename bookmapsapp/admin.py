from django.contrib import admin

# Register your models here.
from bookmapsapp.models import *

admin.site.register(Time)
admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Place)
admin.site.register(Book)