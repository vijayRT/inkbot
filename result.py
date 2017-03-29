import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from os.path import join
from os import listdir
import json
import sys
import time

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

reload(sys)
sys.setdefaultencoding('utf-8')

t0 = time.time()


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

filelist = [f for f in listdir('trends')]
for file_name in filelist:
    f1 = open(join('old_trends', file_name), 'r')
    f1_str = f1.read().replace('\n', '')
    f2 = open(join('trends', file_name), 'r')
    f2_str = f2.read().replace('\n', '')
    print(file_name)
    print(cosine_sim(f1_str, f2_str))
