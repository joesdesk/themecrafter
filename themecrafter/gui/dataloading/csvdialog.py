# https://wxpython.org/Phoenix/docs/html/wx.Dialog.html
# https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html

import wx
import wx.grid

import pandas as pd

from .events import OnDataLoad, EVT_DATA_LOAD, ID_DATA_LOADED


class CsvDialog(wx.Dialog):
    
    def __init__(self, parent):
        '''Opens a window which allows a user to select data.'''
        wx.Dialog.__init__(self, parent, title='Preview CSV')
            #, size=wx.Size(400, 485))
        
        # Set variables
        self.filename = None
        self.header_line_num = 0
        
        self.header_id = 0
        self.header_label = None
        
        # Select CSV using a file picker
        self.filepicker = wx.FilePickerCtrl(parent=self)
        self.filepicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.sel_filename)
        
        # Create a grid to preview the CSV contents
        self.sheet = wx.grid.Grid(parent=self, size=(400, 150))
        self.sheet.CreateGrid(20, 20)
        
        #self.csv_text = wx.TextCtrl(parent=self, 
        #    style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP,
        #    size=(400, 150))
        #self.csv_text.Disable()
        #self.csv_text.HideNativeCaret()
        # Prevents selection
        #self.csv_text.Bind(wx.EVT_SET_FOCUS, self.doNothing)
        
        # Control to select the line containing the header
        self.num_ctrl = wx.SpinCtrl(parent=self, style=wx.SP_ARROW_KEYS)
        self.num_ctrl.Bind(wx.EVT_SPINCTRL, self.sel_line_num)
        
        # List to show headers on a particular line
        self.header_listctrl = wx.ListCtrl(parent=self, 
            style=wx.LC_SINGLE_SEL|wx.LC_REPORT)
        self.header_listctrl.InsertColumn(0, 'Headers')
        self.header_listctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, 
            handler=self.sel_header)
        
        # Final controls
        ok_btn = wx.Button(self, wx.ID_OK, u"OK")
        cancel_btn = wx.Button(self, wx.ID_CANCEL, u"Cancel")
        #self.confirm_btns = self.CreateButtonSizer(flags=wx.CANCEL|wx.OK)
        self.std_btns = wx.StdDialogButtonSizer()
        self.std_btns.AddButton(ok_btn)
        self.std_btns.AddButton(cancel_btn)
        self.std_btns.Realize()

        ok_btn.Bind(wx.EVT_BUTTON, self.extract_data)
        
        # Size the controls
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        
        # Sizer flag object: see https://wxpython.org/Phoenix/docs/html/wx.SizerFlags.html#wx-sizerflags
        
        sizerflag = wx.SizerFlags()
        sizerflag.Align(alignment = wx.ALIGN_CENTRE_HORIZONTAL)

        sizer.Add(self.filepicker, flag=wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(self.sheet, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        sizer.Add(self.num_ctrl, flags=sizerflag)
        sizer.Add(self.header_listctrl, proportion=0,
            flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL|wx.EXPAND, border=20)
        #sizer.Add(self.confirm_btns, flags=sizerflag)
        
        
        #self.confirm_btns.Layout()
        #self.confirm_btns.Realize()
        
        sizer.Add(self.std_btns, flags=sizerflag)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
    
        # https://stackoverflow.com/questions/21388417/why-isn-t-evt-close-fired-when-i-click-the-ok-or-cancel-buttons-in-a-wx-dialog
        #self.Bind(wx.EVT_CLOSE, self.extract_data)
    
    
    def sel_filename(self, event):
        self.filename = event.GetPath()
        self.preview_headers()
        
    
    def sel_line_num(self, event):
        self.header_line_num = event.GetPosition()
        if self.filename is not None:
            self.preview_headers()


    def sel_header(self, event):
        self.header_id = event.GetIndex()
        self.header_label = event.GetLabel()
            
    
    def set_headerlist(self, headers):
        '''Places the list of strings as items in the control.'''
        self.header_listctrl.DeleteAllItems()
        for i, s in enumerate(headers):
            self.header_listctrl.InsertItem(i, s)
        
    
    def preview_headers(self):
        filename = self.filename
        lnum = self.header_line_num
        
        # Load the data
        with open(filename, encoding='utf-8') as f:
            df = pd.read_csv(f, sep=',', skiprows=lnum,
                nrows=20, na_filter=False,
                skip_blank_lines=False, header=0)
        
        # Use the data frame to populate grid and header list
        headers = list(df.columns.values)
        self.set_headerlist(headers)

    
    def extract_data(self, e):
        filename = self.filename
        lnum = self.header_line_num
        header = self.header_label
        
        # Load the data
        with open(filename, encoding='utf-8') as f:
            df = pd.read_csv(f, sep=',', skiprows=lnum,
                na_filter=False,
                skip_blank_lines=False, header=0)
        
        # except IOError:
            # wx.LogError("Cannot open file '%s'." % newfile)
        
        # Extract the text data
        data = df[header].values.tolist()
        #print("EXTRACT_DATA")
        #self.data = data
        self.EndModal(1)
        
        #e.Skip()
        #return data
        evt = OnDataLoad(attr=data, id=ID_DATA_LOADED)
        wx.PostEvent(self.GetParent(), evt)
        
        
            
    def doNothing(self, event):
        '''Prevents display of caret.'''
        self.csv_text.HideCaret()

        
if __name__=='__main__':
    app = wx.App()
    widget = CsvFieldDialog(parent=None)
    exit_status = widget.ShowModal()
    widget.extract_data()
    
    