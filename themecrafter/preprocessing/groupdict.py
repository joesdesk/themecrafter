# Grouping items in a list but keeping track of
# the items which were grouped together.

from collections import defaultdict, Counter


class GroupedDict:
    '''Grouping items in a list but keeping track of the items
    which were grouped together.
    '''
    
    def __init__(self):
        self.container = defaultdict(list)
    
    def group(self, values, by):
        '''Computes a dictionary whose keys are the unique values in `by`
        and the corresponding dictionary value is the list of items
        in `values` corresponding to the value in `by`.
        '''
        for k, v in zip(by, values):
            self.container[k].append(v)
        return None
            
    def items(self):
        return self.container.items()
    
    def values(self):
        return self.container.values()
    
    def keys(self):
        return self.container.keys()
    
    def counts(self):
        counts = Counter()
        for k, v in self.items():
            counts[k] = len(v)
        return counts.most_common()
    
    def pop(self, key, default=None):
        return self.container.pop(key, default)
        
    def get(self, key, default=None):
        return self.container.get(key, default)
        
        