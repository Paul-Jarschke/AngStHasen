from django.contrib import admin
from django.urls import path
from .models import Flight, Book, UserBooking, User, Statistics, EmptyModelAdmin

from django.shortcuts import render
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

admin.site.site_header = "AngStHasenFlights - Admin Terminal"


class TxtImportForm(forms.Form):
    txt_upload = forms.FileField()


class SeatAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('txt-upload/', self.upload_txt)]

        return new_urls + urls

    def upload_txt(self, request):
        if request.method == "POST":
            txt_file = request.FILES["txt_upload"]

            file_data = txt_file.read().decode('utf8')
            txt_data = file_data.split("\n")

            with open('flightseats/data/chartIn.txt', 'w') as f:

                for i in txt_data:
                    fields = i.split()
                    fields = '\t'.join(fields)
                    print(fields)
                    f.write(fields)
                    f.write('\n')
            f.close()

        form = TxtImportForm()
        data = {"form": form}
        return render(request, "admin/txt_upload.html", data)


admin.site.register(Book, SeatAdmin)
admin.site.register(Flight)
admin.site.unregister(Group)
admin.site.register(UserBooking)
admin.site.register(Statistics, EmptyModelAdmin)
