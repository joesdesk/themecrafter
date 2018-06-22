# Source: https://radimrehurek.com/gensim/models/ldamodel.html

from .basemodel import BaseModel

from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim.matutils import corpus2csc

import numpy as np


class GensimLDA:

    def __init__(self, texts):
        self.dictionary = Dictionary(texts)
        self.corpus = [self.dictionary.doc2bow(text) for text in texts]
        
        self.k_topics = None
        self.model = None
        
    def fit(self, k_topics, iterations=50):
        ''''''
        self.k_topics = k_topics
        self.model = LdaModel(corpus=self.corpus, id2word=self.dictionary, \
            num_topics=k_topics, iterations=iterations)
        
    def get_document_topic_matrix(self, X=None):
        '''Returns an n_docs x k_topics array of probabilities
        of a topic in a given document.'''
        if X is None:
            X = self.corpus
        else:
            X = [self.dictionary.doc2bow(text) for text in X]
        
        n_docs = len(X)
        V = np.zeros((n_docs,self.k_topics))
        
        # Extract assignments
        some_iterable = self.model.get_document_topics(X)  ## equiv: self.model[X]
        for i, doc_topic in enumerate(some_iterable):
            for topic_id, prob in doc_topic:
                V[i, topic_id] = prob
        return V
        
    def get_topic_term_matrix(self):
        '''Returns an k_topics x m_words array of probabilities
        of a word in a given topic.'''
        return self.model.get_topics()
        
    def print_topics(self, top_n=10):
        '''Prints the top_n words in a topic'''
        for row in self.get_topic_term_matrix():
            ranking = np.argsort(row)
            ids = np.arange(len(ranking))[ranking]
            
            for k in ids[:-top_n:-1]:
                weight = row[k]
                word = self.dictionary.id2token[k]
                print(k, word, weight)
            print()
    
    def print_topic_words(self, topic_num, topn=None):
        '''Prints the top words and probabilities of a given topic in
        descending probability.'''
        for tok_id, prob in self.model.get_topic_terms(topic_num, topn=topn):
            word = self.dictionary.id2token[tok_id]
            print(word, prob)
            
    def get_topic_bows(self, num_words=10):
        '''Returns a list (for each topic) containing a list of the top num_words'''
        q = self.model.show_topics(num_topics=self.k_topics, num_words=num_words, formatted=False)
        topics = []
        for id, topic in q:
            words = []
            for w, p in topic:
                words.append(w)
            topics.append(words)
        return topics
    

if __name__=='__main__':
    pass
    
    