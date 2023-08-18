from uiassisgui import Ui_assistant_gui
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer,QTime,QDate  #for showing time date in my gui
import sys
from urllib.request import urlopen
import json


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        import maincode
        #maincode.Task_Gui()
        while True:
          maincode.Task_Gui()


startExe= MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui= Ui_assistant_gui()
        self.gui.setupUi(self)

        self.gui.Button_1.clicked.connect(self.startTask)
        self.gui.button_2.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1= QtGui.QMovie("jarves_gui//live.gif")
        self.gui.bg_2.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2= QtGui.QMovie("jarves_gui//loading_1.gif")
        self.gui.bg_3.setMovie(self.gui.label2)
        self.gui.label2.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.timeout.connect(self.location)
        timer.start(999)
        startExe.start()

    def showTimeLive(self):
        time1=QTime.currentTime()
        time=time1.toString()
        date1=QDate.currentDate()
        date=date1.toString()
        label_time= "Time:"+time
        label_date= "Date:"+date
      
    

        self.gui.text_2.setText(label_time)
        self.gui.text1.setText(label_date)
        #self.gui.text_3.setText(label_day)

    def location(self):
        url='http://ipinfo.io/json'
        geo_q=urlopen(url)
        geo_d = json.load(geo_q)
        state=geo_d['city']
        country=geo_d['country']
        label_location= "Location: "+ state +' , '+ country
        self.gui.text_3.setText(label_location)



GuiApp= QApplication(sys.argv)
uiassis_gui = Gui_Start()
uiassis_gui.show()
exit(GuiApp.exec_())


