
import os
import pandas as pd

from matplotlib import pyplot as plt


class Analysis(object):
    def __init__(self):
        pass
        
    def execute(self,parent):
        query = """
            SELECT * FROM NewsHistory
        """
        data = parent.execute(query)
        
        for index, group in data.iterrows():
            sentences = group['Content'].split('.')
            #import pdb;pdb.set_trace()
        
        
        
if __name__ == "__main__":
    Analysis()