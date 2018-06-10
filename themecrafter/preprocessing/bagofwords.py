# For constructing texts needed for gensim

class BagOfWords:

    def __init__(self, tokenlabel='label2', doc_sel="DOCUMENT"):
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
        
        # Keep the tag references for later retagging
        self.tags_ = tags
        
        # Keep the bag of words
        self.bows_ = bows
        

if __name__=='__main__':
    
    # Load tree
    #from ..nlp.utils import open_tree
    #tree = open_tree("M:/themecrafter/labelled/NLTKPlain2-NOUNS-VERBS-BLACKLIST.xml")
    pass
    # Finally, we convert the tree into a list of lists of words
    #from ..preprocessing.bagofwords import BagOfWords
    #bow = BagOfWords(tokenlabel='label2', doc_sel="DOCUMENT")
    #bow.fit(tree)

    # Bag of words representation of each document (sentence)
    #bows = bow.bows_
    #print(len(bows))

    # Corresponding tree elements for later retagging
    #tags = bow.tags_
    
    