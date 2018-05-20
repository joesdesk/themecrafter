from wx import App
from themecrafter.gui.mainwindow import MainWindow
import themecrafter


if __name__=="__main__":
    app = App(redirect=False)
    window = MainWindow(parent=None, title="Theme Crafter 0.1")
    window.Show()
    app.MainLoop()
