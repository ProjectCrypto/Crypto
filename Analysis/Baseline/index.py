
import os
import pandas as pd

from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

from Utilities import Report

class Analysis(object):
    def __init__(self):
        pass
        
    def execute(self,parent):
        query = """
            SELECT * FROM PriceHistory
        """
        data = parent.execute(query)
        x = pd.to_datetime(data.Date)
        y = data.Price
    
        fig,ax = plt.subplots(figsize=(12,8))
        ax.plot(x,y,c='c')
        ax.set_title('Exchange Rate in Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price($)')
        
        
        plt.tight_layout()
        plot1 = os.path.join(parent.output,'plot1.png')
        plt.savefig(plot1, bbox_inches='tight',transparent=True)
        
        
        report = Report(name = 'Baseline', path = parent.output)
        text = "Welcome to 'Report`! A module to help mitigate those tasks."
        report.add(header = 'Introduction', text = text)
        report.add(plot= plot1)
        report.add(header = 'Summry', table = data)
        
        report.create()
        
if __name__ == "__main__":
    Analysis()