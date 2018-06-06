#ftp://ftp.ccp4.ac.uk/ccp4/current/unpacked/checkout/wxPython-src-3.0.2.0/wxPython/samples/wxPIA_book/Chapter-16/html_tag.py
# https://wxpython.org/Phoenix/docs/html/wx.html.HtmlWinTagHandler.html#phoenix-title-wx-html-htmlwintaghandler

import wx
import wx.html

class BrTagHandler(wx.html.HtmlWinTagHandler):
    def __init__(self):
        wx.html.HtmlWinTagHandler.__init__(self)
        
    def GetSupportedTags(self):
        return "BR"
    
    def HandleTag(self, tag):
        parser = self.GetParser()
        
        parser.CloseContainer()
        newc = parser.OpenContainer()
        
        #newc.SetWidthFloat(0, wx.html.HTML_UNITS_PIXELS)
        #newc.SetBackgroundColour('#BBBBBB')

        self.ParseInner(tag)
        #print('tag_processed')
        
        newc.CloseContainer()
        newc.OpenContainer()
        
        return True  


class DocumentTagHandler(wx.html.HtmlWinTagHandler):
    def __init__(self):
        wx.html.HtmlWinTagHandler.__init__(self)
        
    def GetSupportedTags(self):
        return "DOC"
    
    def HandleTag(self, tag):
        parser = self.GetParser()
        
        parser.CloseContainer()
        
        newc = parser.OpenContainer()
         
        newc.SetIndent(20, wx.html.HTML_INDENT_BOTTOM)
        
        #newc.SetWidthFloat(100, wx.html.HTML_UNITS_PERCENT)
        #newc.SetBackgroundColour('#BBBBBB')
        
        id = tag.GetParam("ID")
        newc.SetId(id)

        self.ParseInner(tag)
        #print('tag_processed')
        
        parser.CloseContainer()
        parser.OpenContainer()
        
        return True
        
        
class TokenTagHandler(wx.html.HtmlWinTagHandler):
    def __init__(self):
        wx.html.HtmlWinTagHandler.__init__(self)

    def GetSupportedTags(self):
        return "TOK,SENT"

    def HandleTag(self, tag):
        parser = self.GetParser()
        container = parser.GetContainer()
        old = parser.GetActualColor()
        oldbgcolor = wx.Colour(255,255,255)#container.GetBackgroundColour()
        print(oldbgcolor)
        oldfont = parser.CreateCurrentFont()
        
        tagparams = tag.GetAllParams()
        print(tagparams)
        
        oldfontsize = parser.GetFontSize()
        oldfontunderlined = parser.GetFontUnderlined()
        oldfontitalic = parser.GetFontItalic()
        oldfontface = parser.GetFontFace()
        
        #topic = tag.GetParam("topic")
        
        
        newfont = wx.Font(wx.FontInfo().Underlined())
        #oldfont = wx.Font(wx.FontInfo().FaceName(oldfontface))
        
        clr = "#FFFFCC" #"#0000FF"
        if tag.HasParam("style"):
            shade = tag.GetParam("SHADE")
            if shade.upper() == "SKY":
                clr = "#3299CC"
            if shade.upper() == "MIDNIGHT":
                clr = "#2F2F4F"
            elif shade.upper() == "DARK":
                clr = "#00008B"
            elif shade.upper == "NAVY":
                clr = "#23238E"
            
            #container.InsertCell(wx.html.HtmlFontCell(newfont))
            

            #self.GetParser().SetActualColor(clr)
            container.InsertCell(wx.html.HtmlColourCell(clr, wx.html.HTML_CLR_BACKGROUND))
            #parser.GetContainer().InsertCell(wx.html.HtmlFontCell(newfont))

        self.ParseInner(tag)

        if tag.HasParam("style"):
            #self.GetParser().SetActualColor(old)
            container.InsertCell(wx.html.HtmlColourCell(oldbgcolor, wx.html.HTML_CLR_BACKGROUND))
            #container.InsertCell(wx.html.HtmlFontCell(oldfont))
            #print('apply old font')

        return True


class BlueTagHandler(wx.html.HtmlWinTagHandler):
    def __init__(self):
        wx.html.HtmlWinTagHandler.__init__(self)

    def GetSupportedTags(self):
        return "BLUE"

    def HandleTag(self, tag):
        old = self.GetParser().GetActualColor()
        clr = "#0000FF"
        if tag.HasParam("SHADE"):
            shade = tag.GetParam("SHADE")
            if shade.upper() == "SKY":
                clr = "#3299CC"
            if shade.upper() == "MIDNIGHT":
                clr = "#2F2F4F"
            elif shade.upper() == "DARK":
                clr = "#00008B"
            elif shade.upper == "NAVY":
                clr = "#23238E"

        parser = self.GetParser()
        container = parser.GetContainer()

        # Create special tagging cell
        pp = tag.GetAllParams()
        #print(pp)

        # Set Format
        container.InsertCell(wx.html.HtmlColourCell('#23238E', wx.html.HTML_CLR_BACKGROUND))
        container.InsertCell(wx.html.HtmlColourCell('#FFFFFF', wx.html.HTML_CLR_FOREGROUND))

        #parser.SetContainer(newcell)
        #container = parser.GetContainer()
        #container.SetWidthFloat(50, wx.html.HTML_UNITS_PIXELS)

        # Parsing the inner tag breaks up words which prevents knowing
        # What id of earlier words were in the inner string.
        #self.ParseInner(tag)

        source = parser.GetSource()
        source_start = tag.GetBeginPos()
        source_stop = tag.GetEndPos1()
        inner_source = source[source_start:source_stop]
        #print(inner_source)

        new_cell = wx.html.HtmlWordCell(inner_source, parser.GetDC())
        new_cell.SetId(pp)
        container.InsertCell(new_cell)

        container.InsertCell(wx.html.HtmlColourCell('#FFFFFF', wx.html.HTML_CLR_BACKGROUND))
        container.InsertCell(wx.html.HtmlColourCell('#000000', wx.html.HTML_CLR_FOREGROUND))

        #parser.CloseContainer()
        #parser.CloseContainer()
        #parser.OpenContainer()
        #self.GetParser().SetActualColor(old)
        #self.GetParser().GetContainer().InsertCell(wx.html.HtmlColourCell(old))

        return True
        
        