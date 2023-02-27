import urllib
import ssl
import os
import pandas as pd
import time
import random
import glob
import csv
import re
from bs4 import BeautifulSoup
df2 = []
for y1 in range(1,40):
    path="stock_data\\"
    page = str(y1)
    url = "https://kabuoji3.com/ranking/?date=2018-01-01&type=3&market=2&page="+page+"" 
    print(url)
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read() 
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(random.randrange(3,7))
    stockdata= soup.find_all("td")
    stockdata = [s.contents[0] for s in stockdata]
    stockdata = list(zip(*[iter(stockdata)]*7))
    df = pd.DataFrame(stockdata,)
    df.columns=['date','open','high','low','close','valume','colname']
    for k in df["open"]:
        k2 = k.get('href')
        df2.append(k2)    
df3 = pd.DataFrame(df2)
df3.to_csv(path+"list.csv")