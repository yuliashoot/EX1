from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
import string
import csv

TEXT = "text"


class IR:
    documents = {}
    inverted = {}

    def __init__(self):
        self.documents = self.load_data()

    # function that generates dict with indexes as keys and text as values - Q1
    def load_data(self):
        print("Loading the data")
        data = {}
        all_tweets = []
        f = open("tweets.csv", encoding='utf-8')
        tweet_rows = csv.DictReader(f)
        # taking only the tweet text out of the rows
        for row in tweet_rows:
            all_tweets.append(row[TEXT])

        marker = 0
        length = len(all_tweets)
        # splittig all the tweets to 100 documents.
        for index, ge in enumerate(range(round(length / 100), length, round(length / 100)), 1):
            # slicing only 1/100 of the tweets each time
            document = all_tweets[marker:ge]

            # joining the tweets into one document
            data[index] = " ".join(document)

            # move the marker to the last tweet position
            marker = ge

        return data

    # Function gets raw text and returned tokenized word list - + Q2 + Q6
    def tokenize(self, raw_text):

        # lower case - 2A
        raw_text = raw_text.lower()

        # Normalization - 2D
        raw_text = self.normalization(raw_text)

        # create translate table
        translator = raw_text.maketrans('', '', string.punctuation)

        # remove punctuation and split to words
        word_tokens = word_tokenize(raw_text.translate(translator))

        # remove stop words - 2B
        stop_words = set(stopwords.words('english'))

        filtered_text = [word for word in word_tokens if not word in stop_words]

        # stemming 2C
        ps = PorterStemmer()
        tokenized_words = [ps.stem(word) for word in filtered_text]

        return tokenized_words

    def normalization(self, raw_text):
        # Normalization dict
        abbrevs = {
            'president of the united states': 'potus',
            'united states of america':'usa'}

        for abbrev in abbrevs:
            raw_text = raw_text.replace(abbrev, abbrevs[abbrev])
        return raw_text

    # Build inverted index from indexes - Q3
    def build_inverted_index(self):
        temp_inverted = {}

        for index, raw_text in self.documents.items():
            # Get tokenized words
            tokens = self.tokenize(raw_text)
            for word in tokens:
                # If our inverted dict doesn't have this word, initiazlize a new key
                if word not in temp_inverted:
                    temp_inverted[word] = set()

                # insert the index to the inverted dict
                temp_inverted[word].add(index)

        # sort all indexes
        for word, indexes in temp_inverted.items():
            self.inverted[word] = sorted(list(temp_inverted[word]))

    # Q4
    def intersection(self, term1, term2):
        term1_after_tokenize = self.tokenize(term1)
        term2_after_tokenize = self.tokenize(term2)
        p1, p2 = 0, 0

        # the current version supports only one tokenized word intersection (or one word after normalization)
        if not len(term1_after_tokenize) == 1 or not len(term2_after_tokenize) == 1:
            return []

        index1 = self.inverted.get(term1_after_tokenize[0])
        index2 = self.inverted.get(term2_after_tokenize[0])

        # making sure both words are in the inverted index
        if not index1 or not index2:
            # incase on or more terms are not in the inverted there is no need to continue
            return []

        res_indexes = []
        while p1 < len(index1) and p2 < len(index2):
            if index1[p1] < index2[p2]:
                p1 += 1
            elif index1[p1] > index2[p2]:
                p2 += 1
            else:
                res_indexes.append(index1[p1])
                p1 += 1
                p2 += 1

        return res_indexes

    # Q5
    def get_text_from_index(self, index):
        return self.documents[index]