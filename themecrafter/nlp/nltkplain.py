# Using simple nltk process documents into sentences and tokens.

import xml.etree.ElementTree as ET

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer

from .corpusparser import CorpusParser
from .nltkparser import NltkDocParser, NltkSentParser
#from .pywsd import PyWSDParser

from .reparser import ReParser
from .labelling import label_special, label_word

from ..nlp.utils import open_tree, show_tree, save_tree


class NLTKPlain:
    '''The most basic parser. This keeps the sentences in tact.'''
    def __init__(self):
        pass
    
    def parse(self, docs):
        # First, parse the corpus
        parser = CorpusParser()
        tree = parser.parse(docs)
        
        # Then, parse the documents
        parser = NltkDocParser()
        for t in tree.findall('.//tok'):
            parser.parse(t)
            

class NLTKPlain2:
    '''Adds labels for special tokens found.'''
    def __init__(self):
        self.init_parser = NLTKPlain()
        
    def parse(self, docs):
        # Add element tags around the sentences
        tree = self.init_parser.parse(docs)
        
        # Then, add element tags around the tokens
        parser = NltkSentParser()
        for t in tree.findall('.//tok'):
            parser.parse(t)
        
        return tree
        
        # Then, label some text with special characters.
        for t in tree.findall('.//tok'):
            self.label_special(t)
            self.label_word(t)
        
        # Then, reparse
        parser = ReParser()
        for t in tree.findall('.//tok'):
            if t.get('label', None) is None:
                parser.parse(t)
            
        # Then, label all special text again.
        for t in tree.findall('.//tok'):
            self.label_special(t)
            self.label_word(t)
        
        return tree
        
    def label_special(self, t):
        '''Find all special text and label them.'''
        if t.get('label', None) is None:
            label_, pos_ = label_special( t.text )
            if pos_ is not None:
                t.set('label', label_)
                t.set('pos', pos_)
    
    def label_word(self, t):
        '''Find all special text and label them.'''
        if t.get('label', None) is None:        
            label_ = label_word( t.text )
            if label_ is not None:
                t.set('label', label_)
                
                
class NLTKPlainWS:

    def __init__(self):
        self.init_parser = NLTKPlain()
    
    def parse(self, docs):
        # Add element tags around the sentences
        tree = self.init_parser.parse(docs)
            
        # Then, parse the sentences
        parser = PyWSDParser()
        for t in tree.findall('.//tok'):
            parser.parse(t)
        
        return tree
        

class NLTKPlain3:
    
    def __init__(self):
        self.init_parser = NLTKPlain2()
        
    
       
        
        