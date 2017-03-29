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

def simple_max(a, b, c):
    if a>b>c:
        return 'a'
    elif b>c:
        return 'b'
    else:
        return 'c'






        

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








#Summarizer




class FrequencySummarizer:
    def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut
        self._max_cut = max_cut 
        self._stopwords = set(stopwords.words('english') + list(punctuation))

    def compute_frequencies(self, word_sent):
        freq = defaultdict(int)
        for s in word_sent:
          for word in s:
            if word not in self._stopwords:
              freq[word] += 1
        # frequencies normalization and fitering
        m = float(max(freq.values()))
        for w in freq.keys():
          freq[w] = freq[w]/m
          if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
            del freq[w]
        return freq

    def summarize(self, text, n):
        sents = sent_tokenize(text)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        assert n <= len(sents)
        self._freq = self.compute_frequencies(word_sent)
        ranking = defaultdict(int)
        for i,sent in enumerate(word_sent):
          for w in sent:
            if w in self._freq:
              ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking, n)    
        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):
        return nlargest(n, ranking, key=ranking.get)






#main execution
fs = FrequencySummarizer()
files = [f for f in listdir('articles')]
for f in files:
    filepath = join('articles', f)
    with open(filepath, 'r') as json_file:
        json_data = json.load(json_file)
        print(f)
        for i in range (0, 10):
            try:
                x = str(i)
                print(json_data[x]['title'])
                b0 = json_data[x]['body0']
                b1 = json_data[x]['body1']
                b2 = json_data[x]['body2']
                a = cosine_sim(b0, b1)
                b = cosine_sim(b1, b2)
                c = cosine_sim(b0, b2)
                m = simple_max(a, b, c)
                if m == 'a':
                    tts= b0 + b1
                elif m == 'b':
                    tts = b1 + b2
                else:
                    tts = b0 + b2
                summ_str = ''
                for s in fs.summarize(tts, 8):
                    summ_str += str(s)
                    summ_str += str('\n')
                print(summ_str)
                json_data[x]['summary'] = summ_str
                print("\n\n")
            except Exception as e:
                print(None)
    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent = 4) 
            
t1 = time.time()
print(t1 - t0)
                
