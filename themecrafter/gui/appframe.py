import wx
from .mainframe.mainframe import MainFrame

from .dataloading.datamenu import EVT_DATA_LOAD

from .preprocessing.preprocessingmenu import EVT_XML_LOAD, EVT_SEL_FEAT

from .analyzing.analysismenu import EVT_INIT_MODEL
from .analyzing.analysismenu import ID_TOPWORDS_MODEL, ID_LDA_MODEL

from ..interface.main import MainInterface


class ApplicationFrame(MainFrame):

    def __init__(self):
        MainFrame.__init__(self)
        
        # Setup Interface
        self.interface = MainInterface()
        
        # Bind events to mainwindow
        self.Bind(EVT_DATA_LOAD, self.on_data_load)
        self.Bind(EVT_XML_LOAD, self.on_xml_load)
        self.Bind(EVT_SEL_FEAT, self.on_feat_sel)
        self.Bind(EVT_INIT_MODEL, self.on_init_model)
        
        self.ctrl_topiclist.Bind(wx.EVT_LIST_ITEM_SELECTED, self.topic_sel)
        self.ctrl_topiclist.Bind(wx.EVT_KEY_DOWN, self.show_pos)
        
    def show_pos(self, event):
        keycode = event.GetUnicodeKey()
        tree = self.interface.tree
        for tag in tree.findall('.//tok[@pos="NNS"]'):
            tag.attrib['class'] = str(0)
        
        #xmlstring = self.interface.get_xmlstring()
        
        #self.ctrl_commentview.set_xml(xmlstring)
        #self.ctrl_commentview.highlight_topic(0)
        
    def on_data_load(self, event):
        '''Setup an interface when data is loaded'''
        docs = event.attr
        self.interface.load_docs(docs)
        
        xmlstring = self.interface.get_xmlstring()
        
        self.ctrl_commentview.set_xml(xmlstring)
        
    def on_xml_load(self, event):
        '''Loads the XML into the interface'''
        self.interface.loadxml()
        xmlstring = self.interface.get_xmlstring()
        self.ctrl_commentview.set_xml(xmlstring)
        
    def on_feat_sel(self, event):
        '''Performs a feature selection task.'''
        self.interface.feat_sel()
        xmlstring = self.interface.get_xmlstring()
        
        self.ctrl_commentview.set_xml(xmlstring)
        self.show_topics()
        
    def show_topics(self):
        '''Show topics in the topic list.'''
        df = self.interface.get_topics()
        if df is not None:
            self.set_topics(df)
        
    def on_init_model(self, event):
        ''''''
        id = event.GetId()
        self.interface.do_model()
        
        xmlstring = self.interface.get_xmlstring()
        self.ctrl_commentview.set_xml(xmlstring)
        self.show_topics()
    
    def topic_sel(self, event):
        '''Triggers a display of topics.'''
        idx = event.GetIndex()
        ids = self.interface.show_docs(idx)
        
        self.ctrl_commentview.highlight_topic(idx)
        self.ctrl_commentview.set_doc_sel(ids)
        