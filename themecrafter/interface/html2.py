# The idea behind this module is to act only as 
# a visualization of the comments.

from bs4 import BeautifulSoup


class HTMLTransform:

    def __init__(self, xmlstring):
        '''Prepares the soup for formatting by adding spaces where needed.'''
        soup = BeautifulSoup(xmlstring, "xml")
        docs = soup.corpus.contents
        for doc in docs:
            self._spaceout(doc)
        self._rename_tags(soup)
        self.docs = docs
        
        # Indices for selection and order of documents
        self.sel_ids = None
        
        # Number of documents and number of pages
        self.n_per_page = 10
        
        self.pages = None
        self.n_pages = self.paginate(10)
        
       
        
    def _spaceout(self, tag):
        '''Add spaces where appropriate'''
        offset = 0
        for t in tag.find_all(True, recursive=False):

            if not t.has_attr('offset'):
                return None
            
            loc_offset = int( t.get('offset') )
            if loc_offset is not None:

                #print(t.string)

                space_len = loc_offset - offset
                space = ' '*space_len

                #print(t.name)
                t.insert_before(space)
                self._spaceout(t)

                text_len = int(t.get('len'))
                offset = loc_offset + text_len
            
    def _rename_tags(self, soup):
        '''Change XML tags to HTML elements.'''
        for tag in soup.find_all('tok'):
            tag['type'] = 'tok'
            tag.name = 'span'

        for tag in soup.find_all('sent'):
            tag['type'] = 'sent'
            tag.name = 'span'
            #tag['style'] = "font-size:10pt"

        for tag in soup.find_all('doc'):
            tag['type'] = 'doc'
            #tag.name = 'div'
            #tag['style'] = "padding-bottom:10px"

        soup.corpus.name = 'html'
        
    def render(self, docs, rename_tags=True):
        '''Renders the selection of documents.'''
        soup = BeautifulSoup('', "lxml")
        
        # Add containing element
        toptag = soup.new_tag('corpus')
        soup.append(toptag)
        
        # Add documents
        for doc in docs:
            soup.corpus.append(doc)
        
        # Rename of needed
        if rename_tags:
            self._rename_tags(soup)
            
        # Do highlighting
        # ...
        
        return str(soup)

    def paginate(self, n_per_page):
        '''Sets the text of the pages.'''
        print(len(self.docs))
        # First, apply selection
        if self.sel_ids is not None:
            docs = []
            for i in self.sel_ids:
                assert i < len(self.docs), str(i) + "is not less than" + str(len(self.docs))
                docs.append(self.docs[i])
        else:
            docs = self.docs
                
        n_docs = len(docs)
        pages = []
        counted = 0
        while counted < n_docs:
            upto = min(counted + n_per_page, n_docs)
            
            page = r'<html>'
            for i in range(counted,upto):
                page += str(docs[i])
            page += r'</html>'
            
            pages.append(page)
            counted = upto
            
        self.pages = pages
        self.n_per_page = n_per_page
        return len(self.pages)
        
    
    #def pages(self):
        #'''Shows the page, a list of documents to be rendered.
        #Here, n is from 1 to the total number of pages.'''
        #return self.pages
        #page = self.pages[n]
        #return self.render(page, rename_tags=True)

    def highlight_words(self, words, fgcolors, bgcolors):
        '''Highlight each word with a color.'''
        for tag in self.soup.find_all('tok'):
            if tag.string in words:
                style = "color:" + fgcolor + "; background-color:" + bgcolor
                tag['style'] = '"' + style + '"'
                
    def highlight(self, topic, color):
        for doc in self.docs:
            #print(doc.name)
            #doc.name = "doc"
            for tag in doc.find_all(attrs={'topic':True}):
                #print(tag.name)
                loc = tag['topic'].find(topic)
                if not loc < 0:
                    if tag.name == 'sent':
                        tag['style'] = "color:white; background-color:green;"
                    else:
                        tag['style'] = "color:white; background-color:black;"
                else:
                    tag['style'] = ""
                        
        
    def set_sel(self, indices):
        '''Takes a list of indices to sort and select the documents
        prior to pagination.'''
        self.sel_ids = indices
        
        
if __name__=='__main__':
    
    from ..nlp.utils import open_tree, tree2string
    
    tree = open_tree('M:/themecrafter/results/NLTKPlain2_topwords.xml')
    xmlstring = tree2string(tree)
    
    html = HTMLTransform(xmlstring)
    
    html.highlight('student', '#CCCCCC')
    
    