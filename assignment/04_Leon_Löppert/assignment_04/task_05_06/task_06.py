################################################
#### Programing for Data Scientists: Python ####
####              Assignment 04             ####
####             by Leon Löppert            ####
################################################

# Task 06 - Logging ----

# In Task 4, you used the urllib library to establish a http connection. You can also use the urllib library to perform simple file downloads.
#
# Write a Python function download_file(url, path) that:
#
# checks whether the input URL points to a .txt file
# if the input URL points to a .txt file, uses the urllib library to download and write the text file to the given path on your machine
# logs an error “No text file found at given URL, download aborted!” to the log file created in Task 5 if the input URL does not point to a .txt file.
# properly handles exceptions

import logging
import os
from task_05 import init_log
from urllib.error import HTTPError, URLError
from urllib.request import urlretrieve

def download_file(url, path):
    for i in range(999):
        if not os.path.exists(path + "/file_download" + str(i+1) + ".txt"):
            if url.endswith(".txt"):
                path = path + "/file_download" + str(i+1) + ".txt"
                try:
                    print("Downloading...")
                    urlretrieve(url = url,
                                filename = path)
                    print("Download complete.")
                except URLError as e1:
                    logging.error(f'{e1} while connecting to: {url}') # example: http://diveintopyhon.org/
                except HTTPError as e2:
                    logging.error(f'{e2} while connecting to: {url}') # example: https://realpython.com/python-f-strings/
                except ValueError as e3:
                    logging.error(f'{e3} while connecting to: {url}') # example: ww.asdf.com
            else:
                logging.error("No text file found at given URL, download aborted!")
            break


if __name__ == "__main__":
        # initialize logging using  own function
    init_log(file_name='task_05_06_log.txt',  # creates a txt file called 'task_05_06_log.txt' with all logs
             level=logging.ERROR,  # set root logger level to error (40 would also work)
             file_mode='a',  # appends all logs to log file
             format="%(asctime)s %(levelname)s %(message)s",  # show date/time, levelname and message in logs
             date_format='%d-%m-%y %H:%M')                     # date format = dd-mm-yy , time format = hh:mm

    # Read URL page
    url = input("Type in URL with txt file to download:\n")
    path = input("Type in a destination folder on your device:\n")
    download_file(url=url, path=path)
    logging.shutdown()

#C:/Users/Work/OneDrive/GAU
#https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt
