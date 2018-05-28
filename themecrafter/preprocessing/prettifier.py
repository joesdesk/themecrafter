# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#modifying-the-tree

# Using anchors, id vs name
# https://stackoverflow.com/questions/484719/html-anchors-with-name-or-id

from bs4 import BeautifulSoup

from themecrafter.preprocessing.document import Document


class TaggedCorpus:

    def __init__(self):
    
        self.root = BeautifulSoup('', "lxml")
        
        # Created main html
        htmltag = self.root.new_tag('html')
        self.root.append(htmltag)
        
        # Add head tag
        headtag = self.root.new_tag('head')
        self.root.html.append(headtag)
        
        # Add body tag
        bodytag = self.root.new_tag('body')
        self.root.html.append(bodytag)
    
    
    def parse_doc(self, doc):
        '''Parses the document into its constituents.
        Returns a tag to be appended.'''
        pdoc = Document(doc)

        doctag = self.root.new_tag('document')
        for s in pdoc.sentences:
        
            senttag = self.root.new_tag('sentence')
            for t in s.tokens:
            
                toktag = self.root.new_tag('token')
                toktag.string = t.text
                toktag['pos'] = t.pos
                toktag['tid'] = t.text
                toktag['len'] = len(t.text)
                toktag['sloc'] = t.sloc
                toktag['dloc'] = t.dloc
                senttag.append(toktag)
    
            doctag.append(senttag)
        
        return doctag
        
    
    def add_doc(self, doc):
        
        # Create new tag for doc
        
        
        
        
    
    
        
        
    

    # HTML needs to be built from the inside out
    page = BeautifulSoup('', "lxml")
    
    for i, s in enumerate(docs):
        comment_tag = page.new_tag('comment')
        comment_tag['class'] = 'comment'
        comment_tag['id'] = i
        comment_tag.string = s
        page.append(comment_tag)
        
        lineskip_tag = page.new_tag('br')
        page.append(lineskip_tag)
    
    # Container for everything
    container = BeautifulSoup('', "lxml")
    bodytag = container.new_tag('body')
    container.append(bodytag)
    container.body.append(page)
    page = container
    
    container = BeautifulSoup('', "lxml")
    htmltag = container.new_tag('html')
    container.append(htmltag)
    container.html.append(page)
    page = container
        
    return page.prettify()