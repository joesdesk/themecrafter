# Class to compute a count matrix from a collection of documents which have
# already been preprocessed: i.e. tokenized, potentially including stemming
# and lemmatization.

from collections import Counter
from scipy.sparse import lil_matrix


class TF:
    
    def __init__(self, method='count'):
        if method=='count':
            pass
        
    def fit(self, words):
        '''Returns a dictionary with words as keys and counts as values.'''
        wc = Counter(words)
        return dict(wc)
        
        
class CountMatrix:
    
    def __init__(self):
        pass
        
    def fit(self, docs):
        n_docs = len(docs)
        
        tf = TF()
        wcounts_by_doc = [tf.fit(doc) for doc in docs]
        
        vocab = set()
        for wcs in wcounts_by_doc:
            for w, c in wcs.items():
                vocab.add(w)
        vocab = list(vocab)
        n_terms = len(vocab)
        
        # Now that we know the size of the vocabulary
        M = lil_matrix((n_docs, n_terms))
        for i in range(n_docs):
            for j in range(n_terms):
                w = vocab[j]
                M[i,j] = wcounts_by_doc[i].pop(w, 0)
        return M

        
if __name__=='__main__':
    
    # Test the functions
    from themecrafter.datasets import SixDayWarDataSet
    docs = SixDayWarDataSet().X
    
    #tf = TF()
    #wc = tf.fit(doc.split(' '))
    #for w, c in wc.items():
    #    print(w, c)
    
    from nltk.tokenize import word_tokenize
    docs = [word_tokenize(doc) for doc in docs]
    
    countmatrix = CountMatrix()
    M = countmatrix.fit(docs)
    
    M.todense()
    #print(M)
    
    from sklearn.decomposition import LatentDirichletAllocation as LDA
    lda = LDA(n_components=3, learning_method='batch')
    lda.fit(M)
    
    print(lda.components_)
    
    
    