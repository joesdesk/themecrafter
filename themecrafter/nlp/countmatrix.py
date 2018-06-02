# Class to compute a count matrix from a collection of documents which have
# already been preprocessed: i.e. tokenized, potentially including stemming
# and lemmatization.

from collections import Counter
import numpy as np


class TF:
    
    def __init__(self, method='count'):
        if method=='count':
            pass
        
    def fit(self, words):
        '''Returns a dictionary with words as keys and counts as values.'''
        wc = Counter(words)
        return dict(wc)
        
        
class CountMatrix:
    
    def __init__(self):
        pass
        
    def fit(self):
        pass
        

        
if __name__=='__main__':
    
    # Test the functions
    tf = TF()
    doc = """The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made."""
    wc = tf.fit(doc.split(' '))
    for w, c in wc.items():
        print(w, c)