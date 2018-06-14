# Using simple nltk process documents into sentences and tokens.

import xml.etree.ElementTree as ET

from .corpusparser import CorpusParser
from .nltkparser import NltkDocParser, NltkSentParser
#from .pywsd import PyWSDParser

from .extrataggers import ExtraTagger


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
        
        return tree
            

class NLTKPlain2:
    '''Adds corrections to tokens found.'''
    def __init__(self):
        self.init_parser = NLTKPlain()
        
    def parse(self, docs):
        # Add element tags around the sentences
        tree = self.init_parser.parse(docs)
        
        # Then, add element tags around the tokens
        parser = NltkSentParser()
        for t in tree.findall('.//tok'):
            parser.parse(t)
            
        # Finally, add additional tags to the tokens to
        # indicate alternate forms.
        parser = ExtraTagger()
        for t in tree.findall('.//tok'):
            parser.parse(t)
        
        return tree
        
        
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
        
        
if __name__=="__main__":

    from ..datasets import BGSurveyDataSet as Data
    docs = Data().X
    
    parser = NLTKPlain2()
    tree = parser.parse(docs)
    
    from .utils import open_tree, show_tree, save_tree
    #show_tree(tree)
    
    #save_tree(tree, "M:/themecrafter/parsed/NLTKPlain2_NEW.xml")