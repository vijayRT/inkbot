import gnp
import sys

#sys.path.append('/home/vijay/.local/lib/python3.5/site-packages')
import newspaper
from newspaper import Article



from os import listdir
from os.path import isfile, join



onlyfiles = [f for f in listdir('trends')]
for  filename in onlyfiles:
    print(filename + ':\n\n')
    filepath = join('trends', filename)
    with open(filepath) as fname:
        trends = fname.readlines()
        trends = [x.strip() for x in trends]
    for trend in trends:
        url = gnp.get_google_news_query(trend)['stories'][0]['link']
        a = Article(url)
        a.download()
        a.parse()
        print(trend + " :\n" + a.text + "\n")
    

        
