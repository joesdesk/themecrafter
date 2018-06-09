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
        
        # Keep the tag references for later retagging
        self.tags_ = tags
        
        # Keep the bag of words
        self.bows_ = bows    
        
        
def get_bag_of_words():
    
    # Obtain documents
    from ..nlp.utils import open_tree, show_tree, save_tree
    tree = open_tree("M:/themecrafter/trees/NLTKPlain2.xml")

    # Reduce labelling
    from .labeltransform import LabelTransform
    from ..nlp.nltklemmatizer import NOUN_POS

    labeltransform = LabelTransform(labelname='label2')

    labeltransform.lemmatize = True
    labeltransform.rm_stopwords = True
    labeltransform.rm_punctuation = True
    labeltransform.rm_char_len = 2

    labeltransform.pos_whitelist = NOUN_POS
    labeltransform.label_blacklist = ['program', 'ubc', 'school', \
        'student', 'course']

    # Add new labels to tree
    labeltransform.fit(tree)
    #show_tree(tree)

    # Obtain all tokens with the new label
    all_labels = [t.get('label2') for t in tree.findall('.//tok[@label2]')]

    # Now we remove the most common words
    from collections import Counter
    token_counts = Counter(all_labels)

    blacklist = []
    for k, v in token_counts.items():
        if v < 10:
            blacklist.append(k)

    # Remove the labels which are in the blacklist
    for t in tree.findall('.//tok[@label2]'):
        word = t.get('label2')
        if word in blacklist:
            t.attrib.pop('label2')

    # Finally, we convert the tree into a list of lists of words
    #from ..preprocessing.bagofwords import BagOfWords
    bow = BagOfWords(tokenlabel='label2', doc_sel="DOCUMENT")
    bow.fit(tree)

    # Bag of words representation of each document (sentence)
    bows = bow.bows_
    return bows

    # Corresponding tree elements for later retagging
    #tags = bow.tags_
    
    