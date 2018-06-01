# Using simple nltk process documents into sentences and tokens.

import xml.etree.ElementTree as ET

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer

class NLTKPlain:

    def __init__(self):
        self.tbuilder = ET.TreeBuilder()
        
        # Specify tokenizers
        self.sent_tokenizer = None
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
        
        