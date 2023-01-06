"""Task 06 – Download File

In Task 4, you used the urllib library to establish a http connection. You can also use the urllib library to perform simple file downloads.

Write a Python function download_file(url, path) that:

    checks whether the input URL points to a .txt file
    if the input URL points to a .txt file
        uses the urllib library to download and
        write the text file to the given path on your machine
    logs an error “No text file found at given URL, download aborted!” to the log file created in Task 5 if the input URL does not point to a .txt file.
    properly handles exceptions

Use the download_file() function to download William Shakespeare’s drama Macbeth as a plain text file from: Macbeth
"""
from urllib import request, error
import logging
from task_05 import init_log


def download_file(url, path):
    if url[-4:] == ".txt":
        try:
            # open url, retrieve content and close connection
            site = request.urlopen(url)
            doc = site.read().decode("utf-8")
            site.close()
            # open file path and write content into it
            f = open(path, "w")
            f.write(doc)
            f.close()
        except error.URLError as err:
            logging.error(f'{err} while connecting to : {url}')
            return None
        except error.HTTPError as err:
            logging.error(f'{err} while connecting to : {url}')
            return None
        except error.ContentTooShortError as err:
            logging.error(f'{err} while connecting to : {url}')
            return None

    else:
        logging.error(f'No text file found at given URL, download aborted!')


# Main block
if __name__ == "__main__":
    init_log(file_name="log_info.txt",
             file_mode='a',
             level=logging.ERROR)
    print()
    download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt",
                  "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python for Data/AngStHasen/assignment/02_Sönke_Hänel/assignment_04/task_05_06/macbeth.txt")
    logging.shutdown()
