################################################
#### Programing for Data Scientists: Python ####
####              Assignment 05             ####
####             by Leon Löppert            ####
################################################

# Task 02 - Classes ----

# The Baconian theory holds that Sir Francis Bacon is the author of Shakespeare’s plays.
# We want to perform a very simple stylistic analysis between Shakespeare’s play Macbeth and Bacon’s New Atlantis.
# We check for words that frequently occur in both documents to see whether there are characteristic words that co-occur
# in the texts, which might give some support to the theory.
#
# Your Task:
#
# 1. Download and pre-process the texts as follows:

# New Atlantis
# - get_speaker_text()
# - normalize_text()
# - remove_stopwords()
# - tokenize_text()

# Macbeth
#
# - get_speaker_text()
# - normalize_text()
# - utils_ocr.correct_ocr_errors() – we will provide a function to deal with OCR errors.
# - remove_stopwords()
# - tokenize_text()

# 2. For the pre-processed texts, compute the list of word co-occurrence frequencies, i.e. which words occur in both documents and how often. Use the format:
# [term , frequency_doc1 , frequency_doc2 , sum_of_frequencies]
# Sort the list according to the sum of the frequencies in descending order.

# 3. Use the csv library to store the ordered word co-occurrence frequency list in a CSV file. You can zip the csv and upload it to GitHub.


import os
import re
import sys
import shutil
import numpy as np
import pandas as pd
import csv
import zipfile

sys.path.insert(0, 'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/')
from task_01 import get_speaker_text
from task_01 import normalize_text
from task_01 import remove_stopwords
from task_01 import tokenize_text

# 1.1 Download:
sys.path.insert(0, 'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_04/task_05_06')
from task_06 import download_file

dpath = "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/"
opath = "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/processed/"
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

# 1.2 Preprocessing:
sys.path.insert(0, 'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data')
from utils_ocr import correct_ocr_errors


def coe(file):
    newname = opath + file.rsplit('/')[-1].replace(".txt", "") + "_coe.txt"
    output = open(newname, "wt")
    for line in open(file):
        line = correct_ocr_errors(line)
        output.write(line)
    return newname


def preprocess_text(file):
    out = get_speaker_text(file)
    out = normalize_text(out)
    if file.rsplit("/")[-1] == "MacBeth.txt":
        out = coe(out)
    out = remove_stopwords(out)
    newout = "/".join(out.rsplit("/")[0:-1]) + "/" + file.rsplit("/")[-1].replace(".txt", "") + "_preprocessed.txt"
    shutil.copy(out, newout)
    return tokenize_text(out)


preporcessed_MB = preprocess_text(
    "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/MacBeth.txt")
print(preporcessed_MB)

preporcessed_NA = preprocess_text(
    "C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/NewAtlantis.txt")
print(preporcessed_NA)

# 2.1: As a pandas DataFrame:

MB_dict = {}
for word in preporcessed_MB:
    if word in MB_dict:
        MB_dict[word] += 1

    else:
        MB_dict[word] = 1
print(MB_dict)

NA_dict = {}
for word in preporcessed_NA:
    if word in NA_dict:
        NA_dict[word] += 1

    else:
        NA_dict[word] = 1
print(NA_dict)

intersection = NA_dict.keys() & MB_dict.keys()
sumfq = {w: NA_dict.get(w, 0) + MB_dict.get(w, 0) for w in intersection}

print(np.array([sumfq.keys(),
                {k: MB_dict.get(k, None) for k in list(intersection)},
                {k: NA_dict.get(k, None) for k in list(intersection)},
                sumfq.values()]))

occurences = pd.DataFrame(
    {"term": sumfq.keys(), "frequency_doc1": {k: MB_dict.get(k, None) for k in list(intersection)}.values(),
     "frequency_doc2": {k: NA_dict.get(k, None) for k in list(intersection)}.values(),
     "sum_of_frequencies": sumfq.values()})

occurences = occurences.sort_values("sum_of_frequencies", ascending=False)
print(occurences)

# 2.2 As a list of lists:
occurences2 = []

for i in range(len(intersection)):
    dummy = []
    dummy.append(list(sumfq.keys())[i])
    dummy.append(list({k: MB_dict.get(k, None) for k in list(intersection)}.values())[i])
    dummy.append(list({k: NA_dict.get(k, None) for k in list(intersection)}.values())[i])
    dummy.append(list(sumfq.values())[i])
    occurences2.append(dummy)

occurences2 = sorted(occurences2, key=lambda x: x[3], reverse=True)
print(occurences2)

# 3.1 Export as CSV:
names = ["term", "frequency_doc1", "frequency_doc2", "sum_of_frequencies"]

with open(
        'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/frequencies/co_occ_freq.csv',
        'w', newline='') as new_file:
    write = csv.writer(new_file)

    write.writerow(names)
    write.writerows(occurences2)

# 3.2 Zip file:
zipfile.ZipFile(
    'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/frequencies/co_occ_freq.zip',
    mode='w').write(
    'C:/Users/Work/PycharmProjects/AngStHasen/assignment/04_Leon_Löppert/assignment_05/data/frequencies/co_occ_freq.csv',
    arcname='co_occ_freq.csv')
