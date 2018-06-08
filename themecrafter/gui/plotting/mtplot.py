import numpy as np
from numpy import arange, sin, pi

# https://matplotlib.org/gallery/user_interfaces/embedding_in_wx4_sgskip.html
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

# https://matplotlib.org/users/customizing.html
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Arial']

# https://eli.thegreenplace.net/2008/08/01/matplotlib-with-wxpython-guis/
# http://physicalmodelingwithpython.blogspot.com/

import wx


class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        
        self.Fit()
        
    def show(self):
        '''Must be called to display update.'''
        # https://stackoverflow.com/questions/27878217/pyplot-extend-margin-at-the-bottom-of-a-figure
        self.figure.tight_layout()
        
        #https://stackoverflow.com/questions/10755937/how-to-redraw-a-mathplotlib-figure-in-a-wxpython-panel
        self.canvas.draw()
        self.canvas.Refresh()
        

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        
        # https://matplotlib.org/api/axes_api.html#axes-class
        self.axes.plot(t, s)
        self.show()
        
    def bar(self, xlabels, yheights):
        
        ind = np.arange(len(xlabels))
        self.axes.clear()
        self.axes.bar(ind, yheights, width=0.35)

        self.axes.set_xticks(ind, minor=False)
        self.axes.set_xticklabels(xlabels, fontdict=None, \
            minor=False, rotation=90)
        self.show()

if __name__ == "__main__":
    app = wx.App()
    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()