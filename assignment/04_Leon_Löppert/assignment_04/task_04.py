################################################
#### Programing for Data Scientists: Python ####
####              Assignment 04             ####
####             by Leon Löppert            ####
################################################

# Task 04 - HTTP Request ----

# Working with HTTP connections is essential for many data gathering tasks. The Python library urllib provides all functionality we need. Write a Python function open_url(url) that:

# - uses urllib to establish a HTTP connection to an arbitrary website
# - retrieves and prints the first 200 characters of the html resource, i.e. the html source code, of the chosen website
# - handles the exceptions thrown by the urllib.request function

from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError

def open_url(url):
    try:
        html = urlopen(url) # example: https://docs.python.org/3/library/urllib.error.html
        doc = html.read().decode("utf-8")
        html.close()
        return doc
    except URLError as e1:
        print(f'{e1} while connecting to: {url}') # example: "http://diveintopython.org/"
        return None
    except HTTPError as e2:
        print(f'{e2} while connecting to: {url}') # example: https://realpython.com/python-f-strings/
    except ValueError as e3:
        print(f'{e3} while connecting to: {url}') # example: ww.asdf.com"
        return None




# Read URL page
url = input("Type in URL:\n")


website = open_url(url)
if website != None:
    print("===========================================================================================================")
    print("Connecting to", url)
    print("===========================================================================================================")
    print(website[0:200])

