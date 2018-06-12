from wx import App
from .gui.mainwindow import MainWindow


class Application:

    def __init__(self):
        self.data = None
        self.tree = None
        self.model = None
        self.interface = None
        
    def start(self):
        app = App(redirect=False)
        window = MainWindow(parent=None, title="Theme Crafter 0.1")
        window.Show()
        app.MainLoop()
        
    def data_loaded(self):
        pass
        
    def tree_loaded(self):
        pass
        
    def model_loaded(self):
        pass
        
    def interface_loaded(self):
        pass