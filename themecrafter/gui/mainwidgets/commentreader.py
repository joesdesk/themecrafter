import wx
import wx.html

page = """<html><body>

This silly example shows how custom tags can be defined and used in a
wx.HtmlWindow.  We've defined a new tag, &lt;blue&gt; that will change
the <blue id='awef'>foreground color</blue> of the portions of the document that
it encloses to some shade of blue.  The tag handler can also use
parameters specifed in the tag, for example:

<ul>
<li> <blue shade='sky'>Sky Blue</blue>
<li> <blue shade='midnight'>Midnight Blue</blue>
<li> <blue shade='dark'>Dark Blue</blue>
<li> <blue shade='navy'>Navy Blue</blue>
</ul>

</body></html>
"""

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
        print(pp)

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


wx.html.HtmlWinParser_AddTagHandler(BlueTagHandler)



class MyHtmlFrame(wx.html.HtmlWindow):
    def __init__(self, parent, title):
        wx.html.HtmlWindow.__init__(self, parent)

        #self.sizer = wx.BoxSizer()

        #html = wx.html.HtmlWindow(parent)

        #self.sizer.Add(html, flag=wx.EXPAND|wx.ALL)
        #self.SetSizer(self.sizer)

        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            #html.SetStandardFonts()
            self.SetStandardFonts()

        self.update_counts = 0

        #html.SetPage(page)
        #html.SetPage("<html>awefawef</html>")
        self.SetPage(page)

        #self.Bind(wx.html.EVT_HTML_CELL_HOVER, self.hightlight_hover)
        self.Bind(wx.html.EVT_HTML_CELL_CLICKED, self.hightlight_hover)

    def hightlight_hover(self, event):
        cell = event.GetCell()#.GetNext()
        if (cell is not None) and (cell != ''):
            cid = cell.GetId()
            if cid != '':
                print(cid)

        self.update_counts += 1
        print(self.update_counts)

        self.SetPage("""<html> A concordance is more than an index;
        additional material make producing them a labor-intensive process,
        even when assisted by computers, such as commentary, definitions,
        and topical cross-indexing.
        """ +
        str(self.update_counts) +
        "</html>")

        #c = event.GetCell()#.GetParent()
        #print(type(event.GetCell()))
        #self.GetParser().
        #c.SetBackgroundColour("#e7e7e7")
        #print(c.GetBackgroundColour())
        #c.SetLabel("aewf")
        self.Refresh()
        #print(c)

        #c.Draw()


#app = wx.App()
#frm = MyHtmlFrame(None, "Custom HTML Tag Handler")
#frm.Show()
#app.MainLoop()
