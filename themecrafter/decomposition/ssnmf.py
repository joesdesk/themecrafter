# Semi-supervised Non-negative Matrix Factorization
# This is derived from the work by
# Da Kuang, Jaegul Choo and Haesun Park. "Partitional Clustering Algorithms."
# Chapter 7. Nonnegative Matrix Factorization for Interactive Topic Modeling
# and Document Clustering (2015)

import numpy as np
from numpy.linalg import norm

from scipy.sparse import csc_matrix, eye
from scipy.sparse import vstack, hstack

from scipy.optimize import nnls
from scipy.linalg import norm


# Non-negative least squares on a matrix (NNLS)
def matrix_nnls(A, B, X0, M):
    """
    Solves for argmin_X ||A*X-B||_2 + ||(X-X0)*M||_2 for x>=0.
    """

    # Get number of topics
    k_topics = A.shape[1]
    iden = np.eye(k_topics)

    # Solve per column
    X = []
    for i in range(B.shape[1]):

        m_i = M[i,i]
        A_ = np.vstack(( A, m_i*iden ))
        b_ = np.concatenate(( B[:,i], m_i*X0[:,i] ))
        x, residuals = nnls(A_, b_, maxiter=None)

        X.append(x[:,np.newaxis])

    return np.hstack(X)


# Semi-supervised Non-negative Matrix factorization (SSNMF)
def ssnmf(X, k, W=None, H=None, V=None, G=None, Mw=None, Mh=None):

    # Extract parameters
    n_docs = X.shape[1]
    m_words = X.shape[0]
    
    # Recursive updating
    i=0
    while i < 5:
        W = matrix_nnls(H.T, X.T, V.T, Mw).T
        H = matrix_nnls(W, X, G, Mh)

        loss = norm(X - W@H)
        i += 1

    return (W, H)


# SSNMF incorporating user-feedback
class SSNMF:
    
    def __init__(self, k_topics):
        '''Initializes the model.
        '''
        self.k_topics = k_topics
        
        # Initialize results
        self.W = None
        self.H = None
        
        # Initialize reference matrices
        self.V = None
        self.G = None
        
        # Initialize weight/masking matrices
        self.Mw = None
        self.Mh = None
        
        # Initialize extra metadata
        self.set_topic_labels()
        self.set_vocab()
        self.set_docs()
        
    
    def fit(self, X):
        '''Performs the factorization
        '''
        
        # Determine parameters
        self.n_docs = X.shape[1]
        self.m_words = X.shape[0]
        
        print('Performing factorization on matrix with:')
        print(self.n_docs, " documents")
        print(self.m_words, " words")
        print(self.k_topics, "topics")
        print('Fitting...', end=' ')
        
        # Initialize factor matrices
        if self.W is None:
            self.W = np.random.rand(self.m_words, self.k_topics)
        if self.H is None:
            self.H = np.random.rand(self.k_topics, self.n_docs)
        
        # Initialize reference matrices if needed
        if self.V is None:
            self.V = np.zeros_like(self.W, dtype=float)
        if self.G is None:
            self.G = np.zeros_like(self.H, dtype=float)

        if self.Mw is None:
            self.Mw = np.zeros((self.m_words, self.m_words))
        if self.Mh is None:
            self.Mh = np.zeros((self.n_docs, self.n_docs))
            
        # Do factorization
        self.W, self.H = ssnmf(X, k=self.k_topics, W=self.W, H=self.H,
                                       V=self.V, G=self.G, Mw=self.Mw, Mh=self.Mh)
        
        #
        print('Done!')
    
    
    ## Predict the label for each document
    def predict(self, X):
        ''''''
        G = np.zeros_like(self.H, dtype=float)
        Mh = np.zeros((self.n_docs, self.n_docs))
        
        Hpred = matrix_nnls(self.W, X, G, Mh)
        Hnorm = Hpred / np.sum(Hpred, axis=0)[np.newaxis,:]
        return Hnorm
    
    
    def get_docs_by_topic(self, X, topic_id, n, sort=False):
        ''''''
        # Make hard predictions
        Hpred = self.predict(X)
        ypred = np.argmax(Hpred, axis=0)
        conf = Hpred[( ypred, np.arange(ypred.shape[0]) )]

        # Get indices
        doc_ids, = np.nonzero(ypred==topic_id)
        
        # 
        if sort==True:
            top_ids = np.argsort( -conf[doc_ids] )
            doc_ids = doc_ids[top_ids][:n]
        else:
            doc_ids = np.random.choice(doc_ids, size=n)
            
        return doc_ids
    
    
    # Set extra metadata
    def set_topic_labels(self, labels=None):
        ''''''
        if labels is None:
            self.topic_labels = ['TOPIC{:d}'.format(i+1) for i in range(self.k_topics)]
        else:
            self.topic_labels = labels
    
    
    def set_vocab(self, vocab=None):
        ''''''
        self.vocab = vocab
    
    
    def set_docs(self, docs=None):
        ''''''
        self.docs = docs
    
    
    # Output to user functions
    def show_topics(self, n_top_words=10):
        '''Shows topics and top words in each topic'''
        
        # Ensure vocabulary
        assert self.vocab is not None, "Error: vocabulary not set."
        vocab = self.vocab
        
        # Printing for each topic
        for tid, topic in enumerate(self.W.T):
            print(self.topic_labels[tid], end=': ')
            print(" ".join([vocab[i]
                            for i in topic.argsort()[:-n_top_words - 1:-1]]))
    
    
    def get_document(self, doc_id=None):
        ''''''
        # Get random document if not specified
        if doc_id is None:
            doc_id = np.random.randint(self.n_docs)

        # Print document id and document
        print('Document:', doc_id)
        print()

        print(self.docs[doc_id])
        print()
        
        self.view_weights(doc_id, self.H)
        print()
        return doc_id
    
    
    def view_weights(self, doc_id, weight):
        '''View the topic weights of a document.'''
        
        weights = weight[:,doc_id]
        t_rank = np.argsort(-weights)

        w_rank = weights[t_rank]
        l_rank = np.array(self.topic_labels)[t_rank]
        
        for i in range(self.k_topics):
            print(l_rank[i], "{:.3g}".format(w_rank[i]))
    
    
    # Input from user functions
    def add_word_to_topic(self, word_id, topic_id):
        ''''''
        self.V[word_id, topic_id] += np.mean(self.W[:, topic_id])*2
        self.Mw[word_id,word_id] += 1
        
    
    def remove_word_from_topic(self, word_id, topic_id):
        ''''''
        self.V[word_id, topic_id] = 0
        self.Mw[word_id, word_id] +=1
    
    
    def add_topic_to_doc(self, topic_id, doc_id):
        ''''''
        self.G[topic_id, doc_id] += np.mean(self.H[:, doc_id])*2
        self.Mh[doc_id, doc_id] +=1
    
    
    def remove_topic_from_doc(self, topic_id, doc_id):
        ''''''
        self.G[topic_id, doc_id] = 0
        self.Mh[doc_id, doc_id] +=1
        
        