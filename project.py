import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
def scrap_top_list():
    url='https://www.imdb.com/india/top-rated-indian-movies//'
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    a=soup.find('tbody',class_='lister-list')
    b=a.find_all('tr')
    c=[]
    for i in b:
        movie_detail={}
        movie_link=i.find('td',class_="titleColumn").a['href']
        link='https://www.imdb.com'+movie_link
        movie_detail["link"]=link
        c.append(movie_detail)
       
    file=open('Movies_Detail.json','w')
    w=json.dump(c,file,indent=4)
    return c
top_movie=scrap_top_list()