from ..datasets import BGSurveyDataSet


class ThemeCrafterSession:

    def __init__(self):
        pass

    def load_data(self, dataset=None):
        dataset = BGSurveyDataSet()
        self.docs = dataset.X

    def to_html(self):
        html = ''
        for doc in self.docs:
            html += '<div>' + doc + '</div>'
