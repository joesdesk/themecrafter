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
            space = ' '*(t.i - last_stop)
            self.insert_element(space)
            last_stop += len(t.text)
            
            t_elem = TokenElement(t)
            self.insert_element(t_elem)

            
            
class DocumentElement(HtmlElement):
    
    def __init__(self, d):
        HtmlElement.__init__(self)
        
        self.tag = 'document'
        
        attr = dict()
        attr['i'] = d.i
        
        last_stop = 0
        for s in d.sentences:
            space = ' '*(s.i - last_stop)
            self.insert_element(space)
            last_stop += len(s.text)
            
            s_elem = SentenceElement(s)
            self.insert_element(s_elem)
            


            
class HtmlCorpus(BeautifulSoup):

    def __init__(self, docs):
        ''''''
        
        # Container
        html = HtmlElement()
        html.tag = 'html'
        
        # Header tag
        header = HtmlElement()
        header.tag = 'head'
        html.insert_element(header)
        
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
    
        html.insert_element(body)
        
        # Create string
        htmltext = html.dump()
        BeautifulSoup.__init__(self, htmltext, "lxml")
        
        