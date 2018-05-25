# https://wxpython.org/Phoenix/docs/html/wx.Dialog.html
# https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html

import wx

import pandas as pd

class CsvDialog(wx.FileDialog):
    
    def __init__(self, parent):
        '''Opens a file dialog to select a csv file.'''
        wx.FileDialog.__init__(self, parent, message="Open CSV file", 
            wildcard="CSV files (*.csv)|*.csv", 
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

            
class CsvFieldDialog(wx.Dialog):
    
    def __init__(self, parent):
        '''Opens a window which allows a user to select data.'''
        wx.Dialog.__init__(self, parent)#, size=wx.Size(400, 485))
        
        # Preview the text of the csv
        self.csv_text = wx.TextCtrl(parent=self, 
            style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP,
            size=(400, 150))
        #self.csv_text.Disable()
        #self.csv_text.HideNativeCaret()
        
        # Prevents selection
        #self.csv_text.Bind(wx.EVT_SET_FOCUS, self.doNothing)
        
        # Control to select the line containing the header
        self.header_line = wx.SpinCtrl(parent=self, style=wx.SP_ARROW_KEYS)
        
        #
        self.headers_list = wx.ListCtrl(parent=self, 
            style=wx.LC_SINGLE_SEL|wx.LC_REPORT)
        #self.Bind(wx.EVT_SPINCTRL, , self.headers_list)
        
        # Final controls
        self.confirm_btns = self.CreateButtonSizer(flags=wx.CANCEL|wx.OK)
        
        # Size the controls
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        
        # Sizer flag object: see https://wxpython.org/Phoenix/docs/html/wx.SizerFlags.html#wx-sizerflags
        
        sizerflag = wx.SizerFlags()
        sizerflag.Align(alignment = wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(self.csv_text, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        sizer.Add(self.header_line, flags=sizerflag)
        sizer.Add(self.headers_list, proportion=0, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=20)
        #sizer.Add(self.confirm_btns, flags=sizerflag)
        
        
        #self.confirm_btns.Layout()
        #self.confirm_btns.Realize()
        
        sizer.Add(self.confirm_btns, flags=sizerflag)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
    
    def open_file(self, filename):
        with open(filename, encoding='utf-8') as f:
            i = 0
            for l in f:
                if i < 10:
                    self.csv_text.write(l)
                    i += 1
                else:
                    break
                    
    
    def doNothing(self, event):
        '''Prevents display of caret.'''
        self.csv_text.HideCaret()