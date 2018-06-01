# Using simple nltk process documents into sentences and tokens.

import xml.etree.ElementTree as ET

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer

class NLTKPlain:

    def __init__(self):
        self.tbuilder = ET.TreeBuilder()
        
        self.word_tokenizer = TreebankWordTokenizer()
        
    def make_attr(self, id=None, offset=None):
        attr = {}
        if id is not None:
            attr['id'] = str(id)
        if offset is not None:
            attr['offset'] = str(offset)
        return attr
    
    def parse_corpus(self, docs, id=None, offset=None):
        
        attr = self.make_attr(id, offset)
        self.tbuilder.start('corpus', attr)
        
        for i, doc in enumerate(docs):
            self.parse_doc(doc, id=i, offset=0) # docs are indep = offset 0
        
        self.tbuilder.end('corpus')
        return self.tbuilder.close()
        
    def parse_doc(self, doc, id=None, offset=None):
        
        attr = self.make_attr(id, offset)
        self.tbuilder.start('doc', attr)
        
        # Break the document into sentences.
        k = 0
        rel_offset = 0
        sentences = sent_tokenize(doc)
        for j, s in enumerate(sentences):
            
            # Indicate space before sentence
            rel_offset = doc.find(s, rel_offset)
            assert rel_offset >= 0, s + ' not in ' + id + ' past ' + str(rel_offset)
            self.parse_sent(s, j, offset+rel_offset)
            rel_offset += len(s)
        
        self.tbuilder.end('doc')
        return self.tbuilder.close()
    
    def parse_sent(self, sent, id=None, offset=None):
        
        attr = self.make_attr(id, offset)
        self.tbuilder.start('sent', attr)
        
        rel_offset = 0
        
        # Bug: can't find single quote substrings
        #spans = self.word_tokenizer.span_tokenize(sent)
        words = self.word_tokenizer.tokenize(sent)
        #assert len(spans)==len(words)
        
        # Do parts of speech tagging in addition to tokenization
        poss = pos_tag(words)
        assert len(poss)==len(words)
        
        for k in range(len(words)):
            
            # Indicate space before token
            word, pos = poss[k]
            
            # Stupid replacements by package
            word, rel_offset = self.find(sent, word, rel_offset)
            assert rel_offset >= 0, word + ', not in :' + sent
            
            self.parse_word(word, pos, k, offset+rel_offset)
            rel_offset += len(word)
            k += 1
        
        self.tbuilder.end('sent')
        return self.tbuilder.close()
    
    def parse_word(self, word, pos, id=None, offset=None):
    
        attr = self.make_attr(id, offset)
        attr['pos'] = pos
        self.tbuilder.start('tok', attr)
        
        self.tbuilder.data(word)
        
        self.tbuilder.end('token')
        return self.tbuilder.close()

    def find(self, sentence, word, offset=0):
        '''Fixes substitutions done that prevents finding.'''
        if word in ['``', "''"]:
            word = '"'
        
        return word, sentence.find(word, offset)


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
            
            