# Module for extracting words or features from a tree
# into various forms to be fitted by models.

class AllWords:

    def __init__(self, tokenlabel='label'):
        '''Specifies the attribute of the token to treat as a word.
        If None, extracts the text of the token to be the word.
        '''
        
        # Create the path to find tokens of the corpus
        self.tokenlabel = tokenlabel
        if tokenlabel is not None:
            self.token_xpath = '[@{:s}]'.format(tokenlabel)
        else:
            self.token_xpath = ""
        self.token_xpath = './/tok' + self.token_xpath
        
        self.tags_ = []
        self.words_ = []
        
    def fit(self, tree):
        '''Extracts words from a tree.'''
        
        # Keep the tag references for later retagging
        self.tags_ = elements = tree.findall('.//*[@label]')
        
        # Keep the bag of words
        self.words_ = [t.get('label') for t in elements]
        

class BagOfWords:

    def __init__(self, tokenlabel='label', doc_sel="DOCUMENT"):
        '''Specifies the element of a corpus to treat as a document.
        Can be one of "DOCUMENT" or "SENTENCE".
        Specifies the attribute of the token to treat as a word.
        If None, extracts the text of the token to treat as a word.
        '''
        
        # Create the path to find tokens of the document
        self.tokenlabel = tokenlabel
        if tokenlabel is not None:
            self.token_xpath = '[@{:s}]'.format(tokenlabel)
        else:
            self.token_xpath = ""
        self.token_xpath = './/tok' + self.token_xpath
        
        # Use documents as is, or treat sentences as documents
        if doc_sel=="DOCUMENT":
            self.doc_xpath = './/doc'
        elif doc_sel=="SENTENCE":
            self.doc_xpath = './/doc//sent'
            
        # Store results of fit here
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
            for t in d.findall(self.token_xpath):
                
                word = t.get(self.tokenlabel)
                words.append(word)
            
            bows.append(words)
            tags.append(d)
        
        # Keep the tag references for later retagging
        self.tags_ = tags
        
        # Keep the bag of words
        self.bows_ = bows
        

if __name__=='__main__':
    pass
    
    