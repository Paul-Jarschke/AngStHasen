import urllib
import logging
from urllib import request
from urllib.error import HTTPError,URLError
import os.path



logging.basicConfig(
    filename='test.log',
    filemode='w',
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.DEBUG
)


logging.basicConfig(filename="txt.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s")

def download_file(url,path):
    if url.endswith('.txt'):
        try:
            file= 'macbeth.txt'
            request.urlretrieve(url, file)
            Name = os.path.join(path, file)
            file1 = open(Name, "w")
            file1.write("file information")
            file1.close()

            return None
        except urllib.error.HTTPError as e:
            logging.exception("No text file found at given URL, download aborted!")
            return None
        except urllib.error.URLError as e:
            logging.exception("No text file found at given URL, download aborted!")
            return None
        except urllib.error.ContentTooShortError() as e:
            logging.exception("No text file found at given URL, download aborted!")


url='https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt'
path='C:/Users/janpa/OneDrive/Skrivebord'

download_file(url, path)