# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#modifying-the-tree

# Using anchors, id vs name
# https://stackoverflow.com/questions/484719/html-anchors-with-name-or-id

from .document import Corpus
from .htmlelement import HtmlElement


class TokenElement(HtmlElement):
    
    def __init__(self, t):
        HtmlElement.__init__(self)
        
        self.tag = 'token'
        
        attr = dict()
        attr['pos'] = t.pos
        attr['i'] = t.i
        attr['len'] = len(t.text)
        attr['sloc'] = t.sloc
        attr['dloc'] = t.dloc
        self.attr = attr
        
        self.children = [t.text]
    
    
        
class SentenceElement(HtmlElement):
    
    def __init__(self, s):
        HtmlElement.__init__(self)
        
        self.tag = 'sentence'
        
        attr = dict()
        attr['i'] = s.i
        attr['did'] = s.did
        attr['dloc'] = s.dloc
        
        last_stop = 0
        for t in s.tokens:

            space = ' '*(t.sloc - last_stop)
            self.add(space)
            last_stop = t.sloc + len(t.text)
            
            t_elem = TokenElement(t)
            self.add(t_elem)
            
            
            
class DocumentElement(HtmlElement):
    
    def __init__(self, d):
        HtmlElement.__init__(self)
        
        self.tag = 'document'
        
        attr = dict()
        attr['i'] = d.i
        
        last_stop = 0
        for s in d.sentences:

            space = ' '*(s.dloc - last_stop)
            self.add(space)
            last_stop = s.dloc + len(s.text)
            
            s_elem = SentenceElement(s)
            self.add(s_elem)
            

            
class HtmlCorpus(HtmlElement):

    def __init__(self, docs):
        ''''''
        
        # Container
        HtmlElement.__init__(self)
        self.tag = 'corpus'
        
        # Insert documents as children
        corpus = Corpus(docs)
        for doc in corpus.docs:
            self.add(DocumentElement(doc))
        
    
    def prettify(self):
        return self.dump()
    

        
