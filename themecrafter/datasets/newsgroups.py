from sklearn.datasets import fetch_20newsgroups


class NewsGroupsDataSet:

    def __init__(self, n_samples=2000, n_features=1000, n_components=10):
        '''
        Obtains the data set and sets the parameteres
        '''
        # Shape of data
        self.n_samples=2000
        self.n_features=1000
        self.n_components=10

        # Load the 20 newsgroups dataset as raw data.
        self.X = fetch_20newsgroups(shuffle=True, random_state=1,
            remove=('headers', 'footers', 'quotes'))
            
