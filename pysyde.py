"""
import sys
from PySide import QtGui
app = QtGui.QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Simple')
wid.show()
sys.exit(app.exec_())
"""
"""
from PySide import QtGui  
from PySide import QtCore
from PySide import QtUiTools

class MyWidget(QtGui.QMainWindow):
    def __init__(self, *args):  
       apply(QtGui.QMainWindow.__init__, (self,) + args)

       loader = QtUiTools.QUiLoader()
       file = QtCore.QFile("test2.ui")
       file.open(QtCore.QFile.ReadOnly)
       self.myWidget = loader.load(file, self)
       file.close()
       self.setCentralWidget(self.myWidget)
if __name__ == '__main__':  
   import sys  
   import os
   print("Running in " + os.getcwd() + " .\n")

   app = QtGui.QApplication(sys.argv)  
   app.aboutToQuit.connect(app.deleteLater)

   win  = MyWidget()  
   win.show()
   app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
               app, QtCore.SLOT("quit()"))
   app.exec_()
   """
import sys
from PySide import QtCore, QtGui
from test import Ui_MainWindow

class MyMainWindow(QtGui.QMainWindow):
    count=0
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.nhannut)
    def nhannut(self):
        MyMainWindow.count=MyMainWindow.count+1
        self.ui.label.setText(str(MyMainWindow.count))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    myapp = MyMainWindow()
    myapp.show()
    sys.exit(app.exec_())
   