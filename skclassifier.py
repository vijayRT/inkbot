import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
import os
from os.path import join
import io
import time
import unicodedata
import pickle
import json
from os import listdir
import sys
import operator
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


d = open('dataset.txt', 'w')
dataset_category = [x for x in os.listdir('bbc')]
X_list = []
Y_train = []

print("Preparing dataset: \n")
for dc in dataset_category:
    category_path  = join('bbc', dc)
    dataset_contents = [f for f in os.listdir(category_path)]
    for dataset_file in dataset_contents:
        data_path = join('bbc', dc, dataset_file)
        dataset_file_content = open(data_path, 'r')
        dataset_text = dataset_file_content.read().decode('ascii', errors="ignore")
        X_list.append(dataset_text)
        Y_list = [dc]
        Y_train.append(Y_list)
        dataset_file_content.close()

print("Dataset prepared")


X_train = np.array(X_list)

mlb = MultiLabelBinarizer()
Y = mlb.fit_transform(Y_train)
    
classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

classifier.fit(X_train, Y)

X_test = []

files = [f for f in listdir('articles')]
print("\n\nPerforming Classification\n")
for f in files:
    filepath = join('articles', f)
    with open(filepath, 'r') as json_file:
        json_data = json.load(json_file)
        for i in range (0, 10):
            try:
                n = str(i)
                X_test = [json_data[n]['body0']]
                target_names = [x for x in os.listdir('bbc')]
                predicted = classifier.predict(X_test)
                all_labels = mlb.inverse_transform(predicted)
                cate = [x[0] for x in all_labels]
                json_data[n]['category'] = cate[0]
                print(json_data[n]['category'])
            except Exception as e:
                try:
                    json_data[n]['trend'] = 'Other'
                except Exception as y:
                    print(" ")
    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent = 4) 
