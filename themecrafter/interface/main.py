from ..nlp.utils import open_tree, show_tree, save_tree, tree2string

from pandas import DataFrame
from .html import HTMLInterface

class MainInterface:
    '''Container for all objects of interation for the GUI.'''
    
    def __init__(self, data):
        '''Interface must be started with data.'''
        self.data = data
        
        # Sub-interfaces
        self.html = None
        
        # Initial commands
        self.loadxml()
        
    def show_data(self):
        '''Quickly parses the data into XML format for viewing'''
        pass
        
    def loadxml(self):
        self.tree = open_tree("M:/themecrafter/parsed/NLTKPlain2_NEW.xml")
        #tree = open_tree('M:/themecrafter/results/NLTKPlain2_topwords.xml')
        xmlstring = tree2string(self.tree)
        self.html = HTMLInterface(xmlstring)
    
    def sel_feat(self):
        pass
    
    def add_model(self):
        model = None
        
    def get_topics(self):
        df = DataFrame([("topic1",30)], columns=['topic','weight'])
        return df
        
    def get_html(self):
        htmlstring = self.html.render(0)
        return htmlstring