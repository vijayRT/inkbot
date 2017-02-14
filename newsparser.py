import gnp
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

#sys.path.append('/home/vijay/.local/lib/python3.5/site-packages')
import newspaper
from newspaper import Article



from os import listdir
from os.path import isfile, join



onlyfiles = [f for f in listdir('trends')]
for  filename in onlyfiles:
    print(filename + ':\n\n')
    filepath = join('trends', filename)
    jsonpath  = join('articles', filename)
    with open(filepath) as fname:
        trends = fname.readlines()
        trends = [x.strip() for x in trends]
        with open(jsonpath, 'w') as jsonfile:
            for trend in trends:
                art_json = {'title' : None, 'body':['a', 'b', 'c']}
                art_json['title'] = trend
                print(trend)
                for i in range(0,2):
                    url = gnp.get_google_news_query(trend)['stories'][i]['link']
                    a = Article(url)
                    a.download()
                    a.parse()
                    art_json['body'][i] = a.text
                    print(url + "\n")
                json.dump(art_json, jsonfile, ensure_ascii = False, indent = 4)
           
                
                
            
