from sklearn.decomposition import LatentDirichletAllocation as LDA


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
    
    
    lda = LDA(n_components=3, learning_method='batch')
    lda.fit(M)
    
    print(lda.components_)
    
    
    