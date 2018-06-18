from .mainframe.mainframe import MainFrame
from .dataloading.datamenu import EVT_DATA_LOAD

from ..interface.main import MainInterface


class ApplicationFrame(MainFrame):

    def __init__(self):
        MainFrame.__init__(self)
        
        # Setup Interface
        self.interface = MainInterface()
        
        self.Bind(EVT_DATA_LOAD, self.on_data_load)
        
    def on_data_load(self, event):
        df = self.interface.get_topics()
        self.set_topics(df)
        
        
        
    def show_html(self, page):
        htmlstring = self.interface.get_html()
        self.set_html(htmlstring)
        
        