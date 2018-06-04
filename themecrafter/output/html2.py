# The idea behind this module is to act only as 
# a visualization of the comments.

from bs4 import BeautifulSoup


class HTMLTransform:

    def __init__(self, xmlstring):
        '''Prepares the soup for formatting by adding spaces where needed.'''
        soup = BeautifulSoup(xmlstring, "xml")
        docs = list(soup.corpus.children)
        for doc in docs:
            self._spaceout(doc)
        self.docs = docs
        
        # Number of documents and number of pages
        self.n_per_page = 10
        self.pages = self.paginate(10)
        
    def _spaceout(self, doc):
        '''Add spaces where appropriate'''
        offset = 0
        for tag in doc.find_all('tok'):

            new_offset = int(tag['offset'])
            space_len = max(0, new_offset - offset)
            space = ' '*space_len

            tag.insert_before(space)
            l = len(tag.string) if tag.string is not None else 0
            offset = new_offset + l
            
    def _rename_tags(self, soup):
        '''Change XML tags to HTML elements.'''
        for tag in soup.find_all('tok'):
            tag['type'] = 'tok'
            tag.name = 'span'

        for tag in soup.find_all('sent'):
            tag['type'] = 'sent'
            tag.name = 'span'

        for tag in soup.find_all('doc'):
            tag['type'] = 'doc'
            tag.name = 'div'

        soup.corpus.name = 'html'
        
    def render(self, docs, rename_tags=False):
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
        '''Finds the number of pages.'''
        n_docs = len(self.docs)
        pages = []
        counted = 0
        while counted < n_docs:
            upto = min(counted + n_per_page, n_docs)
            page = self.docs[counted: upto]
            
            pages.append(page)
            counted = upto
            
        self.pages = pages
        self.n_per_page = n_per_page
        return len(self.pages)
        
    def show_page(self, n):
        '''Shows the page, a list of documents to be rendered.
        Here, n is from 1 to the total number of pages.'''
        page = self.pages[n-1]
        return self.render(page)

    def highlight_words(self, words, fgcolors, bgcolors):
        '''Highlight each word with a color.'''
        for tag in self.soup.find_all('tok'):
            if tag.string in words:
                style = "color:" + fgcolor + "; background-color:" + bgcolor
                tag['style'] = '"' + style + '"'

                
if __name__=='__main__':
    
    from ..nlp.session import PreprocessingSession
    
    session = PreprocessingSession()
    session.open_tree('try.xml')
    xmlstring = session.tree_as_string()
    
    html = HTMLTransform(xmlstring)
    
    