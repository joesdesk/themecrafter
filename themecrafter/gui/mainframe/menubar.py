import wx

from ..dataloading.datamenu import DataMenu
from ..preprocessing.preprocessingmenu import PreprocessingMenu
from ..analyzing.analysismenu import AnalysisMenu


class MenuBar(wx.MenuBar):
    '''Class to hold the top menus (file, edit, etc.)'''

    def __init__(self):
        '''Creates a menubar'''

        # Create a menu bar
        wx.MenuBar.__init__(self)

        # Menu for the application and user files
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program.")
        self.Append(filemenu, "File")

        # Menu for the editing process
        #editmenu = wx.Menu()
        #editmenu.Append(wx.ID_ANY, "Undo")
        #editmenu.Append(wx.ID_ANY, "Redo")
        #self.Append(editmenu, "Edit")
        
        # Menu for data loading
        datamenu = DataMenu(self)
        self.Append(datamenu, "Data")
        
        # Menu for the preprocessing
        preprocessingmenu = PreprocessingMenu(self)
        self.Append(preprocessingmenu, "Preprocessing")

        # Menu for topic modelling
        analysismenu = AnalysisMenu(self)
        self.Append(analysismenu, "Analysis")
        
        