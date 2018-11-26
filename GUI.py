import wx

class myFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Paradox Randomizer', size=(300,200))

        #The exit button
        panel=wx.Panel(self)
        button=wx.Button(panel, label="exit",pos=(130,10),size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.closebutton, button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        #Adds an statusbar tp GUI
        status = self.CreateStatusBar()
        #Holds the menu File and edit
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        #Adds items to the first menu file
        first.Append(wx.NewId(), "New Window", "This is a new window" )
        first.Append(wx.NewId(), "Open...", "This will open a new window" )
        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        self.SetMenuBar(menubar)


    def closebutton(self,event):
        self.Close(True)
    
    def closewindow(self, event):
        self.Destroy()


#This is black magic
if __name__ =='__main__':
    app = wx.PySimpleApp()
    frame=myFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
