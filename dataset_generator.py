
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
import os
from os.path import join
import io
import time
import unicodedata
import pickle

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def whatisthis(s):
    if isinstance(s, str):
        print ("ordinary string")
    elif isinstance(s, unicode):
        print ("unicode string")
    else:
        print ("not a string")

d = open('dataset.txt', 'w')
dataset_category = [x for x in os.listdir('bbc')]
dataset = []

print("Preparing dataset: \n")
for dc in dataset_category:
    category_path  = join('bbc', dc)
    dataset_contents = [f for f in os.listdir(category_path)]
    for dataset_file in dataset_contents:
        data_path = join('bbc', dc, dataset_file)
        dataset_file_content = open(data_path, 'r')
        dataset_text = dataset_file_content.read().decode('ascii', errors="ignore")
        dataset_train = (dataset_text, dc)
        dataset.append(dataset_train)
        dataset_file_content.close()

print("Training classifier")
cl = NaiveBayesClassifier(dataset)
f = open('my_classifier.pickle', 'wb')
pickle.dump(cl, f)
f.close()



