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

    def paginate(self, n_per_page=10):
        '''Splits the soup into a list of different pages.'''
        doc_elems = [str(tag) for tag in self.soup.find_all('div')]

        self.pages = []
        counted = 0
        while not counted > len(doc_elems):
            page = ''.join(doc_elems[counted:counted+n_per_page])
            page = '<html>' + page + '</html>'
            self.pages.append(page)
            counted += n_per_page

        return len(self.pages)
        
    def show_first_page(self):
        '''Shows the first 10 comments of xml.'''
        docs = self.docs[:10]
        return self.render(docs)

    def show_page(self, page=0):
        '''Returns the paginated html at given page.'''
        page = min(0, page)
        page = max(page, len(self.pages)-1)

        return self.pages[page]

    def to_string(self, page=0):
        ''''''
        return str(self.soup)

    def highlight_words(self, words, fgcolors, bgcolors):
        '''Highlight each word with a color.'''
        for tag in self.soup.find_all('tok'):
            if tag.string in words:
                style = "color:" + fgcolor + "; background-color:" + bgcolor
                tag['style'] = '"' + style + '"'
