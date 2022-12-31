# Task 6 - Download file

# In Task 4, you used the urllib library to establish a http connection. You can also use the urllib library to perform
# simple file downloads.
#
# Write a Python function download_file(url, path) that:
#
# - checks whether the input URL points to a .txt file
# - if the input URL points to a .txt file, uses the urllib library to download and write the text file to the given
#   path on your machine
# - logs an error “No text file found at given URL, download aborted!” to the log file created in Task 5 if the input
#   URL does not point to a .txt file.
# - properly handles exceptions
#
# Use the download_file() function to download William Shakespeare’s drama Macbeth as a plain text file from: Macbeth

import os
import logging
from task_05 import init_log
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def download_file(url, path):
    # only open url if it is a txt file
    if url.endswith('.txt'):
        try:
            # open url and read content
            html = urlopen(url)
            content = html.read().decode('utf-8')
            # give name to downloaded file
            name_of_file = 'Macbeth'
            # add filename to path and
            my_file_path = os.path.join(path, name_of_file + ".txt")
            # open file and write content to it
            f = open(my_file_path, "w")
            f.write(content)
            # close file
            f.close()
            return None
        except HTTPError as http_e:
            # show exception in log_file if HTTPError occurs
            logging.error(f'{http_e} while connecting to : {url}')
            return None
        except URLError as url_e:
            logging.error(f'{url_e} while connecting to : {url}')
            return None
    else:
        # throw error in logs if url does not point to a txt file
        logging.error('No text file found at given URL, download aborted!')
        return None


# Run only if the script is called
if __name__ == "__main__":
    # initialize logging using our own function
    init_log(file_name='log_file.txt',                          # creates a txt file called 'log_file.txt' with all logs
             level=logging.ERROR,                               # set root logger level to error (40 would also work)
             file_mode='a',                                     # appends all logs to log_file.txt (no overwriting!)
             format="%(asctime)s %(levelname)s %(message)s",    # show date/time, levelname and message in logs
             date_format='%d-%m-%y %H:%M')                      # date format = dd-mm-yy , time format = hh:mm

    print('Downloading file to your path...')

    # download macbeth from url and save it to path
    # use non .txt url to check if the error appears in log_file
    download_file(url='https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt',
                  path=r'C:\Users\Paul\Desktop\Python_for_DS_Files')

    # stop logging
    logging.shutdown()
