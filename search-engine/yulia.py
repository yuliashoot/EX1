import os, glob, string, re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation


def remove_punctuations(file):
    exclude = set(string.punctuation)
    # remove punctuations
    file = ''.join(character for character in file if character not in exclude)
    # standardize white space
    file = re.sub(r'\s+', ' ', file)

    return file


def remove_stop_words(file):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(file)
    wordsFiltered = []
    for w in words:
        if w not in stop_words:
            wordsFiltered.append(w)
    return wordsFiltered


path = os.getcwd()  # this is the current direction of the files
for filename in glob.glob(
        os.path.join(path, "*.txt")):  # you can use other format not just txt (but all have to vw the same)
    with open(filename, 'r') as f:
        content = f.read()
        without_punctuations = remove_punctuations(content)
        without_stop_word = remove_stop_words(without_punctuations)

        print(without_stop_word)  # this is for now what i did,just print to see the result
