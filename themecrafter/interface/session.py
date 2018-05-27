import random

import pandas as pd

from ..datasets import BaseDataSet, NewsGroupsDataSet, BGSurveyDataSet, GradReportsDataSet, StudentsReviewDataSet

from .prettifier import ToHTML


class ThemeCrafterSession:

    def __init__(self):
        pass


    def load_preset_data(self, data=None):
        '''Loads preset data according to name.'''
        if data=='NewsGroups':
            dataset = NewsGroupsDataSet()
        elif data=='BGSurvey':
            dataset = BGSurveyDataSet()
        elif data=='GradReports':
            dataset = GradReportsDataSet()
        elif data=='StudentsReview':
            dataset = StudentsReviewDataSet()
        else:
            dataset = BaseDataSet()
        self.load_data(dataset.X)
        
    
    def load_data(self, data=None):
        '''Loads a list of strings as documents.'''
        self.docs = data


    def read_doc(self, id=None):
        '''Reads a document for a given id.
        If no id is given, reads a document at random.'''
        
        n_docs = len(self.docs)
        
        if id is None:
            id = random.randrange(n_docs)
        
        doc = self.docs[id]
        
        print("doc id:", id)
        print("")
        print(doc)
        print("")
        
    
    def to_html(self):
        html_text = ToHTML(self.docs)
        return html_text
    
    
    def to_html_text(self, file):
        #html = ''
        #for doc in self.docs:
        #    html += '<div style="width: 100px; color: red">' + doc + '</div><br>'
        #return '<html><body>' + html + '</body></html>'
        html_text = self.to_html()
        f = open(file, 'w+')
        f.write(html_text)
        f.close()
        
        
    def tokenize(self):
        ''''''
        pass
        
        