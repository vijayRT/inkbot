# -*- coding: utf-8 -*-

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
img_urls = []
titles = []

html_str = """
<!DOCTYPE html>
<html>
<head>
<title>Inkbot: Interestingly Inhuman</title>
<meta charset="utf-8">
<script id="twitter-wjs" type="text/javascript" async defer src="http://platform.twitter.com/widgets.js"></script>
<link rel= "stylesheet" type ="text/css" href="style.css">
<link rel="shortcut icon" href="inkpot.ico" type="image/x-icon">
</head>
<body>


<div class="container">

<header>
   <h1>INKBOT</h1>
<div class="btn-group">
  <a href = "misc.html"><button class="button">Miscellaneous</button></a>
      <a href = "tech.html"><button class="button">Technology</button></a>
      <a href = "ent.html"><button class="button">Entertainment</button></a>
      <a href = "sport.html"><button class="button">Sports</button></a>
      <a href = "pol.html"><button class="button">Politics</button></a>
      <a href = "index.html"><button class="button">Home</button></a>

</div></header>

"""

index_file.write(html_str.encode('utf8'))
randomfiles = []
i = 0
randomfiles = [x for x in os.listdir('html_files') if x.endswith(".html")]
randomfiles.remove('index.html')
random.shuffle(randomfiles)
while i <= 5:
    file_chosen = open(join('html_files', randomfiles[i]), 'r')
    soup = BeautifulSoup(file_chosen, "lxml")
    try:
        title = soup.title.string
        print(title)
        titles.append(title)
        imgs = soup.findAll("img")
        for img in imgs:
            img_url = img["src"]
            print(str(img_url))
            img_urls.append(str(img_url))
    except Exception as e:
        print(e)
    i+=1
    
    


html_str = """

<body>
<div id="body">
    <!-- BEGIN content -->
    <div id="content">
      <!-- begin featured -->
      <div class="featured">
        <div class="thumb"> <a href=" """
index_file.write(html_str.encode('utf8'))
html_str = str(randomfiles[0])
index_file.write(html_str.encode('utf8'))
html_str = """

        "><img src="

        """
index_file.write(html_str.encode('utf8'))
html_str = img_urls[0]
index_file.write(html_str.encode('utf8'))
html_str = """

" alt="" /></a>
<div class="text">

            <p>"""
index_file.write(html_str.encode('utf8'))
html_str = titles[0]
index_file.write(html_str.encode('utf8'))
html_str =  """</p>
          </div>
        </div>
      </div>
      <hr>
      """
index_file.write(html_str.encode('utf8'))
for i in range(1,5):
    html_str = """
       
    <div class="f post"> <a href=" """
    index_file.write(html_str.encode('utf8'))
    html_str = str(randomfiles[i])
    index_file.write(html_str.encode('utf8'))
    html_str = """
"><img src="
    """
    index_file.write(html_str.encode('utf8'))
    html_str = img_urls[i]
    index_file.write(html_str.encode('utf8'))
    html_str = """
    " alt="" />
        <p>"""
    index_file.write(html_str.encode('utf8'))
    html_str = titles[i]
    index_file.write(html_str.encode('utf8'))
    html_str = """</p></a>
    </div>
    <hr>
    """
    index_file.write(html_str.encode('utf8'))
    

    

    
html_str = """</div>
    </div>
    </body>
    </html>
    """

index_file.write(html_str.encode('utf8'))

index_file.close()


print('mainpage written')



filelist = [ f for f in os.listdir("html_files") if f.endswith(".html")]
filelist.remove('index.html')
for f in filelist:
    if not str(f) == "index.html":
        with open(join('html_files', f), 'a') as hf:
            html_str = """
                    
    </div>



    <div class="newsticker">
    <dl id="ticker">
    """
            hf.write(html_str.encode('utf8'))
            for i in range (len(titles)):
                html_str = """<dd><a href =" """
                hf.write(html_str.encode('utf8'))
                html_str = str(randomfiles[i])
                hf.write(html_str.encode('utf8'))
                html_str = """">"""
                hf.write(html_str.encode('utf8'))
                html_str = titles[i]
                hf.write(html_str.encode('utf8'))
                html_str = """</a></dd>"""
                hf.write(html_str.encode('utf8'))
             
            html_str = "</dl></div>​​​​​​​​​</div></body></html>"
            hf.write(html_str.encode('utf8'))

    
    

