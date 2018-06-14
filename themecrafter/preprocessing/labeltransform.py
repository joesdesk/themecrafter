# Adds labels based on a transformation of other labels on the tree.

# https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk

from ..nlp.tokens import all_stopwords, punctuation
from nltk.util import flatten


class LabelTransform:
    '''Selects features for the analysis by adding labels
    to the elements of the tree.
    '''
    
    def __init__(self, labelname='label', lemmatize=True, \
        rm_stopwords=True, rm_punctuation=True, rm_char_len=1):
        
        self.labelname = labelname
        
        self.lemmatize = lemmatize
        self.rm_stopwords = rm_stopwords
        self.rm_punctuation = rm_punctuation
        self.rm_char_len = rm_char_len
        
        self.pos_whitelist = None
        self.label_blacklist = []
        
    def fit(self, tree):
        '''Applies the token transformation throughout the entire tree.'''
        for t in tree.findall('.//tok'):
        
            # Selects labels
            label = None
            if self.lemmatize:
                label = t.get('lemma', None)
            if label is None:
                label = t.get('alias', None)
            if label is None:
                label = t.get('lcase', None)
            if label is None:
                label = t.text
            
            # Decide whether to add label to element
            pos = t.get('pos', None)
            
            # Filter new label
            if len(label) < self.rm_char_len:
                label=None
            if (self.rm_stopwords) and (label in all_stopwords):
                label=None
            if (self.rm_punctuation) and (label in punctuation):
                label=None
            if label in self.label_blacklist:
                label=None
            
            if (label is not None) and (pos is not None):
                if self.pos_whitelist is not None:
                    if pos not in self.pos_whitelist:
                        label=None
            
            # Append label if survived filtering
            if label is not None:
                t.set(self.labelname, label)
                
                
                