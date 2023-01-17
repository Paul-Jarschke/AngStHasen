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


def download_file(url, path):
    # only open url if it is a txt file
    if url.endswith('.txt'):
        try:
            # open url and read content
            html = urlopen(url)
            content = html.read().decode('utf-8')
            # give name to downloaded file
            name_of_file = 'Macbeth'
            # add filename to path and
            my_file_path = os.path.join(path, name_of_file + ".txt")
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

data_path = "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/"
out_path = "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/processed/"
