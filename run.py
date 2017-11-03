#!/Users/ericentrup/anaconda/bin/python2.7

import os
import sys
import pandas as pd
import argparse
import sqlite3
from glob import glob

from Utilities import dynamicImport

class Main(object):
    def __init__(self,args):
        self.args = args
        self.root = os.path.dirname(os.path.abspath(__file__))  
        
        self.database = self.checkDatabase(args)
        
        
    def main(self):
        """
        Loop through Analysis and run all modules.
        """
        analysisAll = glob(os.path.join(self.root,'Analysis/*'))
        for analysis in filter(os.path.isdir,analysisAll):
            message = "Performing {} analysis..."
            print message.format(os.path.basename(analysis))
            
            self.run(dynamicImport(analysis))
        
        
    def run(self,module):
        instance = module.Analysis()
        instance.execute(self)
        
        
    def checkDatabase(self,args):
        database = os.path.join(self.root,'Sqlite3.db')
        if args.update or not os.path.exists(database):
            os.system(os.path.join(self.root,'updateDb.py'))
            
        return database

            

    def execute(self,query):
        """
        Call from Analysis modules. Query database.
        
        Example:
            parent.execute('SELECT * FROM table')
        """
        with sqlite3.connect(self.database) as connection:
            return pd.read_sql(query,con = connection)
            
    def tables(self):
        """
        Call from Analysis modules. List tables in databse.
        
        Examples:
            parent.tables()
        """
        query = "SELECT name FROM sqlite_master WHERE type = 'table'"
        with sqlite3.connect(self.database) as connection:
            return pd.read_sql(query,con = connection)





if __name__ == "__main__":
    description = "Gather, clean, and present Bitcoin analysis"
    parser = argparse.ArgumentParser(description = description)
    
    parser.add_argument('-o',dest='output',default=os.getcwd(),help='Location for output.')
    parser.add_argument('-u','--update',dest='update',action='store_true',default = False,help='Update database')
    
    settings = parser.parse_args()
    
    main = Main(args = settings)
    main.main()
    print 'Finished.'