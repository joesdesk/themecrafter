from . import BaseDataSet
from sklearn.datasets import fetch_20newsgroups


class NewsGroupsDataSet(BaseDataSet):

    def __init__(self, n_samples=2000, n_features=1000, n_components=10):
        '''Loads the data set according to some parameters
        '''
        # Shape of data
        self.n_samples=2000
        self.n_features=1000
        self.n_components=10

        # Load the 20 newsgroups dataset as raw data.
        newsgroups = fetch_20newsgroups(shuffle=True, random_state=1,
            remove=('headers', 'footers', 'quotes'))
        self.X = newsgroups['data']
