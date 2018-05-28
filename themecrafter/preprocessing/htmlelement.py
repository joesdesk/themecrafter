# Module to easily create html elements from the leaves down.

class HtmlElement:
    
    def __init__(self):
        self.tag = ''
        self.attr = dict()
        self.children = []
        
        
    def insert_element(self, element, at=None):
        if at is None:
            self.children.append(element)
        else:
            self.children.insert(0, element)
        
    
    def dump_attr(self):
        s = ''
        for k, v in self.attr.items():
            s += ' ' + k + '=' + '\"' + v + '\"'
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
        