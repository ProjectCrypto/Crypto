
import os
import pandas as pd

from matplotlib import pyplot as plt


class Analysis(object):
    def __init__(self):
        pass
        
    def execute(self,parent):
        query = """
            SELECT * FROM PriceHistory
        """
        data = parent.execute(query)
        #plt.style.use('fivethirtyeight')
        x = pd.to_datetime(data.Date)
        y = data.Price
        fig,ax = plt.subplots(figsize=(12,8))
        ax.plot(x,y,c='c')
        ax.set_title('Exchange Rate in Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price($)')
        plt.show()
        
        
        
        
if __name__ == "__main__":
    Analysis()