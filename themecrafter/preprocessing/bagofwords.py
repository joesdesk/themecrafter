# For constructing texts needed for gensim

class BagOfWords:

    def __init__(self, tokenlabel='label', doc_sel="DOCUMENT"):
        '''Initializes variables.'''
        
        # For word, use a specific label
        self.tokenlabel = tokenlabel
        if tokenlabel is not None:
            self.tokenxpath = '[@{:s}]'.format(tokenlabel)
        else:
            self.tokenxpath = ""
        self.tokenxpath = './/tok' + self.tokenxpath
        
        # Use documents as is, or use sentences as documents
        if doc_sel=="DOCUMENT":
            self.doc_xpath = './/doc'
        elif doc_sel=="SENTENCE":
            self.doc_xpath = './/doc//sent'
            
        # Internal results
        self.tags_ = None
        self.bows_ = None
            
    def fit(self, tree):
        '''Creates a bag of words representation of a document
        based on a given label.
        '''
        tags = []
        bows = []
        
        for d in tree.findall(self.doc_xpath):
            
            # Extract the word to add to bow
            words = []
            for t in d.findall(self.tokenxpath):
                
                word = t.get(self.tokenlabel)
                words.append(word)
            
            bows.append(words)
            tags.append(d)
            
        self.tags_ = tags    # Keep the tag references for later retagging
        self.bows_ = bows    # Keep the bag of words
        
        
if __name__=='__main__':

    from ..nlp.utils import open_tree, show_tree, save_tree
    tree = open_tree("M:/themecrafter/results/NLTKPlain2.xml")

    x = BagOfWords('label', tree)
    
    