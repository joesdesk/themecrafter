from .mainframe.mainframe import MainFrame

from .dataloading.datamenu import EVT_DATA_LOAD

from .preprocessing.preprocessingmenu import EVT_XML_LOAD

from .commentview.navbar import EVT_PAGE_CHANGE
from .commentview.navbar import ID_FIRST, ID_PREV, ID_NEXT, ID_LAST

from ..interface.main import MainInterface


class ApplicationFrame(MainFrame):

    def __init__(self):
        MainFrame.__init__(self)
        
        # Setup Interface
        self.interface = MainInterface()
        
        # Bind events to mainwindow
        self.Bind(EVT_DATA_LOAD, self.on_data_load)
        self.Bind(EVT_XML_LOAD, self.on_xml_load)
        self.Bind(EVT_PAGE_CHANGE, self.on_page_change)
        
        
    def on_data_load(self, event):
        '''Setup an interface when data is loaded'''
        docs = event.attr
        self.interface.load_docs(docs)
        
        htmlstring = self.interface.html.render_first()
        self.html_update(htmlstring)
        
        self.show_topics()
        
    def on_xml_load(self, event):
        '''Loads the XML into the interface'''
        self.interface.loadxml()
        htmlstring = self.interface.html.render_first()
        self.html_update(htmlstring)
        
    def html_update(self, htmlstring):
        '''Set the page and page number of the commentview.'''
        self.set_html(htmlstring)
        pagenum = self.interface.html.curr_page
        totalpages = self.interface.html.n_pages
        self.ctrl_commentview.pagenav.set_page(pagenum+1, totalpages)
        
    def show_topics(self):
        '''Show topics in the topic list.'''
        df = self.interface.get_topics()
        self.set_topics(df)
        
    def on_page_change(self, evt):
        '''Changes the html text in the commentview.'''
        id = evt.GetId()
        
        if id==ID_FIRST:
            htmlstring = self.interface.html.render_first()
        elif id==ID_PREV:
            htmlstring = self.interface.html.render_prev()
        elif id==ID_NEXT:
            htmlstring = self.interface.html.render_next()
        elif id==ID_LAST:
            htmlstring = self.interface.html.render_last()
        else:
            return None
        
        self.html_update(htmlstring)
        
        