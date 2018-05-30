# A python class to organize parsing and documents.

from collections import Counter

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize


class BaseElement:
    
    def __init__(self):
        self.name = ''
        self.attrs = dict()
        self.contents = []
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def add(self, element, at=None):
        if at is None:
            self.contents.append(element)
        else:
            self.contents.insert(0, element)
    
    def get_attr(self, key):
        if key not in self.attrs.keys():
            return None
        else:
            return self.attrs[key]
    
    def set_attr(self, key, val):
        self.attrs[key] = val
        
    def pop_attr(self, key):
        return self.attrs.pop(key, None)
    
    def attr_as_string(self):
        s = ''
        for k, v in self.attrs.items():
            s += ' ' + k + '=' + '\"' + str(v) + '\"'
        return s
    
    def get_elements(self):
        children = []
        for c in self.contents:
            if type(c) is not str:
                children.append(c)
        return children
        
    def as_plaintext(self):
        text = ''#' '*self.offset
        for c in self.contents:
            if type(c)==str:
                text += c
            else:
                text += c.as_plaintext()
        return text
    
    def as_html_text(self):
        text = ''#' '*self.offset
        
        if len(self.contents)!=0:
            attrs = self.attr_as_string()
            text += u'<' + self.name + attrs + '>'
        
        for c in self.contents:
            if type(c)==str:
                text += c
            else:
                text += c.as_html_text()
        
        text += '</' + self.name + '>'
        return text


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
            #token.set_offset(spacelen)
            
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
            #sentence.set_offset(spacelen)
            
            # Record location in document
            sentence.set_attr('loc', I)
            I = I_new + len(s)
            
            # Add token
            self.add(sentence)
        

class CorpusElement(BaseElement):
    def __init__(self, docs):
        '''Initialize a corpus with a list of documents.'''
        BaseElement.__init__(self)
        self.set_name('corpus')
        
        for d in docs:
            document = DocumentElement(d)
            self.add(document)
            

class NltkPlain:
    def __init__(self, docs):
        CorpusElement.__init__(self, docs)
        
    def get_all_tokens(self):
        '''Obtains all tokens from a corpus element.'''
        tokens = []
        for d in self.get_elements():
            for s in d.get_elements():
                for t in s.get_elements():
                    tokens.append(t)
        return tokens
    
    def get_unique_tokens(self):
        '''Extracts unique tokens to be part of the lexicon.'''
        lexicon = []
        for t in self.get_all_tokens():
            txt = t.as_plaintext()
            if txt not in lexicon:
                lexicon.append(txt)
        return lexicon
    
    def to_html_file(self, file):
        html_text = self.as_html_text()
        
        f = open(file, 'w+')
        f.write(html_text)
        f.close()
    
    