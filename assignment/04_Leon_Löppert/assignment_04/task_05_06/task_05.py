################################################
#### Programing for Data Scientists: Python ####
####              Assignment 04             ####
####             by Leon Löppert            ####
################################################

# Task 05 - Logging ----

# The logging module in Python provides functionality for logging and debugging purposes. Use the logging module to extend the error handling for the function that you implemented to establish a HTTP connection (Task 4). All exceptions thrown by your function shall be logged as errors.

# To accomplish the task:

# - write a Python function init_log(file_name, file_mode, level, format, date_format) that initializes a custom log file to which all debugging information and errors are appended using a format that includes the date, time, level and the message of the logging event
# - log occurring errors by calling logging.error(...)
# - close the log after completing your task by calling logging.shutdown()

import logging


def init_log(file_name, file_mode, level, format, date_format):
    logging.basicConfig(filename=file_name,
                        filemode=file_mode,
                        level=level,
                        format=format,
                        datefmt=date_format)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)  # we can specify what level or above goes into the console
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s %(name)-7s: %(levelname)-7s %(message)s') # ist ist space. 7s ist 7 spaces.
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)


from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError

def open_url(url):
    try:
        html = urlopen(url) # example: https://docs.python.org/3/library/urllib.error.html
        doc = html.read().decode("utf-8")
        html.close()
        return doc
    except URLError as e1:
        logging.error(f'{e1} while connecting to: {url}') # example: http://diveintopyhon.org/
        return None
    except HTTPError as e2:
        logging.error(f'{e2} while connecting to: {url}') # example: https://realpython.com/python-f-strings/
        return None
    except ValueError as e3:
        logging.error(f'{e3} while connecting to: {url}') # example: ww.asdf.com
        return None

if __name__ == "__main__":
# initialize logging using  own function
    init_log(file_name='task_05_06_log.txt',  # creates a txt file called 'task_05_06_log.txt' with all logs
             level=logging.ERROR,  # set root logger level to error (40 would also work)
             file_mode='a',  # appends all logs to log file
             format="%(asctime)s %(levelname)s %(message)s",  # show date/time, levelname and message in logs
             date_format='%d-%m-%y %H:%M')                     # date format = dd-mm-yy , time format = hh:mm

    # Read URL page
    url = input("Type in URL:\n")


    website = open_url(url)
    if website != None:
        print("===========================================================================================================")
        print("Connecting to", url)
        print("===========================================================================================================")
        print(website[0:200])

    logging.shutdown()
