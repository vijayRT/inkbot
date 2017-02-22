import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from os.path import join
from os import listdir
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


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

files = [f for f in listdir('articles')]
for f in files:
    filepath = join('articles', f)
    with open(filepath, 'r') as json_file:
        json_data = json.load(json_file)
        print(f)
        for i in range (0, 10):
            x = str(i)
            print(json_data[x]['title'])
            print (cosine_sim(json_data[x]['body0'], json_data[x]['body1']))
            print (cosine_sim(json_data[x]['body1'], json_data[x]['body2']))
            print (cosine_sim(json_data[x]['body0'], json_data[x]['body2']))
            print('\n')
