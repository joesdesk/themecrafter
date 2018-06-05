# This class stores methods on the nlp results.

import xml.etree.ElementTree as ET


def show_tree(tree, level=0):
    print('  '*level, tree, tree.tag, str(tree.attrib), tree.text, tree.tail)
    for c in tree.getchildren():
        show_tree(c, level+1)

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
    
    
if __name__=='__main__':
    pass