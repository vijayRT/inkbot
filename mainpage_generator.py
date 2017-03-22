from __future__ import unicode_literals

import json
import os
from os import listdir
from os.path import isfile, join
import sys
import time
import random
from bs4 import BeautifulSoup

import shutil
index_file = open(join('html_files', 'index.html'), 'w')

html_str = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script id="twitter-wjs" type="text/javascript" async defer src="http://platform.twitter.com/widgets.js"></script>
<link rel= "stylesheet" type ="text/css" href="inkbot.css">
<body>


<div class="container">

<header>
   <h1>INKBOT</h1>
<div class="btn-group">
  <button class="button">Entertainment</button>
  <button class="button">Politics</button>
  <button class="button">Sports</button>
  <button class="button">Home</button>

</div></header>

"""

for i in range(0, 5):
    file_chosen = open(join('html_files', random.choice(os.listdir('html_files'))), 'r')
    soup = BeautifulSoup(file_chosen)
    title = soup.title.string
    print(title)


    
