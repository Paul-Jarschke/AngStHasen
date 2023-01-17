"""Task 01 – Text Pre-Processing

A computational analysis of natural language text typically requires several pre-processing steps,
such as excluding irrelevant text parts, separating the text into words, phrases, or sentences depending on the analysis use case, removing so-called stop words, i.e., words that contain little to no semantic meaning, and normalizing the texts, e.g., by removing punctuation and capitalization.

Use the download_file() function developed in the past assignments to download the plain text versions of Shakespeare’s play Macbeth and Bacon’s New Atlantis. If you choose not to implement assignment 4, task 6, download the files manually. We will also provide some txt files.

Inspect these real-world texts manually to get an idea of what needs to be done to clean and prepare the texts for computational analysis.

Implement the following functions to perform common pre-processing steps on the texts:

    get_speaker_text() – returns only the text spoken by the characters in the plays and removes all other text in the files, such as:
        Information about the file, acknowledgements, copyright notices etc.
        Headings indicating the act and scene
        Stage instructions
        Character names
    normalize_text()
        converts all text to lower case
        removes all punctuation from the texts
    remove_stopwords() – eliminates all stop words that are part of the list of English stop words (we provide two lists of stopwords, try both and see how they perform)
    tokenize_text() – splits the cleaned text into words

This program is a pre-req for the next one."""


from urllib import request, error
import logging
import os
import re
import sys
import shutil
sys.path.insert(1,
                "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_04/task_05_06")
from task_05 import init_log
from task_06 import download_file


# Main block
if __name__ == "__main__":
    init_log(file_name="log_info.txt",
             file_mode='a',
             level=logging.ERROR)
    print()
    download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt",
                  "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth.txt")
    download_file("https://ia801309.us.archive.org/24/items/newatlantis02434gut/nwatl10.txt",
                  "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis.txt")
    logging.shutdown()

"""get_speaker_text() – returns only the text spoken by the characters in the plays and removes all other text in the files, such as:
        Information about the file, acknowledgements, copyright notices etc.
        Headings indicating the act and scene
        Stage instructions
        Character names"""


def get_speaker_text(doc):
    # open file path for the play to be processed
    fr = open(doc)

    # open file path to write content into it:
    fw = open(doc[:-4] + "_speaker_text" + doc[-4:], "w")
    body = False
    paragraph = False
    spoken = False
    i = -1
    if doc[-11:] == "macbeth.txt":

        for line in fr:
            # (notice: doesnt work - maybe fix later)
            # every second line is an empty line so drop it
            i += 1
            if i % 2 == 0:
                # ignore everything before the actual play
                if line.startswith("Actus Primus. Scoena Prima."):
                    body = True
                # a paragraph begins indented
                if line.startswith(" "):
                    paragraph = True
                if line == "\n":
                    paragraph = False
                # the play begins..
                if body:
                    if paragraph:
                        # get rid of the indicator for the character speaking
                        if line.startswith(" "):
                            try:
                                line = line.split(". ")[1]
                            except:
                                pass
                        # sometimes characters (the witches) are indicated by 1,2 or 3 without a subsequent ".")
                        for nr in range(10):
                            line = line.replace(str(nr), "").lstrip()
                        fw.write(line)
    if doc[-15:] == "newatlantis.txt":

        for line in fr:
            lineout = ""
            # every second line is an empty line so drop it
            i += 1
            if i % 2 == 0:
                # ignore everything before the actual play
                if line.startswith("We sailed from Peru,"):
                    body = True
                # ignore everything after the curtain falls
                if line.startswith("[The rest was not perfected.]"):
                    body = False
            # the play begins
            if body:
                for letter in line:
                    if letter == "\"":
                        spoken = not spoken
                        if not spoken:
                            lineout += " "
                        continue
                    if spoken:
                        lineout += letter
                if lineout.strip() != "" and lineout.strip() != "\n":
                    fw.write(lineout)

    fr.close()
    fw.close()


def normalize_text(doc):
    # open file path for the play to be processed
    fr = open(doc)

    # open file path to write content into it:
    fw = open(doc[:-4] + "_normalize" + doc[-4:], "w")

    PUNCTUATION = set("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"")
    # for letter in text:

    for line in fr:
        lineout = ""
        # get rid of PUNCTUATION
        for letter in line:
            if not letter in PUNCTUATION:
                lineout += letter
        # converts all text to lower case
        lineout = lineout.lower()
        fw.write(lineout)
        # removes all punctuation from the texts
    fr.close()
    fw.close()


# eliminates all stop words that are part of the list of English stop words (we provide two lists of stopwords, try both and see how they perform)
def remove_stopwords(doc):
    fw = open(doc[:-4] + "_removed_stopwords" + doc[-4:], "w")
    # aquire set of stopwords
    stopwords = []
    fstop = open(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/assignment_05_program_data/eng_stop_words.txt")
    for line in fstop:
        stopwords.append(line.strip())
    fstop.close()

    # for every stop word, go through the doc and remove every occurence of the stop words
    fr = open(doc)
    for line in fr:
        lineout = ""
        for word in line.split():
            if not word in stopwords:
                lineout += " " + word
        lineout += "\n"
        fw.write(lineout)
    fr.close()
    fw.close()


# tokenize_text() – splits the cleaned text into words
def tokenize_text(doc):
    fr = open(doc)
    token = []
    for line in fr:
        token.extend(line.split())
    return token


# MacBethy:
get_speaker_text(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth.txt")
normalize_text(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text.txt")
remove_stopwords(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text_normalize.txt")
mac_beth_tokens = tokenize_text(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text_normalize_removed_stopwords.txt")

# Atlantis
get_speaker_text(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis.txt")
normalize_text(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis_speaker_text.txt")
remove_stopwords(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis_speaker_text_normalize.txt")
atlantis_tokens = tokenize_text(
    "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis_speaker_text_normalize_removed_stopwords.txt")

# # ignore this. its just a test
# for i in mac_beth_tokens:
#     print(i)
#
# for i in atlantis_tokens:
#     print(i)
