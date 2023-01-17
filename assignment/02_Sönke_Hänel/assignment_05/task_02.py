"""Task 02 – Classes

The Baconian theory holds that Sir Francis Bacon is the author of Shakespeare’s plays. We want to perform a very simple stylistic analysis between Shakespeare’s play Macbeth and Bacon’s New Atlantis.
We check for words that frequently occur in both documents to see whether there are characteristic words that co-occur in the texts, which might give some support to the theory.

Your Task:

    1. Download and pre-process the texts as follows:
    New Atlantis
        get_speaker_text()
        normalize_text()
        remove_stopwords()
        tokenize_text()

    Macbeth
        get_speaker_text()
        normalize_text()
        utils_ocr.correct_ocr_errors() – we will provide a function to deal with OCR errors.
        remove_stopwords()
        tokenize_text()

    2. For the pre-processed texts, compute the list of word co-occurrence frequencies,
    i.e. which words occur in both documents and how often. Use the format:
    [term , frequency_doc1 , frequency_doc2 , sum_of_frequencies]
    Sort the list according to the sum of the frequencies in descending order.

    3. Use the csv library to store the ordered word co-occurrence frequency list in a CSV file. You can zip the csv and upload it to GitHub.
"""
from urllib import request, error
import logging, os, re, sys, shutil
import pandas as pd

sys.path.insert(1,
                "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_04/task_05_06")
from task_05 import init_log
from task_06 import download_file

sys.path.insert(1,
                "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05")
from task_01 import get_speaker_text, normalize_text, remove_stopwords, tokenize_text
from assignment_05_program_data.utils_ocr import correct_ocr_errors
from operator import itemgetter

# 1. Download and pre-process the texts as follows:
""" New Atlantis
        get_speaker_text()
        normalize_text()
        remove_stopwords()
        tokenize_text()

    Macbeth
        get_speaker_text()
        normalize_text()
        utils_ocr.correct_ocr_errors() – we will provide a function to deal with OCR errors.
        remove_stopwords()
        tokenize_text()"""


def ocr(doc):
    # open file path for the play to be processed
    fr = open(doc)

    # open file path to write content into it:
    fw = open(doc[:-4] + "_ocr" + doc[-4:], "w")

    # apply function
    for line in fr:
        fw.write(correct_ocr_errors(line))
    fr.close()
    fw.close()


# Main block
if __name__ == "__main__":
    init_log(file_name="log_info.txt",
             file_mode='a',
             level=logging.ERROR)
    print()
    # download files
    download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt",
                  "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth.txt")
    download_file("https://ia801309.us.archive.org/24/items/newatlantis02434gut/nwatl10.txt",
                  "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis.txt")
    logging.shutdown()

    # pre-process
    # Atlantis
    get_speaker_text(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis.txt")
    normalize_text(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis_speaker_text.txt")
    remove_stopwords(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis_speaker_text_normalize.txt")
    atlantis_tokens = tokenize_text(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/newatlantis_speaker_text_normalize_removed_stopwords.txt")

    # MacBethy:
    get_speaker_text(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth.txt")
    normalize_text(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text.txt")
    ocr("C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text_normalize.txt")
    remove_stopwords(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text_normalize_ocr.txt")
    mac_beth_tokens = tokenize_text(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/macbeth_speaker_text_normalize_ocr_removed_stopwords.txt")

    """
    2. For the pre-processed texts, compute the list of word co-occurrence frequencies,
    i.e. which words occur in both documents and how often. Use the format:
    [term , frequency_doc1 , frequency_doc2 , sum_of_frequencies]
    Sort the list according to the sum of the frequencies in descending order.
    """

    # map every word of macbeth on the number of its occurrences (see assignment 02.task_03)
    dic_macbeth = {}
    for i in mac_beth_tokens:
        if i in dic_macbeth.keys():
            dic_macbeth[i] += 1
        else:
            dic_macbeth[i] = 1
    #    print(f'\n {dic_macbeth}')

    # map the every word of macbeth on the number of its occurrences (see assignment 02.task_03)
    dic_atlantis = {}
    for i in atlantis_tokens:
        if i in dic_atlantis.keys():
            dic_atlantis[i] += 1
        else:
            dic_atlantis[i] = 1
    #    print(f'\n {dic_atlantis}')

    # add the 0 occurrences
    for k in dic_macbeth.keys():
        if k not in dic_atlantis.keys():
            dic_atlantis[k] = 0
    #    print(f'\n {dic_atlantis}')

    for k in dic_atlantis.keys():
        if k not in dic_macbeth.keys():
            dic_macbeth[k] = 0
    #    print(f'\n {dic_macbeth}')

    # create a list of lists.
    term = []
    frequency_doc1 = []
    frequency_doc2 = []
    sum_of_frequencies = []

    co_occ_freq = [term, frequency_doc1, frequency_doc2, sum_of_frequencies]

    for k in dic_macbeth.keys():
        term.append(k)
        frequency_doc1.append(dic_macbeth[k])
        frequency_doc2.append(dic_atlantis[k])
        sum_of_frequencies.append(dic_macbeth[k] + dic_atlantis[k])

    # DataFrame from a dictionary
    dictionary = {
        "term": co_occ_freq[0],
        "frequency_doc1": co_occ_freq[1],
        "frequency_doc2": co_occ_freq[2],
        "sum_of_frequencies": co_occ_freq[3]
    }
    df = pd.DataFrame(dictionary)

    # sort it by the number of occurences (desc)
    df.sort_values(by=['sum_of_frequencies'], inplace=True, ascending=False)
    print(df.head())

    """3. Use the csv library to store the ordered word co-occurrence frequency list in a CSV file. 
    You can zip the csv and upload it to GitHub."""

    # export as csv
    df.to_csv(
        "C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/frequencies.csv",
        index=False)
    # export as zip
    compression_opts = dict(method='zip',
                            archive_name="frequencies.csv")
    df.to_csv("C:/Users/Soenke/OneDrive/Desktop/WiSe2022/Python/AngStHasen/assignment/02_Sönke_Hänel/assignment_05/out.zip", index=False, compression=compression_opts)
