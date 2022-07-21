"""Parsing input file and generating html_list"""
import itertools


class Parser():
    """Input file parser"""
    
    def __init__(self, file):
        self.file = file
        self.html_list = []
           
    def start_html_list(self):
        self.html_list.append('{% extends "base.html" %}')
        self.html_list.append('{% block content %}')
        
    def end_html_list(self):
        self.html_list.append('{% endblock %}')

    def generator_list(self):
        """Parsing input file and returning generator
        indexing content line by line"""
        
        with open(self.file, 'r') as f:
            for index, line in enumerate(f):
                yield index, line

    def parse(self, current_index=1):
        """recursively parsing generator_list
        and appending html_list"""
        
        limit = len(list(self.generator_list())) -1
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):

            line = line.replace('\n','<br>').replace('\\n','<br>')
            
            content=None
          
            if line.startswith( 'title:'):
                type='title'
                content=line[6:].strip()
            
            elif line.startswith( 'category:'):
                type='category'
                content=line[9:].split(' ')
                
            elif line.startswith( '### '):
                type='h3'
                content=line[3:].strip()
                
            elif line.startswith( '## '):
                type='h2'
                content=line[2:].strip()
                
            elif line.startswith('# '):
                type='h1'
                content=line[1:].strip()
                
            elif line.startswith( '```python'):
                type='code'
                data = self.get_code(index + 1)
                if data:
                    content=data[0]
                    current_index = data[1]
                
            elif line.startswith( 'intro:'):
                type='intro'
                data=self.get_intro(index)
                if data:
                    content=data[0]
                    current_index=data[1]
            
            elif line.startswith( 'link:'):
                type='link'
                data=self.get_link(index)
                if data:
                    content=data[0]    
                    current_index=data[1]
                
            elif line=='<br>' or line=='':
                type='br'
                content='<br>'
            
            else:
                type='paragraph'
                data=self.get_paragraph(index)
                if data:
                    content=data[0]
                    current_index=data[1]
                    
            if type and content:
                self.html_list.append((type, content))
            
            if index == limit:
                return self.html_list
            
            return self.parse(current_index+1)

    def get_code(self, current_index, accumulated_data=''):
        '''recusively finding code content'''
        
        for index, line in itertools.islice(self.generator_list(), current_index + 1, None):
            
            line = line.replace('\n','<br>').replace('\\n','<br>')
            
            if line.startswith('```'):
                return accumulated_data, index
            else:
                    accumulated_data += line
                    return self.get_code(index, accumulated_data)
        
    def get_link(self, current_index):
        '''getting link elements'''
        
        for index, line in itertools.islice(self.generator_list(), current_index + 1, 1):
                data = line[6:]
                data = data.lstrip('[').rstrip(']').strip()
                return data, index
        
    def get_paragraph(self, current_index, accumulated_data=''):
        '''recursively finding paragraph content'''
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):
            
            line = line.replace('\n','<br>').replace('\\n','<br>')
            
            if line=='<br>' or line=='':
                return accumulated_data + '<br>', index
            else:
                    accumulated_data += line
                    return self.get_paragraph(index+1, accumulated_data)
        
        return accumulated_data, current_index

    def get_intro(self, current_index, accumulated_data=''):
        '''getting intro elements'''
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):
            
            line = line.replace('\n','<br>').replace('\\n','<br>').lstrip('intro: ')
            
            if line=='<br>':
                return accumulated_data + '<br>', index
            else:
                accumulated_data += line
                return self.get_intro(index+1, accumulated_data)
                        
                        
                    
                
                
                
        