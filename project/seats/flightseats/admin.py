from django.contrib import admin
from django.urls import path
from .models import Flight, Book, Seats
from django.shortcuts import render
from django import forms
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
            txt_file= request.FILES["txt_upload"]




        form = TxtImportForm()
        data = {"form":form}
        return render(request, "admin/txt_upload.html", data)


admin.site.register(Book)
admin.site.register(Flight,SeatAdmin)
