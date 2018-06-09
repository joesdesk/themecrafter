# Adds labels based on a transformation of other labels on the tree.

# https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk

from ..nlp.tokens import all_stopwords, punctuation
from ..nlp.nltklemmatizer import wordnet_lemmatize
from nltk.util import flatten


class LabelTransform:
    
    def __init__(self, labelname='new_label_name'):
        '''A list of tokens, which are tuples indicating the label and pos.'''
        self.labelname = labelname
        
        self.lemmatize = True
        self.rm_stopwords = True
        self.rm_punctuation = True
        self.rm_char_len = 1
        
        self.pos_whitelist = []
        self.label_blacklist = []
        
    def fit(self, tree):
        '''Applies the token transformation throughout the entire tree.'''
        for t in tree.findall('.//tok[@label]'):
            label = t.get('label')
            pos = t.get('pos', None)
            
            # Create new label
            newlabel = label.lower()
            if self.lemmatize:
                newlabel = wordnet_lemmatize(newlabel, pos)
            
            # Filter new label
            if len(newlabel) < self.rm_char_len:
                newlabel=None
            if (self.rm_stopwords) and (newlabel in all_stopwords):
                newlabel=None
            if (self.rm_punctuation) and (newlabel in punctuation):
                newlabel=None
            if newlabel in self.label_blacklist:
                newlabel=None
            
            if (newlabel is not None) and (pos is not None): 
                if pos not in self.pos_whitelist:
                    newlabel=None
            
            # Append newlabel if survived filtering
            if newlabel is not None:
                t.set(self.labelname, newlabel)
            
            
