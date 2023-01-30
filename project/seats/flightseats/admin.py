from django.contrib import admin
from django.urls import path
from .models import Flight, Book, UserBooking, Statistics, EmptyModelAdmin

from django.shortcuts import render
from django import forms
from django.contrib.auth.models import Group

admin.site.site_header = "AngStHasenFlights - Admin Terminal"


class TxtImportForm(forms.Form):
    txt_upload = forms.FileField()


# The SeatAdmin class is a custom admin model for the Book model, which adds a URL for a custom view for uploading a .txt file.

class SeatAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('txt-upload/', self.upload_txt)]

        return new_urls + urls

    # The method upload_txt handles the uploaded file and writes its contents to a file named chartIn.txt in the flightseats/data directory.
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
        context = {"form": form}
        return render(request, "admin/txt_upload.html", context)


admin.site.register(Book, SeatAdmin)
admin.site.register(Flight)
admin.site.unregister(Group)
admin.site.register(UserBooking)
admin.site.register(Statistics, EmptyModelAdmin)
