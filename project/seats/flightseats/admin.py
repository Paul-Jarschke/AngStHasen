from django.contrib import admin
from django.urls import path
from .models import Flight, Book, UserBooking, User
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import Group, User

admin.site.site_header = "AngStHasenFlights - Admin Terminal"


class TxtImportForm(forms.Form):
    txt_upload = forms.FileField()


class SeatAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('txt-upload/', self.upload_txt),
                    path('statistics/', self.statistics)]

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

    def statistics(self, request):
        # All seats list:
        input = open("flightseats/data/chartIn.txt", 'r')
        nrow = len(input.readlines())
        seat_rows = list(map(str, range(nrow + 1)))[1:]  # gives string list of 1 up to number of rows
        seat_letters = ['A', 'B', 'C', 'D', 'F']

        all_seats_dummy = []
        for r in seat_rows:
            for l in seat_letters:
                all_seats_dummy.append(r + l)

        all_seats = str(all_seats_dummy).replace("[", "").replace("]", "").replace("'", "")

        # Booked seats list:
        booked_seats = str(list(map(str, Book.objects.all()))).replace("[", "").replace("]", "").replace("'", "")

        # Reserved seats list:
        booked_seats2 = list(map(str, Book.objects.all()))
        free_seats = [x for x in all_seats_dummy if x not in booked_seats2]
        free_seats = str(free_seats).replace("[", "").replace("]", "").replace("'", "")

        # Number of bookedseats:
        count_book = len(booked_seats)

        # Number of free seats:
        count_free = len(free_seats)

        # Number of all seats:
        count_all = len(all_seats)

        # Ratios of booked/free seats:
        ratio_book = str(round(((count_book / count_all) * 100), 2)) + "%"
        ratio_free = str(round(((count_free / count_all) * 100), 2)) + "%"

        # Number of users
        # user_count = len(User.objects.all())

        # Data of users
        # user_list = User.objects.all()

        #
        # User = get_user_model()
        user_list = User.objects.all()

        context = {
            'all_seats': all_seats,
            'free_seats': free_seats,
            'booked_seats': booked_seats,
            'ratio_book': ratio_book,
            'ratio_free': ratio_free,
            # 'user_count': user_count,
            'user_list': user_list

        }

        return render(request, "admin/statistics.html", context)


admin.site.register(Book, SeatAdmin)
admin.site.register(Flight)
admin.site.unregister(Group)
admin.site.register(UserBooking)
