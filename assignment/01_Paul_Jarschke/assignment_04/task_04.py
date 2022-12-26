# Task 4 - HTTP Request

# Working with HTTP connections is essential for many data gathering tasks. The Python library urllib provides all
# functionality we need. Write a Python function open_url(url) that:
# - uses urllib to establish an HTTP connection to an arbitrary website
# - retrieves and prints the first 200 characters of the html resource, i.e. the html source code, of the chosen website
# - handles the exceptions thrown by the urllib.request function

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


def open_url(url):
    try:
        html = urlopen(url)
        doc = html.read().decode("utf-8")
        html.close()
        return doc
    except HTTPError as http_e:
        print("%s while connecting to: %s" % (http_e, url))
        return None
    except URLError as url_e:
        print("%s while connecting to: %s" % (url_e, url))
        return None


print("\nHTTP Connection:")
print("===========================")

url = "http://www.umsl.edu/~siegelj/newcourse/part1/URL-HTTP.html"
print("Trying to connect to: " + url)
html = open_url(url)

if html != None:
    print(html[0:1000])