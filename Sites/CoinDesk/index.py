import re
import pandas as pd
import datetime
import urllib

class Website(object):
    """
    Uniquely gather data from website and send back to PriceHistory
    """
    def __init__(self):
        self.table = 'PriceHistory'
        self.Date  = 'FLOAT'
        self.Price = 'FLOAT'
        self.Type  = 'TEXT'
        self.Unit  = 'TEXT'
        self.Site  = 'TEXT'
        
        
        
    def execute(self):
        """
        #### CLEAN UP ####
        """
        columns = [
            'Date',
            'Price'
        ]
        
        data  = pd.DataFrame(columns = columns)
        today = datetime.date.today()
        beginning = datetime.date(2010,07,17)
        request   = 'https://api.coindesk.com/charts/data?data=close&startdate={}&enddate={}&exchanges=bpi&dev=1&index=USD'.format(beginning,today)
        
        apiData = urllib.urlopen(request).read()
        
        parsed = self.parseText(apiData)
        if parsed:
            data = pd.DataFrame(parsed,columns=columns)
            data['Type']    = 'Bitcoin'
            data['Unit']    = 'USD'
            data['Site'] = 'CoinDesk'
    
        return data
    
    
    
    
    def parseText(self,text):
        clean = []
        newText = re.findall('\[(.*?)\]',text)
        for item in newText:
            date, price = item.strip('][').split(',')
            date  = datetime.date.fromtimestamp(float(date) / 1000)
            price = float(price)
            clean.append([date,price])

        return clean