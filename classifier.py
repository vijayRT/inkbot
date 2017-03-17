# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from textblob.classifiers import NaiveBayesClassifier

from textblob import Blobber
from textblob import TextBlob
import nltk
import os
from os.path import join
import io
import time
import unicodedata
import re

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import pdb


def whatisthis(s):
    if isinstance(s, str):
        print ("ordinary string")
    elif isinstance(s, unicode):
        print ("unicode string")
    else:
        print ("not a string")


dataset_category = [x for x in os.listdir('bbc')]
dataset = []

for dc in dataset_category:
    category_path  = join('bbc', dc)
    dataset_contents = [f for f in os.listdir(category_path)]
    for dataset_file in dataset_contents:
        data_path = join('bbc', dc, dataset_file)
        dataset_file_content = open(data_path, 'r')
        dataset_text = dataset_file_content.read()
        dataset_text = re.sub(r"\n", " ", dataset_text)
        dataset_train = (dataset_text, dc)
        dataset_file_content.close()
        dataset.append(dataset_train)
       
try:
    t0 = time.time()
    cl = nltk.NaiveBayesClassifier.train(dataset)
    t1 = time.time()
    print(t1 - t0)
    test_string = """ELHI: BlackBerry recently updated its Hub+ suite of Android apps. And now, the company has launched a new app on Android. Dubbed BlackBerry Privacy Shade, the app has been listed on Google Play Store. However, it's not available to all users just yet.
Privacy Shade is a simple app that blocks everything on the smartphone's display, except for a small window-shaped area that is under user's control. It allows users to control the visibility of sensitive content. The hidden area on the screen can be exposed by reading or typing in. It is also possible to adjust the transparency of the shade according to the surrounding environment.
Blackberry KEYone smartphone coming to India soon, price listed online
"Privacy Shade will let you read emails, messages and personal content at any time without worrying about snoopers, even if someone is looking over your shoulder. The app allows you to view private information in public places - like on the train or in a restaurant - by obscuring the parts of the screen that you're not actively viewing or using, while still allowing you to interact with the obscured parts," reads the information about the app.
If a smartphone is running Android 7.0 Nougat OS, users can add BlackBerry Privacy Shade to the device's Quick Settings. In addition, BlackBerry users can assign Privacy Shade to the Convenience Key. The app is compatible with Android 5.0 and later.
A few days after the launch of its flagship KEYone Android smartphone at MWC 2017, BlackBerry recently unveiled another handset - Aurora. For now, the smartphone is limited to Indonesia.
The company might soon launch KEYone in India, as one Indian e-tailer recently listed the smartphone with an expected price of Rs 39,999. The listing further reveals that the smartphone will come in Black colour and have a one-year warranty. The accessories will include power cable, power adapter and headset. """

    print(cl.classify(test_string))
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(e, exc_type, fname, exc_tb.tb_lineno)

