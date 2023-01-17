from django.contrib import admin
from django.urls import path
from .models import Flight, Book, Seats
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import default_storage


class TxtImportForm(forms.Form):
    txt_upload= forms.FileField()


class SeatAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls= super().get_urls()
        new_urls= [path('txt-upload/', self.upload_txt)]
        return new_urls+urls

    def upload_txt(self, request):
        if request.method == "POST":
            txt_file = request.FILES["txt_upload"]
            file_data = txt_file.read().decode('utf8')
            txt_data = file_data.split("\n")

            for i in txt_data:
                fields = i.split()
                print(fields)







        form = TxtImportForm()
        data = {"form":form}
        return render(request, "admin/txt_upload.html", data)


    #def seat_layout(self, n_col):
        #f = open('flightseats/data/seat_layout.txt', "w")
        #for i in range(n_col):
        #    f.write(f'1	A	B	C	D	E	F\n')
        #f.close()

admin.site.register(Book)
admin.site.register(Flight,SeatAdmin)
