import logging
import urllib
import urllib.request
from urllib.error import HTTPError,URLError

url_python= 'https://en.wnotreallythoughedia.org/wiki/Python_(programming_language)'

logging.basicConfig(level=logging.INFO,filename="log.log",filemode="a",format="%(asctime)s - %(levelname)s - %(message)s")



def open_url(url):
    try:
        fp=urllib.request.urlopen(url)
        bytes= fp.read()
        html_string= bytes.decode("utf8")
        fp.close
        print(html_string[0:200])
    except urllib.error.HTTPError as e:
        logging.exception("Error")
        return None
    except urllib.error.URLError as e:
        logging.exception("Error")
        return None
    except urllib.error.ContentTooShortError() as e:
        logging.exception("Error")


open_url(url_python)