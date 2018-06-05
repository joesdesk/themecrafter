# This class stores methods on the nlp results.

import xml.etree.ElementTree as ET

import pandas as pd
from collections import Counter


def save_tree(tree, filename):
    '''Saves the preprocessed documents.'''
    ET.ElementTree(tree).write(filename)
    
def open_tree(filename):
    '''Loads the processed documents.'''
    tree = ET.parse(filename).getroot()
    return tree
    
def tree2string(tree):
    '''Prints the tree as plaintext.'''
    return ET.tostring(tree)

    
def get_all_tokens(tree):
    '''Obtains all tokens from a corpus element.'''
    tokens = []
    for d in tree.get_elements():
        for s in d.get_elements():
            for t in s.get_elements():
                tokens.append(t)
    return tokens

def tokens_summary(tree):
    '''All tokens as a data frame.'''
    all_tokens = []
    for i, d in enumerate(tree.get_elements()):
        for j, s in enumerate(d.get_elements()):
            for k, t in enumerate(s.get_elements()):
                
                ttext = t.as_plaintext()
                tpos = t.get_attr('pos')
                tok = (ttext, tpos)
                
                all_tokens.append((ttext, tpos, i, j, k))
    
    columns=['token', 'pos', 'doc id', 'sen id', 'tok id']
    df = pd.DataFrame(all_tokens, columns=columns)
    
    return df

def count_tokens(tree):
    '''Extracts unique tokens to be part of the lexicon.'''
    unique_tokens = []
    token_count = []
    
    for t in tree.get_all_tokens():
        txt = t.as_plaintext()
        if txt not in lexicon:
            lexicon.append(txt)
    return lexicon


if __name__=='__main__':
    pass