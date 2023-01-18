import urllib
import urllib.request
url_python= 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def open_url(url):
    try:
        fp= urllib.request.urlopen(url)
        bytes= fp.read()
        html_string= bytes.decode("utf8")
        fp.close
        print(html_string[0:200])
    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)
    except urllib.error.ContentTooShortError() as e:
        print(e)


open_url(url_python)
