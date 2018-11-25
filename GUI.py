import wx

class myFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Paradox Randomizer', size=(300,200))

if __name__ =='__main__':
    app = wx.PySimpleApp()
    frame=myFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
