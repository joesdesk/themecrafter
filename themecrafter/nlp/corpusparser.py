from xml.etree.ElementTree import TreeBuilder
from .utils import show_tree

class CorpusParser:
    '''Creates a corpus element whose tokens are documents.'''
    
    def __init__(self):
        pass
        
    def parse(self, list_of_docs):
        builder = TreeBuilder()
        builder.start('corpus')
        
        for i, doc in enumerate(list_of_docs):
            attrib = {'id':i, 'len':len(doc)}
            
            builder.start('tok', attrib)
            builder.data(doc)
            builder.end('tok')
        
        builder.end('corpus')
        return builder.close()
        

if __name__=='__main__':
    docs = ['The cat flew out of the box.', \
        'It is raining today.']
        
    parser = CorpusParser()
    tree = parser.parse(docs)
    
    show_tree(tree)