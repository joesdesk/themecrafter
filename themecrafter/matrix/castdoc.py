# Class to compute a count matrix from a collection of documents which have
# already been preprocessed: i.e. tokenized, potentially including stemming
# and lemmatization.

from math import log
from collections import Counter
from scipy.sparse import lil_matrix


class TF:
    
    def __init__(self, method='count'):
        self.method = method
    
    def fit(self, words):
        '''Returns a dictionary with words as keys and weighted counts as values.'''
        wc = self.fit_count(words)
        if self.method=='count':
            pass
        if self.method=='binary':
            for w, c in wc.items():
                wc[w] = 1 if c>0 else 0
        if self.method=='term frequency':
            sum_count = sum(list(wc.values()))
            for w, c in wc.items():
                wc[w] = c / sum_count
        if self.method=='log normalization':
            for w, c in wc.items():
                wc[w] = log(1 + c)
        
        return wc
    
    def fit_count(self, words):
        '''Returns a dictionary with words as keys and counts as values.'''
        wc = Counter(words)
        return dict(wc)
        
        
class CountMatrix:
    
    def __init__(self):
        self.vocab = None
        
    def fit(self, docs):
        n_docs = len(docs)
        
        tf = TF()
        wcounts_by_doc = [tf.fit(doc) for doc in docs]
        
        vocab = set()
        for wcs in wcounts_by_doc:
            for w, c in wcs.items():
                vocab.add(w)
        vocab = list(vocab)
        self.vocab = vocab
        n_terms = len(vocab)
        
        # Now that we know the size of the vocabulary
        M = lil_matrix((n_docs, n_terms))
        for i in range(n_docs):
            for j in range(n_terms):
                w = vocab[j]
                M[i,j] = wcounts_by_doc[i].pop(w, 0)
        return M


class TFIDFMatrix:

    def __init__(self):
        pass
        
    def fit(self, docs):
        pass
        
        