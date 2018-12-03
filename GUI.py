import wx

class myFrame(wx.Frame):

    #Makes the program starts automaticly
    def __init__(self, parent, id):
        #Creates a frame with the size 900 high and 800 width and the name Paradox Randomizer
        wx.Frame.__init__(self, parent, id, 'Paradox Randomizer', size=(900,800))

        #The exit button
        panel = wx.Panel(self)
        button = wx.Button(panel, label = "exit", pos=(130,60), size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.closebutton, button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        #Adds an statusbar tp GUI
        status = self.CreateStatusBar()
        #Holds the menu File and edit
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        #Adds items to the first menu file
        first.Append(wx.NewId() , "New Window", "This is a new window" )
        first.Append(wx.NewId(), "Open...", "This will open a new window" )
        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        self.SetMenuBar(menubar)

        #Creates a static text that is 10 pixels down and 10 pixels across
        wx.StaticText(panel, -1, "This i static text", (10,10))

        #Makes a variable called custom and creates a text which is 10 down 
        #and 30 across and has colour 260 pixels across and is aligned left
        custom = wx.StaticText(panel, -1, "this is custom", (10,30), (260,-1), wx.ALIGN_CENTER)
        #Sets the custom variabel to have a text colour of white
        custom.SetForegroundColour('white')
        #Sets the custom variable to have the bakcgroundcolour to blue t
        #This is where the 260 in the custom variable comes in
        custom.SetBackgroundColour('blue')

        panel = wx.Panel(self)
        #User prompt that let's the user enter something
        test = wx.TextEntryDialog(None, "Whats your name", "Title", "Enter name")
        #if they clicked ok the data gets stored in apples
        if test.ShowModal() == wx.ID_OK:
            apples = test.GetValue()
        #text panel which shows the data from apples
        wx.StaticText(panel, -1, apples, (10,60))

    #Creates a closeButton function
    #The function closes the program
    def closebutton(self, event):
        self.Close(True)
    
    #Creates a function called closeWindow
    #The function destroys the program
    def closewindow(self, event):
        self.Destroy()








#This is black magic
if __name__ =='__main__':
    app = wx.PySimpleApp()
    frame=myFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
