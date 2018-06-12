# pywsd
# https://github.com/alvations/pywsd

# Installation
# pip install -U nltk
# python -m nltk.downloader 'popular'
# pip install -U pywsd

# Successfully installed pywsd-1.1.7

# @misc{pywsd14,
# author =   {Liling Tan},
# title =    {Pywsd: Python Implementations of Word Sense Disambiguation (WSD) Technologies [software]},
# howpublished = {https://github.com/alvations/pywsd},
# year = {2014}
# }

#from pywsd.lesk import simple_lesk

#from .pywsdmod import disambiguate
#from pywsd.similarity import max_similarity as maxsim

#from pywsd.lesk import cached_signatures

from nltk.corpus import wordnet as wn

from .nltkparser import NltkDocParser

from xml.etree.ElementTree import SubElement

#>>> sent = 'I went to the bank to deposit my money'
#>>> ambiguous = 'bank'
#>>> answer = simple_lesk(sent, ambiguous, pos='n')
#>>> print answer
#Synset('depository_financial_institution.n.01')

#>>> print answer.definition()
#'a financial institution that accepts deposits and channels the money into lending activities'

#For all-words WSD, try:

#>>> disambiguate('I went to the bank to deposit my money')
#[('I', None), ('went', Synset('run_low.v.01')), ('to', None), ('the', None), ('bank', Synset('depository_financial_institution.n.01')), ('to', None), ('deposit', Synset('deposit.v.02')), ('my', None), ('money', Synset('money.n.03'))]

#>>> disambiguate('I went to the bank to deposit my money', algorithm=maxsim, similarity_option='wup', keepLemmas=True)
#[('I', 'i', None), ('went', u'go', Synset('sound.v.02')), ('to', 'to', None), ('the', 'the', None), ('bank', 'bank', Synset('bank.n.06')), ('to', 'to', None), ('deposit', 'deposit', Synset('deposit.v.02')), ('my', 'my', None), ('money', 'money', Synset('money.n.01'))]


class PyWSDParser:
    '''From an element with text, creates  a sentence element
    whose token elements are tokens.'''
    
    def __init__(self):
        pass
        
    def parse(self, element):
        element.tag = 'sent'
        
        text = element.text
        element.text = None
        
        sense_tagged = disambiguate(text, keepLemmas=True, prefersNone=False)
        #poses = pos_tag(words)
        
        offset = 0
        for k, (word, label, pos, synset) in enumerate(sense_tagged):
            
            #word, pos = poses[k]
            
            # Fix the replacement done by package
            word, offset = self.find(text, word, offset)
            
            errmsg = 'Error: {' + word + '} not found in {' + text + '}'
            assert not (offset < 0), errmsg
            
            attrib = {}
            attrib['id'] = str(k) 
            attrib['offset'] = str(offset)
            attrib['len'] = str(len(word))
            attrib['pos'] = pos
            attrib['label'] = label
            attrib['synset'] = synset
            
            token = SubElement(element, 'tok', attrib)
            token.text = word
            offset += len(word)
        
        return None
    
    def find(self, sentence, word, offset=0):
        '''Fixes substitutions done that prevents finding.'''
        if word in ['``', "''"]:
            word = '"'
        
        return word, sentence.find(word, offset)



#To read pre-computed signatures per synset:

#>>> cached_signatures['dog.n.01']['simple']
#set([u'canid', u'belgian_griffon', u'breed', u'barker', ... , u'genus', u'newfoundland'])

#>>> cached_signatures['dog.n.01']['adapted']
#set([u'canid', u'belgian_griffon', u'breed', u'leonberg', ... , u'newfoundland', u'pack'])


#>>> wn.synsets('dog')[0]
#Synset('dog.n.01')

#>>> dog = wn.synsets('dog')[0]

#>>> dog.name()
#u'dog.n.01'

#>>> cached_signatures[dog.name()]['simple']
#set([u'canid', u'belgian_griffon', u'breed', u'barker', ... , u'genus', u'newfoundland'])

