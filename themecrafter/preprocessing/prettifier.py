# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#modifying-the-tree

# Using anchors, id vs name
# https://stackoverflow.com/questions/484719/html-anchors-with-name-or-id

from bs4 import BeautifulSoup

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
            #space = HtmlElement()
            #space.tag = 'span'
            #space.insert_element(' '*(t.sloc - last_stop))
            space = ' '*(t.sloc - last_stop)
            self.insert_element(space)
            last_stop = t.sloc + len(t.text)
            
            t_elem = TokenElement(t)
            self.insert_element(t_elem)

            
            
class DocumentElement(HtmlElement):
    
    def __init__(self, d):
        HtmlElement.__init__(self)
        
        self.tag = 'document'
        
        attr = dict()
        attr['i'] = d.i
        
        p = HtmlElement()
        p.tag = 'p'
        
        last_stop = 0
        for s in d.sentences:
            #space = HtmlElement()
            #space.tag = 'span'
            #space.insert_element(' '*(s.dloc - last_stop))
            space = ' '*(s.dloc - last_stop)
            p.insert_element(space)
            last_stop = s.dloc + len(s.text)
            
            s_elem = SentenceElement(s)
            p.insert_element(s_elem)
            
        self.insert_element(p)
            


            
class HtmlCorpus(HtmlElement):

    def __init__(self, docs):
        ''''''
        
        # Container
        HtmlElement.__init__(self)
        self.tag = 'html'
        
        # Header tag
        header = HtmlElement()
        header.tag = 'head'
        self.insert_element(header)
        
        # Body tag
        body = HtmlElement()
        body.tag = 'body'
    
        # Create line break element
        lb = HtmlElement()
        lb.tag = 'br'
        
        # 
        corpus = Corpus(docs)
        for doc in corpus.docs:
            body.insert_element(DocumentElement(doc))
            body.insert_element(lb)
    
        self.insert_element(body)
        
    
    def prettify(self):
        return self.dump()
    
        