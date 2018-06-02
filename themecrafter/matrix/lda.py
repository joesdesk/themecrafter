from sklearn.decomposition import LatentDirichletAllocation as LDA


def print_top_words(components, vocab, n_top_words):
    for topic_idx, topic in enumerate(components):
        message = "Topic #%d: " % topic_idx
        message += " ".join([vocab[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()

    
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
    
    from .castdoc import CountMatrix
    countmatrix = CountMatrix()
    M = countmatrix.fit(docs)
    vocab = countmatrix.vocab
    
    lda = LDA(n_components=3, learning_method='batch')
    lda.fit(M)
    components = lda.components_
    
    # Now we obtain the top words in each topic.
    print_top_words(components, vocab, 10)
    