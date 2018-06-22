from ..preprocessing.groupdict import GroupedDict


class TopWords:
    
    def __init__(self):
        '''Prepares the model.'''
        self.groupdict = GroupedDict()
        self.words = None
        
        self.topics = None
        self.counts = None
        
    def fit(self, words):
        '''Input is a list of words.'''
        self.words = words
        
        ids = list( range( len(words) ) )
        self.groupdict.group(ids, words)
        
        self.set_params()
            
    def set_params(self, k_topics=10, min_count=0, max_count=None):
        '''Sets the internal list of topics according to the parameters.
        This will be used to determine the outputs of the model.'''
        self.topics = []
        self.counts = []
        
        i = 0
        for k, c in self.groupdict.counts():
            if not i < k_topics:
                append=False
            elif c < min_count:
                append=False
            elif max_count is None:
                append=True
            elif c > max_count:
                append=False
            else:
                append=True
            
            if append:
                self.topics.append(k)
                self.counts.append(c)
                i += 1
        
    def get_doc_topics(self):
        '''Assigns topic indices to the words used to fit.'''
        n = len(self.words)
        y = [None]*n
        
        for topic_id, topic in enumerate(self.topics):
            idlist = self.groupdict.get(topic)
            for i in idlist:
                y[i] = topic_id
        
        return y
    
    def get_topic_of_original_words(self, topic_id):
        '''Returns the word indices of the fitted words which are
        assigned to the given topic_id.'''
        topic = self.topics[topic_id]
        return self.groupdict.get(topic)
    
    def get_topics(self, top_n=None):
        '''Gets a list of words which are the most occuring.
        These are the topics.'''
        return self.topics
        
    def get_counts(self):
        '''Returns a list of counts corresponding to the occurence of a
        selected topic.'''
        return self.counts
        
    def show(self, tokens=0):
        '''Prints a list of topics and their corresponding counts.'''
        for topic, counts in zip(self.topics, self.counts):
            print("{:s} ({:s})".format(topic, str(counts)))
            
            
if __name__=='__main__':
    #model = TopWordsModel()
    #model.fit(['A', 'B', 'C', 'A'])
    pass
    
    