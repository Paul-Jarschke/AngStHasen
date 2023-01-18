import logging
import urllib
import urllib.request
from urllib.error import HTTPError,URLError

url_python= 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def init_log(file_name,file_mode,level,format,date_format):
    logging.basicConfig(file_name=file_name,
                        file_mode=file_mode,
                        level=level,
                        format=format,
                        date_format=date_format)

init_log(file_name='test.log', file_mode='a',level=logging.ERROR,format="%(asctime)s %(levelname)s %(message)s",date_format='%d-%m-%y %H:%M')

logging.basicConfig(filename="log.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s",date_format='%d-%m-%y %H:%M')



def open_url(url):
    try:
        fp=urllib.request.urlopen(url)
        bytes= fp.read()
        html_string= bytes.decode("utf8")
        fp.close
        print(html_string[0:200])
    except urllib.error.HTTPError as e:
        logging.exception("Error")
    except urllib.error.URLError as e:
        logging.exception("Error")
    except urllib.error.ContentTooShortError() as e:
        logging.exception("Error")

logging.shutdown()