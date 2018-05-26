import random

import pandas as pd

from ..datasets import BaseDataSet, NewsGroupsDataSet, BGSurveyDataSet, GradReportsDataSet, StudentsReviewDataSet


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
        self.docs = dataset.X
    
    
    def load_csv_data(self, csv_filename, col_id):
        '''Loads the dataset '''
        df = pd.read_csv(csv_filename)
        df[col_id]


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
        html = ''
        for doc in self.docs:
            html += '<div>' + doc + '</div><br>'
        return '<html><body width="100px">' + html + '</body></html>'


    def tokenize(self):
        ''''''
        pass
        
        