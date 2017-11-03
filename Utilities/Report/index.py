
import os
from jinja2 import Environment, FilseSystemLoader

root = os.path.abspath(os.path.dirname(__file__))
 
Class Report(object):
    def __init__(self, path, name):
        self.name = name
        self.path = path
        self.html = os.path.join(path,'{}.html'.format(name.replace(' ','')))

        self.sections = []

   
    def add(self, **content):
        style={}
        if 'table' in contents:
            contents['table'] = self.table(contents.get('table'))

        if 'size' in contents:
            style['size'] = contents.pop('size')

        if 'color' in contents:
            style['color'] = contents.pop('color')

        if 'font' in contents:
            style['font'] = contents.pop('font')

        if 'style':
            contents['style'] = style


        self.sections.append(contents)



    def create(self)
        environment = Envionment(loader = FileSystemLoader(os.path.join(root,'templates')))
        template = environment.get_template(‘section.html’)
        ouput = template.render(sections = self.sections, title = self.name)

        with open(self.html,’w’) as f :
            f.write(output)



    def table(self,data):
        environment = Envionment(loader = FileSystemLoader(os.path.join(root,'templates')))
        template = environment.get_template(‘table.html’)
        ouput = template.render(sections = self.sections, title = self.name)

        with open(self.html,’w’) as f :
            f.write(output)
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            