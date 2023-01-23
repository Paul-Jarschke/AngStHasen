from .models import Book, User

# Booked seats list:
bookedseats = list(map(str, Book.objects.all()))

# All seats list:
input = open("flightseats/data/chartIn.txt", 'r')
nrow = len(input.readlines())
seatrows = list(map(str, range(nrow + 1)))[1:]
seatletters = ['A', 'B', 'C', 'D', 'F']

allseats = []
for r in seatrows:
    for l in seatletters:
        allseats.append(r + l)

# Reserved seats list:
freeseats = [x for x in allseats if x not in bookedseats]

# Now we have three list bookedseats, allseats, freeseats that can be displayed in statistics interface

# Number of bookedseats:
count_book = len(bookedseats)

# Number of free seats:
count_free = len(freeseats)

# Number of all seats:
count_all = len(allseats)

# Ratios:
ratio_book = count_book / count_all
ratio_free = count_free / count_all

# Number of users
len(User.objects.all())

# Data of users
User.objects.all()
