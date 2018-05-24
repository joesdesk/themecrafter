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
    
    
    def load_csv_data(self, csv_filename):
        pass
                      
        
    def to_html(self):
        html = ''
        for doc in self.docs:
            html += '<div>' + doc + '</div><br>'
        return '<html><body width="100px">' + html + '</body></html>'
