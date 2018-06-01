# Taken from https://github.com/Lynten/stanford-corenlp

import xml.etree.ElementTree as ET

from stanfordcorenlp import StanfordCoreNLP


class StanfordPlain:

    def __init__(self, annotators=None):
        self.annotators = annotators
        
    def parse_corpus(self, docs):
    
        nlp = StanfordBase()
        nlp.open()
        
        root = ET.Element('root')
        
        for doc in docs:
            
            xmltagged = nlp.annotate(doc, self.annotators)
            xml = ET.fromstring(xmltext)
    
            root.append(xml)
        
        nlp.close()
        return root


class StanfordBase:

    def __init__(self, quiet=True):
        self.nlp = None
        self.quiet = quiet
        
    def open(self):
        self.nlp = StanfordCoreNLP(r'../stanford-corenlp-full-2018-02-27/', \
            quiet=self.quiet, lang='en')
        
        
    def word_tokenize(self, sentence):
        '''Tokenize.'''
        return self.nlp.word_tokenize(sentence)

        
    def sent_tokenize(self, text):
        '''Tokenize by sentence'''
        return self.annotate(text, 'ssplit')
        
        
    def pos_tag(self, sentence):
        '''Part of Speech.'''
        return self.nlp.pos_tag(sentence)
        
        
    def ner(self, sentence):
        '''Named Entities.'''
        return self.nlp.ner(sentence)
        
        
    def parse(self, sentence):
        '''Constituency Parsing.'''
        return self.nlp.parse(sentence)
        
        
    def dependency_parse(self, sentence):
        '''Dependency Parsing.'''
        return self.nlp.dependency_parse(sentence)
        
        
    def dcoref(self, text):
        '''Dependenc'''
        return self.annotate(text, 'dcoref')
        
        
    def annotate(self, text, annotators=None):
        '''Uses the general stanford annotators'''
        if annotators is None:
            # Full list https://stanfordnlp.github.io/CoreNLP/annotators.html
            annotators = 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref'
        props={'annotators': annotators, \
            'pipelineLanguage': 'en', \
            'outputFormat': 'xml'}
        return self.nlp.annotate(text, properties=props)

        
    def close(self):
        '''Do not forget to close! The backend server will consume a lot memery.'''
        self.nlp.close()
        
        