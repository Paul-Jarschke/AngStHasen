# Task 01 - Text Pre-Processing

# A computational analysis of natural language text typically requires several pre-processing steps,
# such as excluding irrelevant text parts, separating the text into words, phrases, or sentences
# depending on the analysis use case, removing so-called stop words, i.e., words that contain little
# to no semantic meaning, and normalizing the texts, e.g., by removing punctuation and capitalization.
#
# Use the download_file() function developed in the past assignments to download the plain text versions of
# Shakespeare’s play Macbeth and Bacon’s New Atlantis.
#
# Inspect these real-world texts manually to get an idea of what needs to be done to clean and prepare the texts
# for computational analysis. Implement the following functions to perform common pre-processing steps on the texts:
#
# get_speaker_text()
# – returns only the text spoken by the characters in the plays and removes all other text in the files, such as:
# Information about the file, acknowledgements, copyright notices etc.
# Headings indicating the act and scene
# Stage instructions
# Character names

# normalize_text()
# converts all text to lower case
# removes all punctuation from the texts

# remove_stopwords()
# – eliminates all stop words that are part of the list of English stop words
# (we provide two lists of stopwords, try both and see how they perform)

# tokenize_text()
# – splits the cleaned text into words

import os
import logging
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# Functions #


def download_file(url, path, filename='file'):
    # only open url if it is a txt file
    if url.endswith('.txt'):
        try:
            # open url and read content
            html = urlopen(url)
            # Net Atlantis cannot be decoded with utf-8 -> latin1 works for both
            content = html.read().decode('latin1')
            # add filename to path and
            my_file_path = os.path.join(path, filename + ".txt")
            # open file and write content to it
            f = open(my_file_path, "w")
            f.write(content)
            # close file
            f.close()
            return None
        except HTTPError as http_e:
            # show exception in log_file if HTTPError occurs
            logging.error(f'{http_e} while connecting to : {url}')
            return None
        except URLError as url_e:
            logging.error(f'{url_e} while connecting to : {url}')
            return None


# execution
dl_path = r'C:\Users\Paul\PycharmProjects\AngStHasen\assignment\01_Paul_Jarschke\assignment_05\text'
out_path = r'C:\Users\Paul\PycharmProjects\AngStHasen\assignment\01_Paul_Jarschke\assignment_05\text\processed_text'

if __name__ == "__main__":
    # File Download
    # MacBeth
    download_file(url="https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt",
                  path=dl_path,
                  filename='MacBeth')

    # Net Atlantis
    download_file(url="https://ia801309.us.archive.org/24/items/newatlantis02434gut/nwatl10.txt",
                  path=dl_path,
                  filename='Net_Atlantis')
