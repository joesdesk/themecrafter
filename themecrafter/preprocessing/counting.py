# Class to compute a count matrix from a collection of documents which have
# already been preprocessed

# Sources:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html

from math import log
from collections import Counter

from numpy import array
from scipy.sparse import csr_matrix

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


# Functions to transform the count matrix into other normalizations.

def count2bin(countmatrix):
    '''Compute whether the term appeared or not in each document.'''
    for w, c in wc.items():
        wc[w] = 1 if c>0 else 0
    
def count2tf(countmatrix):
    '''Compute the term probability of each document.'''
    sum_count = sum(list(wc.values()))
    for w, c in wc.items():
        wc[w] = c / sum_count

def count2lognorm(countmatrix):
    '''Normalizes the count matrix using log normalization.'''
    for w, c in wc.items():
        wc[w] = log(1 + c)

def count2df(countmatrix):
    '''Obtains the document frequency of a term.'''
    pass

def count2tfidf(countmatrix):
    '''Compute the term-frequency inverse document-frequency of a count matrix.'''
    pass

    
class CountMatrix:
    
    def __init__(self):
        '''Initializes the vocabulary.'''
        self.vocab = None
        
    def fit(self, docs):
        '''Creates a document-term matrix where documents are placed along the rows,
        and terms across the columns. The matrix elements are the number of
        counts a term appears in a document.'''
        
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
        
        # Invert the vocabulary
        len_vocab = len(vocabulary)
        self.vocab = [None]*len_vocab
        for k, v in vocabulary.items():
            self.vocab[v] = k
        
        return csr_matrix((data, indices, indptr), dtype=int)
        
        