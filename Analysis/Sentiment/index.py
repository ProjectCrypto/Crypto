
import os
import pandas as pd

from matplotlib import pyplot as plt


import nltk.classify.util
#from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import wordnet

stopwords = nltk.corpus.stopwords.words('english')

class Analysis(object):
    def __init__(self):
        pass
        
    def execute(self,parent):
        query = """
            SELECT * FROM NewsHistory
        """
        data = parent.execute(query)
        
        for index, group in data.iterrows():
            content = group['Content'].encode('ascii',errors='ignore')
            for line in sent_tokenize(content):
                tokens = self.stop_words(line)
                # Need to do something with this
               # import pdb;pdb.set_trace()
        

        
    def stop_words(self,sentence):
        lowerCase = sentence.lower()
        tokens    = word_tokenize(lowerCase)
        
        return [x for x in tokens if x not in stopwords]
        
        
if __name__ == "__main__":
    Analysis()