# A python class to organize parsing and documents.

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize


class Token:
    def __init__(self, text):
        self.text = text
        
        self.pos = ''
        
        self.i = 0
        
        self.sid = 0
        self.sloc = 0
        
        self.did = 0
        self.dloc = 0
        

class Sentence:
    def __init__(self, text):
        self.text = text
        
        self.tokens = []
        
        self.i = 0
        
        self.did = 0
        self.dloc = 0
    
    def parse(self):
        words = word_tokenize(self.text)
        postags = pos_tag(words)
        
        I = 0
        for i in range(len(postags)):
            
            w, t = postags[i]
            
            tok = Token(w)
            tok.pos = t
            
            tok.i = i
            tok.sid = self.i
            tok.did = self.did
            
            I = self.text.find(w, I)
            tok.sloc = I
            tok.dloc = self.dloc + I
            I += len(w)
            
            self.tokens.append(tok)
            

class Document:
    def __init__(self, text):
        self.text = text
        
        self.sentences = []
        
        self.i = 0
        
    def parse(self):
        sentences = sent_tokenize(self.text)
        
        I = 0
        for i, s in enumerate(sentences):
            sent = Sentence(s)
            
            sent.i = i
            sent.did = self.i
            
            I = self.text.find(s, I)
            sent.dloc = I
            I += len(s)
            
            sent.parse()
            self.sentences.append(sent)
        

class Corpus:
    def __init__(self, docs):
        '''Initialize a corpus with a list of documents.'''
        self.text = ""
        for doc in docs:
            self.text += doc + '\n\n'
        
        self.docs = []
        for i, d in enumerate(docs):
            doc = Document(d)
            doc.i = i
            doc.parse()
            self.docs.append(doc)
            
        self.tokens = self.get_all_tokens()
        self.lexicon = self.get_lexicon()
            
    def get_all_tokens(self):
        '''Extracts all tokens from all sentences from all documents.'''
        
        all_tokens = []
        for d in self.docs:
            for s in d.sentences:
                for t in s.tokens:
                    all_tokens.append(t)
        return all_tokens
    
    def get_lexicon(self):
        '''Extracts unique tokens to be part of the lexicon.'''
        lexicon = []
        for t in self.tokens:
            if t.text not in lexicon:
                lexicon.append(t.text)
        return lexicon
        
    def token2lid(self, token):
        '''Converts token to id in lexicon.'''
        for i, l in enumerate(self.lexicon):
            if l==token:
                return i
                
                