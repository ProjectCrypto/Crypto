
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Website(object):
    """
    Uniquely gather data from website and send back to NewsHistory
    
    ### TO DO
    
        This needs to clean text to add back to driver. Driver will do analysis then pass to main.py
    
    
    """
    def __init__(self):
        self.table = 'NewsHistory'
        self.Site  = 'TEXT'
        self.Text  = 'TEXT'
        self.Date  = 'FLOAT'
        self.Title = 'TEXT'
        
    def execute(self):
        url = 'https://www.cryptocoinsnews.com/'
        links = []
        data = requests.get(url).text
        soup = BeautifulSoup(data,'lxml')
        for link in soup.find_all('a',class_='grid-thumb-image'):
            title = link['title']
            href  = link['href']
            links.append((title,href))

            
        self.parseText(links)

        return pd.DataFrame()


    def parseText(self,links):
        for item in links:
            break
            #import pdb;pdb.set_trace()