import arcpy
import pythonaddins

class ButtonClass1(object):
    """Implementation for Baru_Addin_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        message = pythonaddins.MessageBox("Click Event...","Title for MessageBox",1)
        if(message =="OK"):
            print"Do someting"
        elif(message =="Cancel"):
            print"User wants to cancel"
