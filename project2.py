from bs4 import BeautifulSoup
from project  import top_movie
import requests
import json
import psycopg2

def get_movie_list_details(move_list):
    i=0
    g=[]
    while i<=50:
        d=move_list[i]["link"]
        d1=[]
        page=requests.get(d)
        soup=BeautifulSoup(page.text,'html.parser')
        movie=soup.find("div",class_="sc-80d4314-0 fjPRnj").h1.get_text()
        d1.append(movie)
        Detail=soup.find("section",cel_widget_id="StaticFeature_Details")
        s=Detail.find_all("div")
        y=[]
        for ul in s:
                h=ul.find_all("ul")
                for li in h:
                    o=li.find_all("li")
                    for aa in o:
                        z=aa.find_all('a')
                        details=[details.get_text() for details in z]
                        for p in details:
                            y.append(p)
        b=y[1].split()
        s=b[1]+b[0]
        d1.append(s)
        i=i+1
        g.append(tuple(d1))

    return g
ss=get_movie_list_details(top_movie)
print(ss)

 
