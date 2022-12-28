# Task 05 - Logging

#The logging module in Python provides functionality for logging and debugging purposes. Use the logging module to
# extend the error handling for the function that you implemented to establish a HTTP connection (Task 4).
# All exceptions thrown by your function shall be logged as errors.

# To accomplish the task:
# - write a Python function init_log(file_name, file_mode, level, format, date_format) that initializes a custom log
#   file to which all debugging information and errors are appended using a format that includes the date, time, level
#   and the message of the logging event
# - log occurring errors by calling logging.error(...)
# - close the log after completing your task by calling logging.shutdown()
# - If you choose not to complete Tasks 4, test the logging functionality with a few examples of your own.

import logging
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# Urls for testing:
# working url
# 'https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError'
# raise http error (404)
# 'https://www.uni-goettingen.de/de/hilfskraft+php/sql+gesucht+%2810+std./monat%29/667669.html'
# raise url error
# 'http://www.iamnotarealaddress.de'


def init_log(file_name, file_mode, level, format, date_format):
    """Initiates basic configuration for a logger.
    Level, format, dateformat, log filename and filemode have to be specified."""
    logging.basicConfig(level=level, format=format, datefmt=date_format, filename=file_name, filemode=file_mode)


# initialize logging with
init_log(file_name='log_file.txt',                          # creates a txt file called 'log_file.txt' with all logs
         level=logging.ERROR,                               # set root logger level to error (40 would also work)
         file_mode='a',                                     # appends all logs to log_file.txt
         format="%(asctime)s %(levelname)s %(message)s",    # show date/time, levelname and message in logs
         date_format='%d-%m-%y %H:%M')                      # date format = dd-mm-yy , time format = hh:mm


def open_url(url):
    try:
        # read html code from url
        html = urlopen(url)
        doc = html.read().decode("utf-8")
        html.close()
        return doc
    except HTTPError as http_e:
        # show exception in log_file instead of printing to stderr
        logging.error(f'{http_e} while connecting to : {url}')
        return None
    except URLError as url_e:
        # show exception in log_file instead of printing to stderr
        logging.error(f'{url_e} while connecting to : {url}')
        return None


print("\nHTTP Connection:")
print("_______________________________________________________________________________________________________________")
url = 'http://www.iamnotarealaddress.de'
print("Trying to connect to: " + url)
html = open_url(url)

# printing the whole html script if no exception is thrown
# use print(html) to get full information
if html is not None:
    print(html[0:200])

# shutdown logging
logging.shutdown()
