#Imports the libary wxPython which is the library used to create the GUI
import wx
#Imports the Ho4_randomizer file we created look in folder for file
from Hoi4_randomizer import *


#Creates a class with the name myFrame using the class wx.Frame which 
#is the class used the open up a window
class myFrame(wx.Frame):

    #Makes the program starts automaticly using the method __init__ taking the 
    #parameters self, parent, id
    def __init__(self, parent, id):
        #Creates a frame with the size 900 high and 800 width and the name Paradox Randomizer
        wx.Frame.__init__(self, parent, id, 'Paradox Randomizer', size=(400,400))

        #Creates the panel inside the frame it's where everything the user is gonna use 
        #for example the button
        panel = wx.Panel(self)

        #Adds an statusbar to GUI
        #Makes a variable called status using wxPythons function CreateStatusBar 
        #which creates an status bar
        status = self.CreateStatusBar()
        
        #Creates a menu bar at the top of the window stored in the variable 
        menubar = wx.MenuBar()
        #Adds a menu to menubar called first and second 
        first = wx.Menu()
        second = wx.Menu()

        #Adds a option in the first menu called new window which has a text in the status bar 
        first.Append(wx.NewId() , "New Window", "This feature will come in a future version" )
        #Adds another option to the first menu with other name but same text
        first.Append(wx.NewId(), "Open...", "This feature will come in a future version" )
        #Tells what the first and second menu is gonna be called which is file and edit
        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        #Does so the menubar actual shows
        self.SetMenuBar(menubar)

        #creates a button in the panel with the name spin the wheel at the position 150 pixels across
        #and 150 pixels down with the height and width of 100 pixels
        button2 = wx.Button(panel, label = "Spin the wheel", pos = (150,150), size = (100,100))
        #Does so the button can be pressed and something happens based on the imagebutton function
        #created further down
        self.Bind(wx.EVT_BUTTON, self.imagebutton, button2)



    
    #Creates a function called closeWindow
    #The function destroys the program using the function Destroy
    def closewindow(self, event):
        self.Destroy()

    #Creates a function called imagebutton
    #The function shows the country on the first click and the flag on the second
    def imagebutton(self, event):
        for random_number in range(10):
            for i in range(2):
                #Creates a variable called png which is using our function from 
                #the other file called countryflag then it checks which type if picture it is
                #and then converts it to bitmap so it can be used in the GUI
                png = wx.Image(country_flag(), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                #Makes a static bitmap using our png variable at the position 160 pixels across and 80 pixels down
                #Then using the width and height of the image
                wx.StaticBitmap(self, -1, png, (160,80), (png.GetWidth(), png.GetHeight()))
                #Creates an text based on the random country we got in Ho4_randomizer
                #Then puts it at the position 165 pixels across and 60 pixels down
                wx.StaticText(self, -1, countries[random_number], (165,60))



#This is black magic
#The whole if  statement starts the program 
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

        #button = wx.Button(panel, label = "exit", pos=(450,350), size=(100,100))
        #self.Bind(wx.EVT_BUTTON, self.closebutton, button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        #Creates a closeButton function
        #The function closes the program
        def closebutton(self, event):
            self.Close(True)
"""