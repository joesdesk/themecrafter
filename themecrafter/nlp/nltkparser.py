from xml.etree.ElementTree import SubElement
from .utils import show_tree

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize


class NltkDocParser:
    '''From an element with text, creates a document element
    whose token elements are sentences.'''
    
    def __init__(self):
        pass
        
    def parse(self, element):
        element.tag = 'doc'
        
        text = element.text
        element.text = None
        
        sents = sent_tokenize(text)
        
        offset = 0
        for i, sent in enumerate(sents):
            
            offset = text.find(sent, offset)
            
            attrib = {}
            attrib['id'] = i
            attrib['offset'] = offset
            attrib['len'] = len(sent)
            
            token = SubElement(element, 'tok', attrib)
            token.text = sent
            offset += len(sent)
        
        return None

        
class NltkSentParser:
    '''From an element with text, creates  a sentence element
    whose token elements are tokens.'''
    
    def __init__(self):
        pass
        
    def parse(self, element):
        element.tag = 'sent'
        
        text = element.text
        element.text = None
        
        words = word_tokenize(text)
        poses = pos_tag(words)
        
        offset = 0
        for k in range(len(words)):
            
            word, pos = poses[k]
            
            offset = text.find(word, offset)
            
            attrib = {}
            attrib['id'] = k 
            attrib['offset'] = offset
            attrib['len'] = len(word)
            attrib['pos'] = pos
            
            token = SubElement(element, 'tok', attrib)
            token.text = word
            offset += len(word)
        
        return None
        

if __name__=='__main__':
    pass
    
    