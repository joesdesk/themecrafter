from ..nlp.corpusparser import CorpusParser
from ..nlp.utils import open_tree, show_tree, save_tree, tree2string

from ..preprocessing.labeltransform import LabelTransform
from ..nlp.nltklemmatizer import NOUN_POS, VERB_POS, ADJ_POS

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
        self.labeltransform = LabelTransform()
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
        
    def savexml(self):
        '''Save XML into a file'''
        #filename = ""
        #save_tree(self.tree, filename)
        # Save results to file
        #dir = "M:/themecrafter/labelled/"
        #save_tree(tree, dir+"NLTKPlain2-STANDARD.xml")
        pass
        
    def loadmodel(self):
        self.model = GensimLDA()
        
    def feat_sel(self):
        '''Performs feature selection.'''
        if self.tree is not None:
            self.label(self.tree)
            show_tree(self.tree)
        
    def add_model(self):
        model = None
        
    def get_topics(self):
        df = DataFrame([("topic1",30)], columns=['topic','weight'])
        return df
        
    def get_html(self):
        htmlstring = self.html.render(0)
        return htmlstring
        
    def label(self, tree):

        # Flags
        LEMMATIZE = True ## Don't change

        # Remove stopwords and punctuations
        RM_STOPWORDS = True  ## Don't change
        RM_PUNCT = True  ## Don't change

        # Remove short words
        RM_CHAR_LEN = 2  ## Don't change

        # Include only nouns
        KEEP_NOUNS = True  ## Don't change
        KEEP_VERBS = True
        KEEP_ADJ = False  ## Don't change
        KEEP_ALLPOS = True  ## 

        # Extra words to exclude 
        BLACKLIST = []  ##['program', 'student', 'ubc']

        # Initialize labeller
        labeltransform = LabelTransform(labelname='label', lemmatize=LEMMATIZE, \
            rm_stopwords=RM_STOPWORDS, rm_punctuation=RM_PUNCT, \
            rm_char_len=RM_CHAR_LEN)
            
        labeltransform.pos_whitelist=[]
        if KEEP_NOUNS:
            labeltransform.pos_whitelist.extend(NOUN_POS)
        if KEEP_VERBS:
            labeltransform.pos_whitelist.extend(VERB_POS)
        if KEEP_ADJ:
            labeltransform.pos_whitelist.extend(ADJ_POS)
        if KEEP_ALLPOS:
            labeltransform.pos_whitelist=None
            
        labeltransform.label_blacklist = BLACKLIST

        # Perform labellling
        labeltransform.fit(tree)
        
        