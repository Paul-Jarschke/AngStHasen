################################################
#### Programing for Data Scientists: Python ####
####              Assignment 05             ####
####             by Leon Löppert            ####
################################################

# Task 01 - Text Pre-Processing ----

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
# get_speaker_text() – returns only the text spoken by the characters in the plays and removes all other text in the files, such as:
# Information about the file, acknowledgements, copyright notices etc.
# Headings indicating the act and scene
# Stage instructions
# Character names

# normalize_text()
# converts all text to lower case
# removes all punctuation from the texts

# remove_stopwords() – eliminates all stop words that are part of the list of English stop words (we provide two lists of stopwords, try both and see how they perform)

# tokenize_text() – splits the cleaned text into words

import os
import re
import sys
import shutil

sys.path.insert(0, 'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_04/task_05_06')
from task_06 import download_file

dpath = "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/"
opath = "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/processed/"

if __name__ == "__main__":
    download_file(url="https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt",  # MacBeth
                  path=dpath)
    download_file(url="https://ia801309.us.archive.org/24/items/newatlantis02434gut/nwatl10.txt",  # Net Atlantis
                  path=dpath)

    try:
        os.remove(dpath + "MacBeth.txt")
    except:
        pass
    try:
        os.remove(dpath + "NewAtlantis.txt")
    except:
        pass

    os.rename(dpath + "file_download1.txt",
              dpath + "MacBeth.txt")
    os.rename(dpath + "file_download2.txt",
              dpath + "NewAtlantis.txt")


def get_speaker_text(file):
    play = file.rsplit('/')[-1].replace(".txt", "")
    text = open(file, "rt")

    newname = opath + file.rsplit('/')[-1].replace(".txt", "") + "_getspeaker.txt"
    output = open(newname, "wt")

    if play == "MacBeth":

        body = False
        paragraph = False

        for line in text:
            if line.startswith("Actus Primus"):
                body = True
            if line.startswith(" "):
                paragraph = True
            if line == "\n":
                paragraph = False
            if body == True:
                if paragraph == True:
                    if re.match(r'\s', line):
                        try:
                            line = line.split(". ")[1]
                        except:
                            pass
                    for nr in range(10):
                        line = line.replace(str(nr), "").lstrip()
                    output.write(line)

    if play == "NewAtlantis":

        body = False
        speaking = False

        for line in text:
            if line.startswith("We sailed from Peru"):
                body = True
            if line.startswith("[The rest was not perfected.]"):
                body = False

            if body == True:
                for line in text:
                    linenew = ""
                    for letter in line:
                        if letter == '"':
                            speaking = not speaking
                        if speaking == True:
                            linenew = linenew + letter
                    linenew = linenew.replace('"', " ")
                    if linenew != "":
                        output.write(linenew)
                        if not linenew.endswith("\n"):
                            output.write("\n")
    return newname


def normalize_text(file):
    punctuation = [",", ".", ":", ";", "/", "\\", "!", "?", "[", "]", "(", ")", "{", "}", "...", "-", "'", '"', "*"]
    text = open(file, "rt")

    newname = opath + file.rsplit('/')[-1].replace(".txt", "") + "_normal.txt"
    output = open(newname, "wt")

    for line in text:
        for sign in punctuation:
            line = line.replace(sign, "")
        line = line.lower()
        output.write(line)
    return newname


def remove_stopwords(file):
    sw = []
    stopwords = open(dpath + "eng_stop_words.txt")
    for stopword in stopwords:
        sw.append(stopword.replace("\n", ""))
        sw.append(stopword.replace("\n", "").upper())
        sw.append(stopword.replace("\n", "").title())

    text = open(file, "rt")

    newname = opath + file.rsplit('/')[-1].replace(".txt", "") + "_nostop.txt"
    output = open(newname, "wt")

    for line in text:
        for w in sw:
            line = re.sub(r'\b' + w + r'\b', "", line)
            line = re.sub(' +', ' ', line)
            line = line.strip()
        output.write(line + "\n")
    return newname


def tokenize_text(file):
    text = open(file, "rt")
    words = []

    for line in text:
        words.append(line.split())

    words = sum(words, [])
    return words

# get_speaker_text(
#     "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/NewAtlantis.txt"
# )
#
# normalize_text(
#     "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/processed/NewAtlantis_getspeaker.txt"
# )
# remove_stopwords(
#     "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/processed/NewAtlantis_getspeaker_normal.txt"
# )
# preprocessed = tokenize_text(
#     "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/processed/NewAtlantis_getspeaker_normal_nostop.txt"
# )
# print(preprocessed)
