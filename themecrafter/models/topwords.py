from collections import Counter
from ..preprocessing.groupdict import GroupedDict


def TopWordsInterface:

    def __init__(self, tree):
        '''Extracts labels from a labelled xml tree to obtain the top words.'''
        self.tree = tree
        self.elements = tree.findall('.//*[@label]')
        words = [t.get('label') for t in tokens]
    
        self.model = TopWordsModel()
        self.model.fit(words)
        
    def get_tagged_xml(self):
        '''Use the topic assignments of the model to
        add tags to the xml elements.
        '''
        y = self.model.get_doc_topics()
        for i, tag in enumerate(self.elements):
            topic_id = y[i]
            tag.set('topic', str(topic_id))
        return self.tree

        
class TopWordsModel:
    
    def __init__(self):
        ''''''
        self.groupdict = GroupedDict()
        
    def fit(self, words):
        '''Input is a list of words.'''
        self.words = words
        
        ids = list( range( len(words) ) )
        print(ids)
        self.groupdict.group(ids, words)
        
        self.sel_topics()
            
    def sel_topics(self, k_topics=10, min_count=0, max_count=None):
        '''Returns a list of topics which fit the parameters.'''
        self.topics = []
        self.counts = []
        
        i = 0
        for k, c in self.groupdict.counts():
            if not i < k_topics:
                pass
            elif c < min_count:
                pass
            elif max_count is None:
                self.topics.append(k)
                self.counts.append(c)
                i += 1
            else:
                if c > max_count:
                    pass
                else:
                    self.topics.append(k)
                    self.counts.append(c)
                    i += 1
        
    def get_doc_topics(self, words=None):
        '''Assigns topic indices to the words.'''
        if words is None:
            n = len(self.words)
        else:
            n = len(words)
        
        y = [None]*n
        for topic_id, topic in enumerate(self.topics):
            idlist = self.groupdict.get(topic)
            for i in idlist:
                y[i] = topic_id
        
        return y
    
    def get_doc_ids(self, topic_id):
        '''Returns the indices classified as the given topic_id.'''
        topic = self.topics[topic_id]
        return self.groupdict.get(topic)
    
    def get_topics(self, top_n=None):
        '''Gets a list of words which are the most occuring.
        These will be treated as topics.
        '''
        return self.topics
        
    def get_counts(self):
        '''Returns a list of counts corresponding to the occurence of a
        selected topic.
        '''
        return self.counts
        
    def show(self, tokens=0):
        ''''''
        print(self.topics)
        print(self.counts)
        pass
        for topic, counts in zip(self.topics, self.counts):
            print("{:s} ({:s})".format(topic, str(counts)))
            print("{:s}".format(topic))
            pass
            
            
if __name__=='__main__':
    model = TopWordsModel()
    model.fit(['A', 'B', 'C', 'A'])

    