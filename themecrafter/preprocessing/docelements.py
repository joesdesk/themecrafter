# A python class to organize parsing and documents.

from .baseelement import BaseElement

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize


class TokenElement(BaseElement):
    def __init__(self, text):
        BaseElement.__init__(self)
        self.set_name('token')
        self.parse(text)
        
    def parse(self, text):
        self.add(text)
        

class SentenceElement(BaseElement):
    def __init__(self, text):
        BaseElement.__init__(self)
        self.set_name('sentence')
        self.parse(text)
        
    def parse(self, text):
        words = word_tokenize(text)
        postags = pos_tag(words)
        
        I = 0
        for i in range(len(postags)):
            
            w, t = postags[i]
            
            token = TokenElement(w)
            token.set_attr('pos', t)
            
            token.set_attr('i', i)
            
            # Indicate space before token
            I_new = text.find(w, I)
            spacelen = I_new - I
            self.add(' '*spacelen)
            
            # Record location in document
            token.set_attr('loc', I)
            I = I_new + len(w)
            
            # Add token
            self.add(token)
            

class DocumentElement(BaseElement):
    def __init__(self, text):
        BaseElement.__init__(self)
        self.set_name('document')
        self.parse(text)
        
    def parse(self, text):
        sentences = sent_tokenize(text)
        
        I = 0
        for i, s in enumerate(sentences):
            sentence = SentenceElement(s)
            
            sentence.set_attr('i', i)
            sentence.set_attr('len', len(s))
            
            # Indicate space before sentence
            I_new = text.find(s, I)
            spacelen = I_new - I
            self.add(' '*spacelen)
            
            # Record location in document
            sentence.set_attr('loc', I)
            I = I_new + len(s)
            
            # Add token
            self.add(sentence)
        

class CorpusElement:
    def __init__(self, docs):
        '''Initialize a corpus with a list of documents.'''
        BaseElement.__init__(self)
        self.set_name('corpus')
        
        for d in docs:
            document = DocumentElement(d)
            self.add(document)

    def get_all_tokens(self):
        '''Extracts all tokens from all sentences from all documents.'''
        all_tokens = []
        for d in self.children:
            for s in d.children:
                for t in s.children:
                    all_tokens.append(t.children)
        return all_tokens
    
    def get_lexicon(self):
        '''Extracts unique tokens to be part of the lexicon.'''
        lexicon = []
        for t in self.get_all_tokens():
            if t not in lexicon:
                lexicon.append(t)
        return lexicon
        
    def token2lid(self, token):
        '''Converts token to id in lexicon.'''
        for i, l in enumerate(self.lexicon):
            if l==token:
                return i
                

                