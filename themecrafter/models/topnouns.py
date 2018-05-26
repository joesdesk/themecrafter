# This model takes as its topics the top n nouns.
# Then, each document is tokenized by sentence and the sentiment of each
# sentence is analyzed which is the sentence associated with each topic if it
# appears in the sentence.

from collections import Counter
from ..preprocessing.document import Corpus

class TopNWords:

    def __init__(self, k_topics=10):
        self.k_topics = k_topics
        self.topics = []
    
    def fit(self, docs):
        '''Extracts the top 10 nouns and highlights them.'''
        
        corpus = Corpus(docs)
        self.corpus = corpus
        
        all_tokens = corpus.get_all_tokens()
        
        noun_tags = ['NN','NNP','NNPS', 'NNS']
        noun_tokens = [t for t in all_tokens if t.pos in noun_tags]
        
        nouns = [t.text for t in noun_tokens]
        
        # Obtain topics based on nouns
        wcount = Counter(nouns)
        topnouns = wcount.most_common()[:self.k_topics]
        topics = [w for w, c in topnouns]
        
        self.topics = topics
    
    
    def pred(self):
        '''Show tagged documents via html.'''
        
        h = HtmlElement()
        h.tag = 'html'
        
        for doc in corpus.docs:
            hcom = HtmlComment(doc)
            comm = hcom.highlight_tags(topics)
            h.add_element(comm)
            
            linebreak = HtmlElement()
            linebreak.tag = 'br'
            h.add_element(linebreak)
        
        return h.dump()