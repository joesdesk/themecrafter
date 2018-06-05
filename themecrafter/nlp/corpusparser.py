from xml.etree.ElementTree import TreeBuilder


class CorpusParser:
    '''Creates a corpus element.'''
    
    def __init__(self):
        pass
        
    def parse(self, text):
        builder = TreeBuilder()
        
        builder.start('corpus')
        builder.data(text)
        builder.end('corpus')
        
        return builder.close()
        

if __name__=='__main__':
    pass