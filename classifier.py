# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from textblob.classifiers import NLTKClassifier
from textblob import Blobber
from textblob import TextBlob
import nltk
import os
from os.path import join
import io
import time
import unicodedata
import re
import pickle
import math
import sys
import codecs




def to_alphanum(s):
    import re
    pattern  =  re.compile('[\W_]+')
    return pattern.sub('', s)


dataset_category = [x for x in os.listdir('bbc')]
dataset = []

print("Preparing dataset")
for dc in dataset_category:
    category_path  = join('bbc', dc)
    dataset_contents = [f for f in os.listdir(category_path)]
    for dataset_file in dataset_contents[:50]:
        data_path = join('bbc', dc, dataset_file)
        dataset_file_content = codecs.open(data_path, 'r',encoding='utf-8', errors='ignore')
        dataset_text = dataset_file_content.read()
        to_alphanum(dataset_text)
        dataset_train = (dataset_text, dc)
        dataset_file_content.close()
        dataset.append(dataset_train)
       
try:
    print('Training Classifier')
    t0 = time.time()
    cl = NLTKClassifier(dataset)
    f = open('my_classifier.pickle', 'wb')
    pickle.dump(cl, f)
    f.close()
    t1 = time.time()
    print(t1 - t0)
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(e, exc_type, fname, exc_tb.tb_lineno)

