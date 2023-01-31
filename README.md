## AngStHasenFlights

AngStHasenFlights is an easy-to-use web-based application to book seats on flights and to process and store bookings
automatically.
This application gives customers the possibility to register, log in, get an overview of reserved and free seats on
flights and the possibility to reserve seats.
Administrators can add flights and manage existing user accounts, flights and bookings via the admin page. Admins can
also view and download statistics about the flights.

## Motivation

The purpose of a seat reservation system is to provide customers with a simple, flexible and convenient way to book
flights, and to make processes efficient by avoiding the need for resources for manual entries and corrections through
automatic bookings.
A more academic motivation was to put our python skills into practice in the context of this project.

## Features

- Easy setup and use after installation
- Maintainability and extensibility due to modular MVT scheme of django framework

## Installation

Please make sure you are using a version of Python that is not older than Python 3.8!

Please follow the following steps to install the AngStHasenFlights Django environment:

1. clone the repository using the command line command: "git clone https://github.com/prichi99/AngStHasen.git".
2. open the project-folder "angsthasen/project/seats" of the project in your terminal with the cd command
3. install the required dependencies. To do this, just enter the command "pip install -r requirements.txt" in the
   terminal.
4. start the project with the command: "python manage.py runserver"

## Database troubleshooting:

1. If you do not use our database on the first runup, you need to perform the following commands in the respective order
   to get the server running:
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
2. When there are further database errors, delete the database and all migration files (except the __init__.py) and
   retry step 1.

### Predefined custom users

- This application features sample users out of the box **which should be deleted before the software is taken into
  daily business!!**

| Username     | password              | admin |
|--------------|-----------------------|-------|
| LeonHase     | notafraidofflying1999 | yes   |
| Janniboy_xD  | ichmagflugzeuge_x3    | no    |
| SönkFlug     | appliedstatisticsftw  | no    |
| PaulDerGroße | lecker!paulanerspezi  | no    |

### User functions

- Typical user functions like register, login, logout and a help page are implemented on the website.
- In our demo version users can only select one flight (HAM to ARN). For this flight they can reserve free seats in the
  respective page, see depiction below:

![](project/seats/flightseats/static/img/images/book_seat.png)

### Admin functions:

- Users with admin rights are shown and granted access to the admin page.
- Admins (and only admins) can edit and delete users, bookings and flights.
- Admins can change the seat layout by uploading a new "chartIn.txt" file.
  However, it is important that the format defaults are maintained: The first representing the headings for the
  columns
  representing the seats; the first column representing the rows of seats in the aircraft. Please make sure that you
  include the six seat letters from A to F only.\
  Example:\
  1 A B C D E F \
  2 A B C D E F \
  3 A B C D E F
- Administrators can access and download a statistics page that displays the number and proportion of free and reserved
  seats, as well as lists of all available and unavailable seats. Further, all user information (except
  passwords) are shown. The information can be downloaded to a text file. See depiction below:

![](project/seats/flightseats/static/img/images/show_stats.png)

## Tests (optional: only if you have tests)

Describe and show how to run the tests with code examples.

## Contributions:

Leon:

- statistics area setup/text/download button
- login/logout integration
- base conception
- seat reservation/cancellation (booking function)
- representation of booked/free seats on the webpage inclusive colouring +
  synchronization with database
- setting up default accounts and flights
- ChartIn fileread implementation into booking function
- help page setup
- integration of conditional header and homepage greeting if logged in
- everything in Javascript (especially SweetAlert notifications for rejected and successful bookings or logout)
- logout page with timer
- header and navigation bar improvements

Jan:

- setting up the whole Django framework
- statistics area download http request
- login/logout and user model implementation
- navigation bar implementation
- ChartIn fileread implementation into admin page

Sönke:

- starting page design
- help page text
- logo design
- readme template

Paul:

- refactoring of booking function
- communications management
- quality management and adherence to the PEP 8 Style Guide and best practice guidelines
- exhaustive commenting
- exhaustive programming of tests

## License Agreement

### Power of Attorney Statement

I, the signee, am working on the project 'AngStHasenFlights' under the supervision of Prof. Dr. Bela Gipp. The
specified project involves the creation of software and documentation that shall be placed under an open source license.

I hereby grant Prof. Dr. Bela Gipp full authorization to perform any legal acts necessary, including making declarations
on my behalf, in order to irrevocably place any software and documentation created as a result of my project under an
open source license, e.g. Apache 2.0. The type of license remains at the discretion of Prof. Gipp, as long as it is an
open source license. I am aware that this will permanently exclude any commercial exploitation of my copyrights.

I hereby confirm that I have read and understood the Apache Licence 2.0
at: https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)#fulltext

Göttingen, 31.01.23

Leon Löppert, Jan Parlesak, Sönke Hänel, Paul Jarschke
