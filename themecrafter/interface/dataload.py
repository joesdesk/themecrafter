from ..nlp.corpusparser import CorpusParser
from ..nlp.utils import tree2string


class DataLoadInterface:

    def __init__(self, docs):
        '''Initial parsing of the model.'''
        parser = CorpusParser()
        self.tree = parser.parse(docs)
        
        # Rough parsing of the data
        for d in self.tree.findall('tok'):
            d.tag = 'doc'
    
    def get_xml_string(self):
        return tree2string(self.tree)