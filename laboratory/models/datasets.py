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
        Lets X be the list of texts as strings.
        '''
        self.X = self.X.data
        self.vocab = None
        
    
    def cast_tfidf(self):
        '''
        Returns X as the TFIDF casting of the data.
        '''
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                           max_features=self.n_features,
                                           stop_words='english')
        
        self.cast_text()
        self.X = tfidf_vectorizer.fit_transform(self.X[:self.n_samples])
        self.vocab = tfidf_vectorizer.get_feature_names()
   

    def cast_tf(self):
        '''
        Returns X as the TF casting of the data.
        '''
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                        max_features=self.n_features,
                                        stop_words='english')
        
        self.cast_text()
        self.X = tf_vectorizer.fit_transform(self.X[:self.n_samples])
        self.vocab = tf_vectorizer.get_feature_names()

