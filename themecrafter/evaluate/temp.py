import numpy as np


def clear_classes(tree):
    '''For each element in the tree, remove tags'''
    for tag in tree.findall(attrs={'class':True}):
        print(tag)
    

def classify(tags, y):
    '''Add class to y.'''
    for i, t in enumerate(tags):
        t.attrib['class'] = str(y[i])
        

def sent_ranges(tree):
    '''Returns a list of ranges corresponding to the range of sentences
    in each document of a tree.
    '''
    ranges = []
    start = 0
    for d in tree.findall('.//doc'):
        nsents = len( d.findall('.//sent') )
        b = start + nsents
        ranges.append((start, b))
        start = b
    return ranges
    
    
def aggr_weights(V, ranges):
    '''Given a matrix of weights, and list of ranges,
    returns a matrix of weights where each row corresponds to the average
    weights in the corresponding range.'''
    E = []
    for i, (a,b) in enumerate(ranges):
        Q = np.sum(V[a:b,:], axis=0)
        E.append( Q / (b-a) )
    R = np.array(E)
    return R
    
    