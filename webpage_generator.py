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
                html_name = json_content[x]['trend'] + '.html'
                html_file_name = join('html_files', html_name)
                html_file = open(html_file_name, 'w')





                
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
                html_str = """
                
</div>



<div class="newsticker">
<dl id="ticker">
      <dd>This is a snippet of the news. It could be the whole news item or it could link to another page containing...</dd>
      <dd>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</dd>
      <dd>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</dd>
      <dd>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</dd>
      <dd class="text">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</dd>    
</dl>
</div>

<div id="footer"> <div id="footerContainer"> <div id="imginthefooter"> </div> </div> </div>​​​​​​​​​
</div>

</body>
</html>
                """




                
                html_file.write(html_str.encode('utf8'))
                html_file.close()
            
            except Exception as e:
                print('')

t1 = time.time()
print(t1-t0)
