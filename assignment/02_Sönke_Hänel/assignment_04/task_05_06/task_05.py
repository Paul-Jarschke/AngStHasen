"""Task 05 – Logging

The logging module in Python provides functionality for logging and debugging purposes.
Use the logging module to extend the error handling for the function that you implemented to establish a HTTP connection (Task 4).
All exceptions thrown by your function shall be logged as errors.

To accomplish the task:

    +write a Python function init_log(file_name, file_mode, level, format, date_format) that
    +initializes a custom log file to which all debugging information and errors are appended using a format that includes
        the date,
        time,
        level and the message of the logging event
    log occurring errors by calling logging.error(...)
    close the log after completing your task by calling logging.shutdown()

If you choose not to complete Tasks 4, test the logging functionality with a few examples of your own."""
import logging
from urllib import request, error


# see: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
def init_log(file_name, file_mode, level, format='%(asctime)s %(levelname)s %(message)s', date_format='%y-%m-%d %H:%M'):
    logging.basicConfig(filename=file_name,
                        filemode=file_mode,
                        level=level,
                        format=format,
                        datefmt=date_format)


def open_url(url):
    try:
        site = request.urlopen(url)
        doc = site.read().decode("utf-8")
        site.close()
        print(doc[:200])


    except error.URLError as err:
        logging.error(f'{err} while connecting to : {url}')
        return None
    except error.HTTPError as err:
        logging.error(f'{err} while connecting to : {url}')
        return None
    except error.ContentTooShortError as err:
        logging.error(f'{err} while connecting to : {url}')
        return None


# Main block
if __name__ == "__main__":
    init_log(file_name="log_info.txt",
             file_mode='a',
             level=logging.ERROR)
    open_url("https://de.wikeeeeeeeeeeeeeeeeeeeeeeeeipedia.org/wiki/ASCII-Art#Beispiele_aus_dem_Usenet")
    open_url("https://www.google.com/search?q=aphex_twin")
    open_url("https://de.wikipedia.org/wiki/ASCII-Art#Beispiele_aus_dem_Usenet")
    logging.shutdown()
