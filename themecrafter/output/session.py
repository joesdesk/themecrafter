import random

from .load_data_session import LoadDataSession

from ..preprocessing import HtmlCorpus


class ThemeCrafterSession(LoadDataSession):

    def __init__(self):
        LoadDataSession.__init__(self)


    def read_doc(self, id=None):
        '''Reads a document for a given id.
        If no id is given, reads a document at random.'''
        
        n_docs = len(self.docs)
        
        if id is None:
            id = random.randrange(n_docs)
        
        doc = self.docs[id]
        
        print("doc id:", id)
        print("")
        print(doc)
        print("")
        
    
    def to_html(self):
        html = HtmlCorpus(self.docs)
        return html
    
    
    def to_html_text(self):
        html = self.to_html()
        return html.prettify()
    
    
    def to_html_file(self, file):
        html_text = self.to_html_text()
        
        f = open(file, 'w+')
        f.write(html_text)
        f.close()
        
        
    def tokenize(self):
        ''''''
        pass
        
