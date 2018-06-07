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
            self._rename_tags(doc)
        self.docs = docs
        
        # Dictionary of topics containing the selections as strings
        self.cached_pages = dict()
        
        # Number of documents and number of pages
        self.n_per_page = 10
        
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
            
    def _rename_tags(self, doc_elem):
        '''Change XML tags to HTML elements.'''
        for tag in doc_elem.find_all('tok'):
            tag['type'] = 'tok'
            tag.name = 'span'

        for tag in doc_elem.find_all('sent'):
            tag['type'] = 'sent'
            tag.name = 'span'
            #tag['style'] = "font-size:10pt"

        #for tag in doc_elem.find_all('doc'):
            #tag['type'] = 'doc'
            #tag.name = 'div'
            #tag['style'] = "padding-bottom:10px"

        doc_elem.name = 'doc'
        doc_elem['type'] = 'doc'
        
    def paginate(self, docs):
        '''Turns the documents into a list of html strings for pages.'''
        
        n_docs = len(docs)
        n_per_page = self.n_per_page
        
        pages = []
        counted = 0
        while counted < n_docs:
            upto = min(counted + n_per_page, n_docs)
            
            page = r'<html>'
            for i in range(counted,upto):
                doc = docs[i]
                page += str(doc)
            page += r'</html>'
            
            pages.append(page)
            counted = upto
            
        return pages

    def highlight_doc(self, doc, topic=None):
        '''Highlight each word with a color.'''
        if topic==None:
            return None

        for tag in doc.find_all(attrs={'topic':True}):
            
            # Clear existing styles
            tag['style'] = None
            
            # Assign styles
            loc = tag['topic'].find(topic)
            if not loc < 0:
                tagtype = tag['type']
                if tagtype=='doc':
                    pass
                if tagtype=='sent':
                    tag['style'] = "background-color:#E8D898;"
                if tagtype=='tok':
                    pass
                
    def add_cache(self, topic=None, indices=None):
        '''Takes a list of indices to sort and select the documents
        prior to pagination.'''
        
        if indices is None:
            docs = self.docs
        else:
            docs = []
            for i in indices:
                doc = self.docs[i]
                self.highlight_doc(doc, topic)
                docs.append(self.docs[i])
        
        pages = self.paginate(docs)
        self.cached_pages[topic] = pages
        
        
if __name__=='__main__':
    
    from ..nlp.utils import open_tree, tree2string
    
    tree = open_tree('M:/themecrafter/results/NLTKPlain2_topwords.xml')
    xmlstring = tree2string(tree)
    
    html = HTMLTransform(xmlstring)
    html.add_cache()
    html.add_cache('hello', [1,2,3])
    
    