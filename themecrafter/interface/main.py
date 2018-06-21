from ..nlp.corpusparser import CorpusParser
from ..nlp.utils import open_tree, show_tree, save_tree, tree2string

from ..preprocessing.labeltransform import LabelTransform
from ..nlp.nltklemmatizer import NOUN_POS, VERB_POS, ADJ_POS

from ..preprocessing import BagOfWords

from ..models.gensimlda import GensimLDA
from ..models.utils import hard_assignments, rank2id

import numpy as np
from pandas import DataFrame



class MainInterface:
    '''Container for all objects of interation for the GUI.'''
    
    def __init__(self):
        '''Creates the variables.'''
        # Parsed XML
        self.docs = None
        self.tree = None
        
        # Sub-interfaces
        self.labeltransform = LabelTransform()
        self.model = None
        self.doc_scores = None
        self.doc_assigns = None
        self.topics = None
        
    def load_docs(self, docs):
        '''Loads the documents to be analyzed.'''
        self.docs = docs
        parser = CorpusParser()
        tree = parser.parse(self.docs)
        
    def loadxml(self):
        '''Load XML into interface'''
        file = "M:/themecrafter/parsed/NLTKPlain2_NEW.xml"
        self.tree = open_tree(file)
        
    def savexml(self):
        '''Save XML into a file'''
        #filename = ""
        #save_tree(self.tree, filename)
        # Save results to file
        #dir = "M:/themecrafter/labelled/"
        #save_tree(tree, dir+"NLTKPlain2-STANDARD.xml")
        pass
    
    def get_xmlstring(self):
        return tree2string(self.tree)
    
    def do_model(self):
        bow = BagOfWords(tokenlabel='label', doc_sel="SENTENCE")
        bow.fit(self.tree)
        
        # Bag of words representation of each document (sentence)
        bows = bow.bows_
        # Corresponding tree elements for later retagging
        tags = bow.tags_
        
        # Get model...
        self.model = GensimLDA(bows)
        self.model.fit(k_topics=10)
        
        V = self.model.get_document_topic_matrix()
        print(V.shape)
        y = hard_assignments(V)
        
        for i, t in enumerate(tags):
            t.attrib['class'] = str(y[i])
            #show_tree(t)
            
        # Get topic of each document
        docids = []
        start = 0
        for d in self.tree.findall('.//doc'):
            nsents = len( d.findall('.//sent') )
            b = start + nsents
            docids.append((start, b))
            start = b
        
        # Create new matrix on document basis
        E = []
        for i, (a,b) in enumerate(docids):
            Q = np.sum(V[a:b,:], axis=0)
            E.append( Q / (b-a) )
        R = np.array(E)
        
        # Obtain entropy
        from scipy.stats import entropy
        entr = np.apply_along_axis(entropy, axis=1, arr=R)
        
        # Save entropies to rank documents
        self.doc_scores = entr
        self.doc_assigns = hard_assignments(R)
        
        # Create data frame with topics
        df = DataFrame(columns=['topic','words'])
        for i, ws in enumerate(self.model.get_topic_bows(7)):
            topic = 'topic {:d}'.format(i+1)
            words = ', '.join(ws)
            df = df.append({'topic':topic,'words':words}, ignore_index=True)
        #self.get_topics(df)
        self.topics = df
    
    def show_docs(self, topic_num):
        '''Gets the document indices for documents related to the topics by weight.'''
        sel = self.doc_assigns==topic_num
        ids = np.arange(len(self.doc_assigns))[sel]
        scores = self.doc_scores[sel]
        rankings = np.argsort(scores)
        k = rank2id(rankings)
        return ids[k]
        
    def feat_sel(self):
        '''Performs feature selection.'''
        if self.tree is not None:
            self.label(self.tree)
            show_tree(self.tree)
            
    def get_topics(self):
        if self.topics is not None:
            return self.topics
            
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
        BLACKLIST = ['program', 'ubc']

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
        
        
if __name__=='__main__':
    interface = MainInterface()
    
    interface.loadxml()
    interface.label(interface.tree)
    
    interface.do_model()