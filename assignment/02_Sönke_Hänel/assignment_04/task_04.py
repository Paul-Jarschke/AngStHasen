# """Task 04 – HTTP Request
#
# Working with HTTP connections is essential for many data gathering tasks. The Python library urllib provides all functionality we need. Write a Python function open_url(url) that:
#
#     uses urllib to establish a HTTP connection to an arbitrary website
#     retrieves and prints the first 200 characters of the html resource, i.e. the html source code, of the chosen website
#     handles the exceptions thrown by the urllib.request function
#
# """
from urllib import request, error


def open_url(url):
    try:
        site = request.urlopen(url)
        doc = site.read().decode("utf-8")
        site.close()
        print(doc[:200])

    except error.URLError as err:
        print("Error! There is something wrong with the URL.")
    except error.HTTPError as err:
        print("Error! This page probably no longer exists or you dont have the permission.")
    except error.ContentTooShortError as err:
        print("Error!")


open_url("https://de.wikipedia.org/wiki/ASCII-Art#Beispiele_aus_dem_Usenet")
