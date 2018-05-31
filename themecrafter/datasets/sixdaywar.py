from . import BaseDataSet


class SixDayWarDataSet(BaseDataSet):

    def __init__(self):
        ''''''
        f = open('themecrafter/datasets/sixdaywar/test.txt')
        data = [line.rstrip('\n') for line in f]
        
        self.X = data
