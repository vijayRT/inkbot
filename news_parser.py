import gnp
import sys
import json
import re
import pickle
import time



reload(sys)
sys.setdefaultencoding('utf-8')
t0 = time.time()
#sys.path.append('/home/vijay/.local/lib/python3.5/site-packages')
import newspaper
from newspaper import Article
from newspaper import Config

conf = Config()
conf.skip_bad_cleaner = True




from os import listdir
from os.path import isfile, join


pattern=re.compile("[^\w']")
onlyfiles = [f for f in listdir('trends')]


for  filename in onlyfiles:
    print(filename + ':\n\n')
    filepath = join('trends', filename)
    jsonpath  = join('articles', filename)
    urlpath = join('urls', filename)
    
    with open(filepath) as fname:
        trends = fname.readlines()
        trends = [x.strip() for x in trends]
        art_json = {}
        json_all = {}

        
        with open(urlpath, 'r') as uname:
            u = eval(uname.read())
            k = 0
            for trend in trends:
                url_list = u[k]
                art_body = ['', '', '']
                for i in range(0,3):
                    try:
                        url = url_list[i]
                        a = Article(url, config=conf)
                        a.download()
                        a.parse()
                        #a.text = pattern.sub(' ', a.text)
                        art_body[i] = a.text
                    except Exception as e:
                        print(str(e))
                        i -= 1
                art_json = {
                'trend': trend,
                'title': a.title,
                'image': a.top_image,
                'body0': art_body[0],
                'body1': art_body[1],
                'body2': art_body[2],
                'summary': '',
                'category': '',
                 'tweet': ''   
                    }
                print(json.dumps(art_json, indent=4))
                json_all[k] = art_json
                k+=1
                
        with open(jsonpath, 'w') as jsonfile:
            json.dump(json_all, jsonfile, indent = 4)
            
                
            
t1 = time.time()
print(t1-t0)
