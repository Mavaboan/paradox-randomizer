import wx
from Hoi4_randomizer import *


class myFrame(wx.Frame):

    #Makes the program starts automaticly
    def __init__(self, parent, id):
        #Creates a frame with the size 900 high and 800 width and the name Paradox Randomizer
        wx.Frame.__init__(self, parent, id, 'Paradox Randomizer', size=(400,400))

        #The exit button
        panel = wx.Panel(self)
        #button = wx.Button(panel, label = "exit", pos=(450,350), size=(100,100))
        #self.Bind(wx.EVT_BUTTON, self.closebutton, button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        #Adds an statusbar to GUI
        status = self.CreateStatusBar()
        #Holds the menu File and edit
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        #Adds items to the first menu file
        first.Append(wx.NewId() , "New Window", "This feature will come in a future version" )
        first.Append(wx.NewId(), "Open...", "This feature will come in a future version" )
        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        self.SetMenuBar(menubar)

        button2 = wx.Button(panel, label = "Spin the wheel", pos = (150,150), size = (100,100))
        self.Bind(wx.EVT_BUTTON, self.imagebutton, button2)


    #Creates a closeButton function
    #The function closes the program
    def closebutton(self, event):
        self.Close(True)
    
    #Creates a function called closeWindow
    #The function destroys the program
    def closewindow(self, event):
        self.Destroy()
    #Creates a function called imagebutton
    #The function shows the country on the first click and the flag on the second
    def imagebutton(self, event):
        png = wx.Image(country_flag(), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (160,80), (png.GetWidth(), png.GetHeight()))
        wx.StaticText(self, -1, countries[random_number], (165,60))







#This is black magic
if __name__ =='__main__':
    app = wx.PySimpleApp()
    frame=myFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()




"""
        ==================================== UNUSED STUFF MAY BE NEEDED FOR LATER USE ====================================


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
        wx.StaticText(panel, -1, apples, (50,60))
"""