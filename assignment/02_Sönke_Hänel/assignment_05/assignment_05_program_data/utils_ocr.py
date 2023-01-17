import re

def correct_ocr_errors(text):
    #  vowels {V}
    vowel = {"a", "e", "i", "o", "y"}
    #  consonants {C}
    cons = {"q", "w", "r", "t", "p", "s", "d", "f", "h", "j", "k", "l", "c", "x", "b", "n", "m"}

    # 'd -> ed
    text = re.sub("\'d", "ed", text)

    chars = list(text)
    for i in range(len(chars)):
        # v{C} -> u
        if chars[i] == "v" and chars[i + 1] in cons:
            chars[i] = "u"
            i += 1
        # {C,V}u{V} -> v
        if chars[i] == "u" and chars[i + 1] in vowel and chars[i - 1] != "q":
            chars[i] = "v"
            i += 1
        # {C}ne -> {C}n in verbs and some nouns
        if chars[i] == " " and chars[i - 1] == "e" and chars[i - 2] == "n" and chars[i - 3] in cons:
            chars[i - 1] = ""
    # .*esse plural in nouns and adjectives (and some infinitive forms)
    text = "".join(chars)
    text = re.sub("esse ", "ess ", text)
    # {C}ye -> {C}ie
    text = re.sub("ie\s", "y ", text)
    # ie -> y at ending
    text = re.sub("ie ", "y ", text)
    # io -> j at beginning
    text = re.sub(" iu", " ju", text)
    return text