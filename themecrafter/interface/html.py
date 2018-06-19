# Module to visualize the comments through html.

from math import floor
from bs4 import BeautifulSoup

from .htmlrender import doc2tr
from .html_styling import highlight


class HTMLInterface:
    '''The interface for viewing the XML documents.'''
    
    def __init__(self, xmlstring):
        '''Takes an XML string and turns it into a soup so that elements
        can be easily extracted and rendered.
        '''
        # Convert the entire XML string into a soup.
        soup = BeautifulSoup(xmlstring, "xml")
        
        # The documents are cached via a list of soup tags so that
        # only selected documents are rendered saving time.
        self.docs = soup.corpus.contents
        
        # Selection of documents
        self.sel_doc_ids = None
        
        # Pagination variables
        self.n_docs_per_page = 10
        self.n_pages = 0
        self.curr_page = 0
        
        # Initialize commands
        self.set_doc_sel()
        
    def set_doc_sel(self, doc_ids=None):
        '''Changes the list of documents to navigate through.'''
        self.sel_doc_ids = doc_ids
        if doc_ids is None:
            total_docs = len(self.docs)
        else:
            total_docs = len(doc_ids)
        self.n_pages = (total_docs // self.n_docs_per_page) + 1
                
    def doc_range(self, page_num):
        '''Returns a range object indicating the ids of the documents
        specified by the page number.
        '''
        # Find start and end indices specified by page_num
        start_doc_id = self.n_docs_per_page * page_num
        end_doc_id = start_doc_id + self.n_docs_per_page
        
        if self.sel_doc_ids is None:
            total_docs = len(self.docs)
            sel_docs = range(total_docs)
            return list(sel_docs[start_doc_id:end_doc_id])
            
        total_docs = len(self.sel_docs)
        end_doc_id = min(end_doc_id, total_docs)
        if start_doc_id > end_doc_id:
            return []
            
        return self.sel_doc_ids[start_doc_id:end_doc_id]
        
    def render(self, page_num):
        '''Turns the documents into a list of html strings for pages.'''
        page_num = max(0, page_num)
        page_num = min(page_num, self.n_pages)
        self.curr_page = page_num
        
        doc_ids = self.doc_range(page_num)
        
        page = r'<html><table style="width:100%">'
        
        for i in doc_ids:
            doc = self.docs[i]
            highlight( doc )
            
            page += r'<tr style="align:center">'
            page += r'<td></td>'
            #page += r'<td style="text-align:right; vertical-align:top; background-color:blue; width:100%">300</td>'
            page += r'<td style="vertical-align:top; width:50">{:d}</td>'.format(i+1)
            page += doc2tr( doc )
            page += r'<td></td>'
            page += r'</tr>'
        
        page += r'<table></html>'
        return page
        
    def render_first(self):
        return self.render(0)
        
    def render_prev(self):
        return self.render(self.curr_page-1)
        
    def render_next(self):
        return self.render(self.curr_page+1)
        
    def render_last(self):
        return self.render(self.n_pages-1)
        
        