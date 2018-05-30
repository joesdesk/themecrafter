# Module to easily create tree elements from the leaves down.


class Element:
    
    def __init__(self):
        self.name = ''
        self.attrs = dict()
        self.children = []
    
    
    def get_name(self):
        return self.name
    
    
    def set_name(self, name):
        self.name = name
        
        
    def add(self, element, at=None):
        if at is None:
            self.children.append(element)
        else:
            self.children.insert(0, element)
    

    def get_attr(self, key):
        if key not in self.attrs.keys():
            return None
        else:
            return self.attrs[key]
    
    
    def set_attr(self, key, val):
        self.attrs[key] = val
        
    
    def pop_attr(self, key):
        return self.attrs.pop(key, None)
    
    
    def attr_to_string(self):
        s = ''
        for k, v in self.attrs.items():
            s += ' ' + k + '=' + '\"' + str(v) + '\"'
        return s
    
    
    def to_string(self):
        text = ''
        
        if len(self.children)!=0:
            attrs = self.attr_to_string()
            text += u'<' + self.name + attrs + '>'
        
        for c in self.children:
            if type(c)==str:
                text += c
            else:
                text += c.dump()
        text += '</' + self.name + '>'
        return text
    
        
        