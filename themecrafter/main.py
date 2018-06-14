import wx
from .gui.mainwindow import MainWindow

from .gui import EVT_DATA_LOAD, EVT_XML_LOAD, EVT_INIT_MODEL

from .nlp.utils import open_tree, tree2string
from .interface.html2 import HTMLTransform
from .models.topwords import TopWordsInterface
from .interface.dataload import DataLoadInterface


class Application:

    def __init__(self):
        self.data = None
        self.xml = None
        self.interface = None
        
        # 
        self.app = wx.App(redirect=False)
        self.window = MainWindow(parent=None, title="Theme Crafter 0.1")
        
            # See https://wiki.wxpython.org/self.Bind%20vs.%20self.button.Bind
        #self.Bind(wx.EVT_MENU, self.data_loaded, main_menubar)
        self.window.Bind(EVT_DATA_LOAD, self.data_loaded)
        self.window.Bind(EVT_INIT_MODEL, self.init_model)
        self.window.topic_list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.sel_topic)
        
    def start(self):
        self.window.Show()
        self.app.MainLoop()
        
    def show_xml(self, xmlstring):
        '''Given an XML result from a process, display it.'''
        # HTML parser
        self.html = HTMLTransform(xmlstring)
        self.html.n_per_page = 10
        self.html.add_cache()
        
        ## Obtain the pages and apply them
        pages = self.html.cached_pages[None]
        self.window.commentview.set_data(pages)
        
    def data_loaded(self, evt):
        data = evt.attr
        
        self.data = data
        datainterface = DataLoadInterface(data)
        xmlstring = datainterface.get_xml_string()
        self.show_xml(xmlstring)
        
    def tree_loaded(self, evt):
        filename = "M:/themecrafter/parsed/NLTKPlain2_NEW.xml"
        tree = open_tree(filename)
        self.xml = tree
        #xmlstring = tree2string(tree)
        #self.show_xml(xmlstring)
        
    def init_model(self, evt):
        data = evt.model_params
        print(data)
        print(evt.GetId())
        
        self.tree_loaded(None)
        #print(xmlstring)
        # Set Topic View
        
        from .preprocessing.labeltransform import LabelTransform
        transform = LabelTransform()
        transform.fit(self.xml)
        
        top_nouns = TopWordsInterface(self.xml)
        top_nouns.tag_xml_tokens()
        top_nouns.tag_xml_sents()
        top_nouns.test_get_doc_topic_bow()
        
        xmlstring = top_nouns.get_xml_string()
        #print(xmlstring)
        
        self.show_xml(xmlstring)
        
        topics = top_nouns.topic_counts()
        self.window.topic_list_ctrl.set_data(topics)
        
        # Set HTML
        # self.window.commentview.commentwindow.LoadPage('themecrafter/interface/test.html')
        
        for i, topic in enumerate(top_nouns.model.get_topics()):
            #print(i)
            sel_ids = top_nouns.get_docs(i)
            #print(sel_ids)
            self.html.add_cache(str(i), sel_ids)

    def sel_topic(self, event):
        '''Handles the selection of a topic.'''
        
        # Obtain the topic index
        index = event.GetIndex()
        
        # Get the topic name
        #topic = self.top_nouns.topics[index]
        
        # Get html pages from cache
        if self.html is not None:
            pages = self.html.cached_pages[str(index)]
            self.window.commentview.set_data(pages)
            
        # Obtain the concurrence of the topic
        #concr = self.top_nouns.topic_concurrence[index]
        
        #self.plot.bar(self.top_nouns.topics, concr)

        
        