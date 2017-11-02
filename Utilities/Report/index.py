


class Report(object):
    def __init__(self,name,path):
        print 'report'
        
    def _table(self,data):
        raise NotImplemented
        
    def add(self,**kwargs):
        raise NotImplemented
        
        
    def create(self):
        raise NotImplemented
        
        