"""Parsing input file and generating html_dict"""

import itertools

class Parser():
    """Input file parser"""
    
    def __init__(self, file):
        self.file = file
        self.html_dict={"content":[]}
        self.avoid_list=['title', 'category', 'intro', 'code', 'link', 'list']
           
    def generator_list(self):
        """Reading input file and returning generator indexing content line by line"""
        
        with open(self.file, 'r') as f:
            for index, line in enumerate(f):
                yield index, line

    def append_html_dict_content(self, type, content):
        '''appending content to html_dict'''
        self.html_dict['content'].append([type, content])
        
    def update_html_dict(self, key, value):
        '''updating html_dict'''
        self.html_dict[key] = value
        
    def get_html_dict(self):
        '''getting html_dict'''
        return self.parse()
    
    def type_line(self, line):
        '''returning line type'''
        if line.startswith('title:'):
            return 'title'
        elif line.startswith('category:'):
            return 'category'
        elif line.startswith('intro:'):
            return 'intro'
        elif line.startswith('code:'):
            return 'code'
        elif line.startswith('link:'):
            return 'link'
        elif line.startswith('### '):
            return 'title3'
        elif line.startswith('## '):
            return 'title2'
        elif line.startswith('# '):
            return 'title1'
        elif line.startswith('list:'):
            return 'list'
        elif line =='':
            return 'end'
        else:
            return 'paragraph'

    def parse(self, current_index=0):
        """recursively parsing generator_list and appending html_dict"""
        
        limit = len(list(self.generator_list()))
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):

            line = line.replace('\n','').replace('\\n','<br>')
            
            type = None
            content = None
            
            match self.type_line(line):
         
                case 'title':
                    self.update_html_dict("title", line[6:].strip())
                
                case 'category':
                    self.update_html_dict("category", self.get_category(line))
                    
                case 'intro':
                    self.update_html_dict("intro", self.get_intro(index)[0])

                case 'title3':
                    type='title'
                    content=(line[3:].strip(), 3)
                    
                case 'title2':
                    type='title'
                    content=(line[2:].strip(), 2)
                    
                case 'title1':
                    type='title'
                    content=(line[1:].strip(),1)
                    
                case 'code':
                    type='code'
                    data = self.get_code(index + 1)
                    if data:
                        content=data[0]
                        current_index = data[1]
                    
                case 'link':
                    type='link'
                    content=self.get_link(line)
                    
                case 'list':
                    type='list'
                    content=self.get_list(line)
                    
                case 'end':
                    type='br'
                    content=''
                    
                case _:    
                    type='paragraph'
                    data=self.get_paragraph(index)
                    if data:
                        content=data[0]
                        current_index=data[1]
                    
            if type and content:
                self.append_html_dict_content(type, content)
            
            return self.parse(current_index+1)
        
        return self.html_dict

    def get_category(self, line):
        '''getting category elements'''
        line=line.replace('<br>','')
        return line[10:].strip().split(' ')
    
    def get_intro(self, current_index):
        '''getting intro elements'''
        
        accumulated_data = ''
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):
            
            line = line.replace('\n','').strip()
            line = line.lstrip('intro: ').strip()
            
            if self.type_line(line)=='end' or self.type_line(line) in self.avoid_list:
                return accumulated_data, index

            accumulated_data += line

        return accumulated_data, current_index

    def get_code(self, current_index):
        '''recursively getting code content'''
        
        accumulated_data = ''
        
        for index, line in itertools.islice(self.generator_list(), current_index + 1, None):
            
            line = line.replace('\n','<br>').replace('\\n','<br>')
            
            if line.startswith('code_'):
                return accumulated_data, index + 1
            
            accumulated_data += line
            
        return accumulated_data, current_index
                
    def get_link(self, line):
        '''getting link elements'''
        return line[5:].strip().split(', ')

    def get_paragraph(self, current_index):
        '''getting paragraph content'''

        accumulated_data = ''
        
        for index, line in itertools.islice(self.generator_list(), current_index, None):
            
            line = line.replace('\n','').strip()
            
            if self.type_line(line)=='end' or self.type_line(line) in self.avoid_list:
                return accumulated_data, index

            accumulated_data += line + '\n'
        
        return accumulated_data, current_index + 1        
                
    def get_list(self, line):
        '''getting list elements'''
        return line[5:].strip().split(',')
                
