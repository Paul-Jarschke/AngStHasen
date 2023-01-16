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

