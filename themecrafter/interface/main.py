from ..nlp.corpusparser import CorpusParser
from ..nlp.utils import open_tree, show_tree, save_tree, tree2string
from ..models.gensimlda import GensimLDA

from pandas import DataFrame
from .html import HTMLInterface


class MainInterface:
    '''Container for all objects of interation for the GUI.'''
    
    def __init__(self):
        '''Creates the variables.'''
        # Parsed XML
        self.docs = None
        self.tree = None
        
        # Sub-interfaces
        self.html = None
        self.model = None
        
    def load_docs(self, docs):
        '''Loads the documents to be analyzed.'''
        self.docs = docs
        parser = CorpusParser()
        tree = parser.parse(self.docs)
        xmlstring = tree2string(tree)
        self.html = HTMLInterface(xmlstring)
        
    def loadxml(self):
        '''Load XML into interface'''
        file = "M:/themecrafter/parsed/NLTKPlain2_NEW.xml"
        self.tree = open_tree(file)
        
        xmlstring = tree2string(self.tree)
        self.html = HTMLInterface(xmlstring)
        
    def loadmodel(self):
        self.model = GensimLDA()
        
    def sel_feat(self):
        pass
        
    def add_model(self):
        model = None
        
    def get_topics(self):
        df = DataFrame([("topic1",30)], columns=['topic','weight'])
        return df
        
    def get_html(self):
        htmlstring = self.html.render(0)
        return htmlstring
        
        