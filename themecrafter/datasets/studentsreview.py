from . import BaseDataSet
import pandas as pd


class StudentsReviewDataSet(BaseDataSet):

    def __init__(self):
        '''Loads the data set.
        '''
        survey_data = pd.read_csv("M:/data/studentsreviews.csv")
        self.X = survey_data['comment'].tolist()
