from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups


class NewsGroupsDataSet:
    
    def __init__(self, n_samples=2000, n_features=1000, n_components=10):
        '''
        Obtains the data set and sets the parameteres
        '''
        # Shape of data
        self.n_samples=2000
        self.n_features=1000
        self.n_components=10
        
        # Load the 20 newsgroups dataset as raw data.
        self.X = fetch_20newsgroups(shuffle=True, random_state=1,
                                       remove=('headers', 'footers', 'quotes'))
    
    
    def cast_text(self):
        '''
        Returns data, a list of the data in as strings
        '''
        data = self.X.data
        vocab = None
        return (data, vocab)
        
    
    def cast_tfidf(self):
        '''
        Returns data, the TFIDF casting of the raw data and
                vocaab, the list of words
        '''
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                           max_features=self.n_features,
                                           stop_words='english')
        
        data, null = self.cast_text()
        data = tfidf_vectorizer.fit_transform(data[:self.n_samples])
        vocab = tfidf_vectorizer.get_feature_names()
        return (data, vocab)
    

    def cast_tf(self):
        '''
        Returns data, the TF casting of the raw data and
                vocab, the list of words
        '''
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                        max_features=self.n_features,
                                        stop_words='english')
        
        data, null = self.cast_text()
        data = tf_vectorizer.fit_transform(data[:self.n_samples])
        vocab = tf_vectorizer.get_feature_names()
        return (data, vocab)

