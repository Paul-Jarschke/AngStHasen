from django.contrib import admin

from .models import Flight, Book
admin.site.register(Book)
admin.site.register(Flight)
