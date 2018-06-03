# Class to compute a count matrix from a collection of documents which have
# already been preprocessed: i.e. tokenized, potentially including stemming
# and lemmatization.

from math import log
from collections import Counter

from numpy import array
from scipy.sparse import csr_matrix


class TF:
    
    def __init__(self, method='count', vocab=None):
        self.method = method
        self.vocab = vocab
    
    def fit(self, words):
        '''Returns a dictionary with words as keys and weighted counts as values.'''
        if self.vocab is None:
            self.vocab = list(set(words))
        
        counts = self.fit_count(words)
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
        
        return counts
    
    def fit_count(self, words):
        '''Returns a dictionary with words as keys and counts as values.'''
        wc = Counter(words)
        
        counts = [0]*len(self.vocab)
        for i, v in enumerate(self.vocab):
            c = wc.get(v, 0)
            counts[i] = c
            
        return counts
        


class CountMatrix:
    
    def __init__(self):
        self.vocab = None
        
    def fit(self, docs):
        ''''''
        # see: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html
        
        indptr = [0]
        indices = []
        data = []
        vocabulary = {}
        
        for d in docs:
            for term in d:
                index = vocabulary.setdefault(term, len(vocabulary))
                indices.append(index)
                data.append(1)
            indptr.append(len(indices))
            
        return csr_matrix((data, indices, indptr), dtype=int)

        
class TFIDFMatrix:

    def __init__(self):
        pass
        
    def fit(self, docs):
        pass
        
        