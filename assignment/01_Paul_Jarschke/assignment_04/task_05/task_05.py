# from task_04 import open_url
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
    logging.basicConfig(level=level,
                        format=format,
                        datefmt=date_format,
                        filename=file_name,
                        filemode=file_mode)

# call in
init_log(file_name= 'log_file',
         file_mode='w',
         level=logging.ERROR,
         format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
         date_format='%m-%d %H:%M')


def open_url(url):
    try:
        html = urlopen(url)
        doc = html.read().decode("utf-8")
        html.close()
        return doc
    except HTTPError as http_e:
        logging.error(f'{http_e} while connecting to : {url}')
        return None
    except URLError as url_e:
        logging.error(f'{url_e} while connecting to : {url}')
        return None


print("\nHTTP Connection:")
print("_______________________________________________________________________________________________________________")
url = 'http://www.iamnotarealaddress.de'
print("Trying to connect to: " + url)
html = open_url(url)

# printing the whole html script
# use print(html) to get full information
if html is not None:
    print(html[0:200])

logging.shutdown()