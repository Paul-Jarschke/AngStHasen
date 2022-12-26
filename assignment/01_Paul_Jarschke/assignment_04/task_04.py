# Task 4 - HTTP Request

# Working with HTTP connections is essential for many data gathering tasks. The Python library urllib provides all
# functionality we need. Write a Python function open_url(url) that:
# - uses urllib to establish an HTTP connection to an arbitrary website
# - retrieves and prints the first 200 characters of the html resource, i.e. the html source code, of the chosen website
# - handles the exceptions thrown by the urllib.request function

from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def open_url(url):
    try:
        html = urlopen(url)
        doc = html.read().decode("utf-8")
        html.close()
        return doc
    except HTTPError as http_e:
        print(f'{http_e} while connecting to : {url}')
        return None
    except URLError as url_e:
        print(f'{url_e} while connecting to : {url}')
        return None


print("\nHTTP Connection:")
print("_______________________________________________________________________________________________________________")

# Urls for testing
# working url
# 'https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError'
# raise http error (404)
# 'https://www.uni-goettingen.de/de/hilfskraft+php/sql+gesucht+%2810+std./monat%29/667669.html'
# raise url error
# 'http://www.iamnotarealaddress.de'

url = 'https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError'
print("Trying to connect to: " + url)
html = open_url(url)

# printing the whole html script
# use print(html) to get full information
if html is not None:
    print(html[0:200])
