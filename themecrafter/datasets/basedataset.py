from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class BaseDataSet():

    def __init__(self):
        '''Loads the data set.

        Derived classes load the data by overwrite this method and
        setting self.X to be a list of strings, which are the documents.
        '''
        self.X = []


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
