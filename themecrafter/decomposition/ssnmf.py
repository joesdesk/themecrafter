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


# Non-negative least squares
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


# Semi-supervised Non-negative Matrix factorization
def ssnmf(X, k, W=None, H=None):

    # Extract parameters
    n_docs = X.shape[1]
    m_words = X.shape[0]
    
    # initialize W, H, D
    if W is None:
        W = np.random.rand(m_words, k)
    if H is None:
        H = np.random.rand(k, n_docs)

    # also initialize reference matrices
    V = np.zeros((m_words, k), dtype=float)
    G = np.zeros((k, n_docs), dtype=float)

    Mw = np.eye(m_words)*0
    Mh = np.eye(n_docs)*0

    i=0
    while i < 20:
        W = matrix_nnls(H.T, X.T, V.T, Mw).T
        H = matrix_nnls(W, X, G, Mh)

        i += 1
        loss = norm(X - W@H)

    return (W, H)
