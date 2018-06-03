import numpy as np

from sklearn.decomposition import LatentDirichletAllocation as LDA
from scipy.stats import entropy

from themecrafter.matrix.utils import rank_to_indices


def comp_normed(components):
    return components / components.sum(axis=0)[np.newaxis,:]


def word_entropy(components):
    return np.apply_along_axis(entropy, axis=0, arr=normed_components)


def top_words(words, weights, n=10, verbose=True):
    '''Returns the top n words by weight.'''
    rankings = np.argsort(weights)
    
    sorted_words = np.array(words)[rankings]
    sorted_weights = weights[rankings]
    
    top_words = sorted_words[:-n:-1]
    top_weights = sorted_weights[:-n:-1]
    
    #if verbose:
    #    for wrd, wgt in zip(twords, tweights):
    #        print(wrd, '{:g}'.format(wgt), end='; ')
    #    print()
        
    return top_words, top_weights

    
if __name__=='__main__':
    
    # Test the functions
    from themecrafter.datasets import SixDayWarDataSet
    docs = SixDayWarDataSet().X
    
    from nltk.tokenize import word_tokenize
    docs = [word_tokenize(doc) for doc in docs]
    
    from .castdoc import CountMatrix
    countmatrix = CountMatrix()
    M = countmatrix.fit(docs)
    vocab = countmatrix.vocab
    
    lda = LDA(n_components=3, learning_method='batch')
    lda.fit(M)
    components = comp_normed(lda.components_)
    
    # Now we obtain the top words in each topic.
    for weights in components:
    #    print( vocab, topic_wgts)
    #    assert len(vocab)==len(topic_wgts)
        top_wordtop_words(vocab, weights)
    
    
    
    #import matplotlib.pyplot as plt
    #plt.imshow(components)
    #plt.show()