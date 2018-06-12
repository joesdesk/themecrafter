import wx
from .gui.mainwindow import MainWindow

from .gui import EVT_DATA_LOAD
from .gui import EVT_INITIALIZE_MODEL

from .nlp.utils import open_tree, tree2string
from .interface.html2 import HTMLTransform
from .interface.topnouns_interface import TopNounsInterface
from .interface.dataload import DataLoadInterface


class Application:

    def __init__(self):
        self.data = None
        self.tree = None
        self.model = None
        self.interface = None
        
        # 
        self.app = wx.App(redirect=False)
        self.window = MainWindow(parent=None, title="Theme Crafter 0.1")
        
            # See https://wiki.wxpython.org/self.Bind%20vs.%20self.button.Bind
        #self.Bind(wx.EVT_MENU, self.data_loaded, main_menubar)
        self.window.Bind(EVT_DATA_LOAD, self.data_loaded)
        self.window.Bind(EVT_INITIALIZE_MODEL, self.init_model)
        
        
    def start(self):
        self.window.Show()
        self.app.MainLoop()
        
    def data_loaded(self, evt):
        data = evt.attr
        
        datainterface = DataLoadInterface(data)
        xmlstring = datainterface.get_xml_string()
        #print(xmlstring)
        # Set Topic View
        #self.top_nouns = TopNounsInterface()
        
        #topics = self.top_nouns.topic_summary()
        #self.topic_list_ctrl.set_data(topics)
        
        # Set HTML
        #tree = open_tree('M:/themecrafter/labelled/NLTKPlain2_topwords.xml')
        #xmlstring = tree2string(tree)
        
        self.html = HTMLTransform(xmlstring)
        self.html.n_per_page = 10
        
        self.html.add_cache()
        
        pages = self.html.cached_pages[None]
        print(pages[0])
        self.window.commentview.set_data(pages)
        #self.window.commentview.commentwindow.LoadPage('themecrafter/interface/test.html')
        
        #for i, topic in enumerate(self.top_nouns.topics):
            #sel_ids = self.top_nouns.topic2docs[i]
            #self.html.add_cache(topic, sel_ids)
        
        
    def init_model(self, evt):
        data = evt.model_params
        print(data)
        print(evt.GetId())
        