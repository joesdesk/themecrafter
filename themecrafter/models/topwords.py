from ..nlp.utils import tree2string

from collections import Counter
from ..preprocessing.groupdict import GroupedDict

from ..matrix.castdoc import CountMatrix

import numpy as np
import pandas as pd

from .utils import rank2id


class TopWordsInterface:

    def __init__(self, tree):
        '''Extracts labels from a labelled xml tree to obtain the top words.'''
        self.tree = tree
        self.elements = tree.findall('.//*[@label]')
        words = [t.get('label') for t in self.elements]
    
        self.model = TopWordsModel()
        self.model.fit(words)
        
    def tag_xml_tokens(self):
        '''Use the topic assignments of the model to
        add topic tags to the xml token elements.
        '''
        y = self.model.get_doc_topics()
        for i, tag in enumerate(self.elements):
            topic_id = y[i]
            if topic_id is not None:
                tag.set('topic', str(topic_id))
        return self.tree

    def tag_xml_sents(self):
        '''Use the topic assignments of the tokens to
        add topic tags to the xml sentence elements.'''
        for s in self.tree.findall('.//doc//sent'):
            
            # All tokens in a sentence with a topic tag
            sent_tokens = s.findall('.//tok[@topic]')
            
            topics = [tok.attrib.pop('topic') for tok in sent_tokens]
            topics = list(set(topics))
            
            if len(topics) > 0:
                topic_str = ",".join(topics)
                s.set('topic', topic_str)
                
    def test_tag_xml_sents(self):
        '''Prints the topics in each sentence as a diagnostic.'''
        for i, sent in enumerate(self.tree.findall('.//doc//sent')):
            topic = sent.get('topic', None)
            if topic is not None:
                print(topic, end=',')
                pass
    
    def get_doc_topic_bow(self):
        '''Extract the topics for each document in the form
        of a bag of words.
        '''
        docs_topic_bow = []
        for d in self.tree.findall('.//doc'):
            
            sent_tokens = d.findall('.//sent[@topic]')

            topics = [ sent.get('topic') for sent in sent_tokens ]
            topics = ",".join(topics)
            
            if not topics=="":
                docs_topic_bow.append( topics.split(',') )
            else:
                docs_topic_bow.append([])
        return docs_topic_bow
                
    def test_get_doc_topic_bow(self):
        '''Prints the topics in each document.'''
        docs_topics = self.get_doc_topic_bow()
        for i, l in enumerate(docs_topics):
            print("document", i, "has", len(l), "topics:", l)
            pass

    def get_doc_term_matrix(self, doc_topic_bow=None):
        '''Convert the document-topic bow into a count matrix.'''
        if doc_topic_bow is None:
            doc_topic_bow = self.get_doc_topic_bow()
        doc_term_matrix = CountMatrix()
        X = doc_term_matrix.fit(doc_topic_bow)
        topics = doc_term_matrix.vocab
        return X, topics
        
    def topic_counts(self):
        '''Returns a two-column data frame with topic names
        and document counts.'''
        topics = self.model.get_topics()
        counts = self.model.get_counts()
        df = pd.DataFrame({'topics': topics, 'counts':counts})
        return df
    
    def get_xml_string(self):
        '''After the fit, returns the tagged xml for display.'''
        self.tag_xml_tokens()
        self.tag_xml_sents()
        return tree2string(self.tree)
        
    def get_docs(self, topic_num):
        '''Given a topic number, obtain the labels'''
        topic_key = self.model.get_topics()[topic_num]
        
        doc_term_matrix, null = self.get_doc_term_matrix()
        doc_term_matrix = doc_term_matrix.toarray()
        
        doc_weights = np.squeeze(doc_term_matrix[:,topic_num])
        print(doc_weights.shape)
        rank = np.argsort(-doc_weights)
        
        ids = rank2id(rank)
        weights = doc_weights[ids]
        
        return ids[weights>0].tolist()
    
    def topic2docids(self):
        n_topics = len(self.model.get_topics())
        topic2docs = [self.get_docs(i) for i in range(n_topics)]
        return topic2docs
        
        
class TopWordsModel:
    
    def __init__(self):
        ''''''
        self.groupdict = GroupedDict()
        
    def fit(self, words):
        '''Input is a list of words.'''
        self.words = words
        
        ids = list( range( len(words) ) )
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
            elif c > max_count:
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
    
    def get_topic_of_original_words(self, topic_id):
        '''Returns the word indices of original fitted words which are
        classified into the given topic_id.'''
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
    #model = TopWordsModel()
    #model.fit(['A', 'B', 'C', 'A'])

    #
    from ..nlp.utils import open_tree, show_tree, save_tree
    tree = open_tree("M:/themecrafter/parsed/NLTKPlain2_NEW.xml")
    #show_tree(tree)
    
    #
    from ..preprocessing.labeltransform import LabelTransform
    transform = LabelTransform()
    transform.fit(tree)
    #show_tree(tree)
    
    model = TopWordsInterface(tree)
    model.tag_xml_tokens()
    model.tag_xml_sents()
    #show_tree(model.tree)
    
    print(model.topic2docids())