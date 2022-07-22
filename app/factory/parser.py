"""Parsing input file and generating html_dict"""

import itertools


class Parser():
    """Input file parser"""
    
    def __init__(self, file):
        self.file = file
        self.html_dict={"title":None, 
                        "category":None, 
                        "intro":None,
                        "content":[]}
           
    def generator_list(self):
        """Reading input file and returning generator indexing content line by line"""
        
        with open(self.file, 'r') as f:
            for index, line in enumerate(f):
                yield index, line

    def append_htlm_dict_content(self, type, content):
        '''appending content to html_dict'''
        self.html_dict['content'].append([type, content])
        
    def update_html_dict(self, key, value):
        '''updating html_dict'''
        self.html_dict[key] = value
        
    def get_html_dict(self):
        '''getting html_dict'''
        return self.parse()

    def parse(self, current_index=0):
        """recursively parsing generator_list and appending html_dict"""
        
        limit = len(list(self.generator_list())) -1
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):

            line = line.replace('\n','').replace('\\n','<br>')
            
            type = None
            content = None
         
            if line.startswith( 'title:'):
                self.update_html_dict("title", line[6:].strip())
            
            elif line.startswith( 'category:'):
                self.update_html_dict("category", self.get_category(line))
                
            elif line.startswith( 'intro:'):
                self.update_html_dict("intro", self.get_intro(index)[0])
                
            elif line=='' or line==None:
                type='br'
                content='<br>'
            
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
                
            elif line.startswith( 'link:'):
                type='link'
                content=self.get_link(line)
                
            else:
                type='paragraph'
                data=self.get_paragraph(index)
                if data:
                    content=data[0]
                    current_index=data[1]
                    
            if type and content:
                self.append_htlm_dict_content(type, content)
            
            if index == limit:
                return self.html_dict
            
            return self.parse(current_index+1)

    def get_category(self, line):
        '''getting category elements'''
        line=line.replace('<br>','')
        return line[10:].strip().split(' ')
    
    def get_intro(self, current_index, accumulated_data=''):
        '''getting intro elements'''
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):
            
            line = line.replace('\n','').strip()
            line = line.lstrip('intro: ').strip()
            
            if line=='':
                return accumulated_data, index
            else:
                accumulated_data += line
                return self.get_intro(index+1, accumulated_data)
        
        return accumulated_data, current_index + 1                

    def get_code(self, current_index, accumulated_data=''):
        '''recusively finding code content'''
        
        for index, line in itertools.islice(self.generator_list(), current_index + 1, None):
            
            line = line.replace('\n','<br>').replace('\\n','<br>')
            
            if line.startswith('```'):
                return accumulated_data, index
            else:
                    accumulated_data += line
                    return self.get_code(index + 1, accumulated_data)
                
    def get_link(self, line):
        '''getting link elements'''
        return line[6:].lstrip('[').rstrip(']').strip().split(', ')

        
    def get_paragraph(self, current_index, accumulated_data=''):
        '''recursively finding paragraph content'''
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):
            
            line = line.replace('\n','').strip()
            
            if line=='':
                return accumulated_data, index
            else:
                    accumulated_data += line
                    return self.get_paragraph(index+1, accumulated_data)
        
        return accumulated_data, current_index + 1

                        
                    
                
                
                
        