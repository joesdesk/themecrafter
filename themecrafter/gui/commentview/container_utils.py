import wx
import wx.html
# Functions to diagnose the structure of parsed containers

def list_children(container, lvl):
    '''Identifies the first child of the container. If none can be found,
    iterate through the next containers until none can be found.'''
    
    #print(lvl)
    next_container = container.GetFirstChild()
    while next_container is not None:
        
        if type(next_container)==wx.html.HtmlContainerCell:
            next_container.SetBackgroundColour("#BBBBBB")
            next_container.SetWidthFloat(20, wx.html.HTML_UNITS_PIXELS)
            id = next_container.GetId()
            #print(id)
            
            #next_container.SetBorder("#BBBBBB", "#BBBBBB", 2)
        
        list_children(next_container, lvl+1)
        next_container = next_container.GetNext()
        
            
def parse(container, lvl=0):
    '''Diagnostic tool to probe the results of parsing HTML.'''
    if container is None:
    #   print('    '*lvl + 'None')
    #elif lvl>=2:
        pass
    else:
        if str(type(container))==r"<class 'wx._html.HtmlContainerCell'>":
            bgcolor = container.GetBackgroundColour()
            halign = container.GetAlignHor()
            valign = container.GetAlignVer()
            width = container.GetWidth()
            print('    '*lvl + str(bgcolor) + ',' + str(halign) + ',' + str(valign) + ',' + str(width) )
        elif str(type(container))==r"<class 'wx._html.HtmlWordCell'>":
            #textrep = container.word
            print('    '*lvl + str('HTML_WORD_CELL') )
        else:
            print('    '*lvl + str(type(container)) )
        
        parse(container.GetFirstChild(), lvl+1)
        parse(container.GetNext(), lvl)