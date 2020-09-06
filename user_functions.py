import requests
import pymysql
import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import pymysql
import config
from sqlalchemy import create_engine

def get_top_links(resp):
    #print(resp.url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        print("came")
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
    return results[:5]

def send_to_mysql(searchstring,username):
    data={}
    sql_connection =  create_engine('mysql+pymysql://'+config.USER+':'+config.PASSWORD+'@'+config.SERVER+':'+config.PORT+'/'+config.DBNAME,echo=False)
    data['searchkeyword']=str(searchstring)
    data['userid']=str(username)
    #data['results']=results
    df = pd.DataFrame(data,index=[0])
    df.to_sql(name=config.DBTABLE, con=sql_connection, if_exists = 'append', index=False)
    if(sql_connection):
        sql_connection.dispose()
    del df
    return 1