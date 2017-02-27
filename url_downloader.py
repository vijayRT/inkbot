import gnp
import sys
import json
import re
import os

reload(sys)
sys.setdefaultencoding('utf-8')

#sys.path.append('/home/vijay/.local/lib/python3.5/site-packages')




from os import listdir
from os.path import isfile, join


pattern=re.compile("[^\w']")
onlyfiles = [f for f in listdir('trends')]


for  filename in onlyfiles:
    print(filename + ':\n\n')
    filepath = join('trends', filename)
    urlpath  = join('urls', filename)

    
    with open(filepath) as fname:
        trends = fname.readlines()
        trends = [x.strip() for x in trends]
        trend_list = []
        with open(urlpath, 'w') as urlfile:
            for trend in trends:
                print(trend)
                url_list = []
                for i in range(0,3):
                    try:
                        url = gnp.get_google_news_query(trend)['stories'][i]['link']
                        #print(url)
                        url_list.append(url)
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(e, exc_tb.tb_lineno)
                        i -= 1
                trend_list.append(url_list)
            urlfile.write(str(trend_list))
