
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
        ax.set_title('Exchange Rate in Time',fontsize=24)
        ax.set_xlabel('Date')
        ax.set_ylabel('Price($)')
        ax.legend(loc='best',fancybox=True, shadow=True)
        
        plt.tight_layout()
        plot1 = os.path.join(parent.output,'plot1.png')
        plt.savefig(plot1, bbox_inches='tight',transparent=True)
        
        
        
        
        text = """
        Welcome to Report! An API to help mitigate the tasks in presenting
        your analysis. Add sections with header or tables and plots. I cant
        say I have everything figured out but this should help those who
        are savy with Python but not HTML. <3
        """    
        
        report = Report(name = 'Baseline', path = parent.output)
        
        report.add(header = 'Introduction', text = text)
        report.add(plot= plot1)
        report.add(header = 'Summary', table = data.head())
        
        report.create()
        
if __name__ == "__main__":
    Analysis()