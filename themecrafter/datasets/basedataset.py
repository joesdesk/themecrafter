from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class BaseDataSet():

    def __init__(self):
        '''Initializes the base data set.
        This method should be overridden in derived classes to
        set self.X to a python list of strings, which represent documents.
        '''
        self.X = None


    def to_text(self):
        '''
        Returns data, a list of the data in as strings
        '''
        data = self.X.data
        vocab = None
        return (data, vocab)


    def to_tfidf(self):
        '''
        Returns data, the TFIDF casting of the raw data and
                vocaab, the list of words
        '''
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                           max_features=self.n_features,
                                           stop_words='english')

        data, null = self.to_text()
        data = tfidf_vectorizer.fit_transform(data[:self.n_samples])
        vocab = tfidf_vectorizer.get_feature_names()
        return (data, vocab)


    def to_tf(self):
        '''
        Returns data, the TF casting of the raw data and
                vocab, the list of words
        '''
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                        max_features=self.n_features,
                                        stop_words='english')

        data, null = self.to_text()
        data = tf_vectorizer.fit_transform(data[:self.n_samples])
        vocab = tf_vectorizer.get_feature_names()
        return (data, vocab)
