## Airline Seat Reservation - ASR
ASR is an easy-to-use web-based application to book seats on flights and to process and store bookings automatically. 
This application gives customers the possibility to register, log in, get an overview of reserved and free seats on flights and the possibility to reserve seats.
Administrators can add flights and manage existing user accounts, flights and bookings via the admin page. Admins can also view and download statistics about the flights.

## Motivation
The purpose of a seat reservation system is to provide customers with a simple, flexible and convenient way to book flights, and to make processes efficient by avoiding the need for resources for manual entries and corrections through automatic bookings.
A more academic motivation was to put our python skills into practice in the context of this project.
 
## Features
- Easy setup and use after installation
- Maintainability and extensibility due to modular MVT scheme of django framework

### User functions
- Typical user functions register, login, logout and get help from the website are implemented.
- Users can choose an airline and select and reserve free seats in the overview there
!(flightseats/static/img/images/book_seat.png)

### Admin functions:
- Users with admin rights are shown and granted access to the admin page.
- Admins (and only admins) can edit and delete users, bookings and flights.
- Admins can change the seat layout by editing the file "chartIn.txt". 
However, it is important that the format defaults are maintained: The first representing the headings for the columns representing the seats; the first column representing the rows of seats in the aircraft. Each aircraft has an even number of seats evenly distributed on two sides.
- Administrators can access and download a statistics page that displays the number and percentage of free and reserved seats, as well as lists of all available and unavailable seats and their number, and all user information (except passwords).
!(flightseats/static/img/images/show_stats.png)

## Installation
Please follow the following steps to install ASR:
1. clone the repository using the command line command: "git clone https://github.com/prichi99/AngStHasen.git".
2. open the sub directory of the project inside  "../tree/main/project/seats" of the project in your terminal
3. install the required dependencies. To do this, just enter the command "pip install -r requirements.txt" in the terminal.
4. start the project with the command: "python manage.py runserver"

## API reference
For small projects with a simple enough API, include the reference docs in this README. For medium-sized and larger projects, provide a link to the API reference docs.

## Tests (optional: only if you have tests)
Describe and show how to run the tests with code examples.

## How to use and extend the project? (maybe)
Include a step-by-step guide that enables others to use and extend your code for their projects. Whether this section is required and whether it should be part of the `README.md` or a separate file depends on your project. If the **very short** `Code Examples` from above comprehensively cover (despite being concise!) all the major functionality of your project already, this section can be omitted. **If you think that users/developers will need more information than the brief code examples above to fully understand your code, this section is mandatory.** If your project requires significant information on code reuse, place the information into a new `.md` file.

## Results
If you performed evaluations as part of your project, include your preliminary results that you also show in your final project presentation, e.g., precision, recall, F1 measure and/or figures highlighting what your project does. If applicable, briefly describe the dataset your created or used first before presenting the evaluated use cases and the results.

If you are about to complete your thesis, include the most important findings (precision/recall/F1 measure) and refer to the corresponding pages in your thesis document.

## License
Include the project's license. Usually, we suggest MIT or Apache. Ask your supervisor. For example:

Licensed under the Apache License, Version 2.0 (the "License"); you may not use news-please except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](LICENSE).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License

## License of this readme-template (remove this once you replaced this readme-template with your own content)
This file itself is partially based on [this file](https://gist.github.com/sujinleeme/ec1f50bb0b6081a0adcf9dd84f4e6271).
