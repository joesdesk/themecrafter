from bs4 import BeautifulSoup


class HTMLTransform:

    def __init__(self, xmlstring):
        '''Prepares the soup for formatting by adding spaces where needed.'''
        self.soup = BeautifulSoup(xmlstring, "xml")
        
        # Add spaces where appropriate
        offset = 0
        for tag in self.soup.find_all('tok'):
            
            new_offset = int(tag['offset'])
            space_len = max(0, new_offset - offset)
            space = ' '*space_len
            #print(new_offset - offset, tag['offset'], tag.string)
                
            tag.insert_before(space)
            l = len(tag.string) if tag.string is not None else 0
            #print(l)
            offset = new_offset + l
                
    def rename_tags(self):
        '''Change XML tags to HTML elements.'''
        for tag in self.soup.find_all('tok'):
            tag['class'] = 'tok'
            tag.name = 'span'

        for tag in self.soup.find_all('sent'):
            tag['class'] = 'sent'
            tag.name = 'span'
            
        for tag in self.soup.find_all('doc'):
            tag['class'] = 'doc'
            tag.name = 'div'
        
        self.soup.corpus.name = 'html'
    
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
        
    def show_page(self, page=0):
        '''Returns the paginated html at given page.'''
        page = min(0, page)
        page = max(page, len(self.pages)-1)
        
        return self.pages[page]
        
    def to_string(self, page=0):
        ''''''
        return str(self.soup)
        
        