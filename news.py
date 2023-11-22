import requests
import pandas as pd
from bs4 import BeautifulSoup

titles = []
for j in range(1, 100, 10):
    res = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%86%8D%EB%B3%B4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=32&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=' + str(j))
    soup = BeautifulSoup(res.text, 'lxml')
    title = soup.select('a.news_tit')
    for i in title:
#         print(i.text)
        titles.append(i.text)
    
    
df = pd.DataFrame({'Title': titles})
df.to_csv('News_data_new.csv', encoding = 'utf-8', index = False, mode = 'a')
