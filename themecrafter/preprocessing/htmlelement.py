# Module to easily create html elements from the leaves down.


class HtmlElement:
    
    def __init__(self):
        self.tag = ''
        self.attr = dict()
        self.children = []
    
    
    def get_name(self):
        return self.tag
    
    
    def set_name(self, tag):
        self.tag = tag
        
        
    def add(self, element, at=None):
        if at is None:
            self.children.append(element)
        else:
            self.children.insert(0, element)
    

    def get_attr(self, key):
        if key not in self.attr.keys():
            return None
        else:
            return self.attr[key]
    
    
    def set_attr(self, key, val):
        self.attr[key] = val
        
    
    def rm_attr(self, key):
        return self.attr.pop(key, None)
    
    
    def dump_attr(self):
        s = ''
        for k, v in self.attr.items():
            s += ' ' + k + '=' + '\"' + str(v) + '\"'
        return s
    
    
    def dump(self):
        text = ''
        
        if len(self.children)!=0:
            attr = self.dump_attr()
            text += u'<' + self.tag + attr + '>'
        
        for c in self.children:
            if type(c)==str:
                text += c
            else:
                text += c.dump()
        text += '</' + self.tag + '>'
        return text
    
        
        