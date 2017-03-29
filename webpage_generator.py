# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import os
from os import listdir
from os.path import isfile, join
import sys
import time

import shutil



filelist = [ f for f in os.listdir("html_files") if f.endswith(".html") ]
for f in filelist:
    os.remove(join('html_files', f))
    
t0 = time.time()

#country_list =  ['Australia', 'Canada', 'India', 'USA', 'UK']
file_list = [f for f in listdir('articles')]
for f in file_list:
    filepath = join('articles', f)
    with open(filepath, 'r') as json_file:
        json_content = json.load(json_file)
        for i in range (0, 10):
            try:
                x = str(i)
                html_name = json_content[x]['category'] + '_' + json_content[x]['trend'] + '.html'
                html_file_name = join('html_files', html_name)
                html_file = open(html_file_name, 'w')
                




                
                html_str = """
<!DOCTYPE html>
<html>
<head><title>"""
                html_file.write(html_str.encode('utf8'))
                html_str = json_content[x]['title']
                html_file.write(html_str.encode('utf8'))

                html_str = """</title>
<meta charset="utf-8">
<script id="twitter-wjs" type="text/javascript" async defer src="http://platform.twitter.com/widgets.js"></script>
<link rel= "stylesheet" type ="text/css" href="inkbot.css">
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
  
<div class="article">
  

	<div class="newstitle"><h2>
                
                """




                
                html_file.write(html_str.encode('utf8'))
                html_str = json_content[x]['title']
                html_file.write(html_str.encode('utf8'))



                
                html_str = """
                </h2></div><br>
                
   	<img src=\"
    """
                html_file.write(html_str.encode('utf-8'))
                html_str = json_content[x]['image']
                html_file.write(html_str)
                html_str = """
                \" width="75%" height="75%"><br>
  <p class="newsbody"><b><i>"""
                html_file.write(html_str.encode('utf8'))
                html_str = str(f)
                html_file.write(html_str.encode('utf8'))
                html_str = """:</i></b>
  """

                html_file.write(html_str.encode('utf8'))
                html_str = json_content[x]['summary']
                html_file.write(html_str.encode('utf8'))
                html_str = """</p>"""
                html_str = json_content[x]['tweet']
                html_file.write(html_str.encode('utf8'))
                
                html_file.close()
            
            except Exception as e:
                print('')


