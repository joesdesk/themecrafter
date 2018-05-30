from .base_session import BaseSession

from ..datasets import BaseDataSet, NewsGroupsDataSet, BGSurveyDataSet, GradReportsDataSet, StudentsReviewDataSet

import pandas as pd


class LoadDataSession:

    def __init__(self):
        BaseSession.__init__(self)
        
        
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
    
    
    def load_csv_data(self, filename, headerloc, col):
        '''Loads documents from a column of a csv.'''
        series = pd.read_csv(filename, sep=',', header=headerloc, \
            usecols=[col], squeeze=True)
        self.docs = series.tolist()
        
        