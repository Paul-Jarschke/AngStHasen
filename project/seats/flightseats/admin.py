# file registers pages to the admin page and defines every functionality needed on the admin page


from django.contrib import admin
from django.urls import path
from .models import Flight, Book, Statistics, EmptyModelAdmin

from django.shortcuts import render
from django import forms
from django.contrib.auth.models import Group

admin.site.site_header = "AngStHasenFlights - Admin Terminal"


# using django-forms for a File-upload-field
class TxtImportForm(forms.Form):
    txt_upload = forms.FileField()


# The SeatAdmin class is a custom admin model for the Book model, which adds a URL for a custom view for uploading a .txt file.
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_choice', 'reserved_by', 'booking_time')

    def get_urls(self):
        urls = super().get_urls()  # get all existing urls
        new_urls = [path('txt-upload/', self.upload_txt)]  # create custom url path

        return new_urls + urls

    # The method upload_txt handles the uploaded file and writes its contents to a file named chartIn.txt in the flightseats/data directory.
    def upload_txt(self, request):
        if request.method == "POST":  # using the method post to retieve the uploaded file
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
        context = {"form": form}
        return render(request, "admin/txt_upload.html", context)


# FlightAdmin class is needed to show what is displayed in Flight class in the admin terminal
class FlightAdmin(admin.ModelAdmin):
    list_display = ('airline', 'flight_number', 'origin_airport', 'dest_airport', 'day', 'month', 'year', 'departure')


# Register what should be shown on admin page
admin.site.register(Book, SeatAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.unregister(Group)
admin.site.register(Statistics, EmptyModelAdmin)
