import sys


import splash, MainWindow, createform, Author, Info, Email
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
class SplashWindow(QtWidgets.QMainWindow, splash.Ui_SplashScreen):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup(self)
        self.Main = None
        self.Continue.clicked.connect(self.click)
    def click(self):
        self.close()
        information = ["", "","","","","","","","","","",""]
        self.mnWindow = Main(information)
        self.mnWindow.show()
class Main(QtWidgets.QMainWindow, MainWindow.Ui_MainForm):
    def __init__(self, information):
        super().__init__()
        self.setupUi(self, information)
        self.create.triggered.connect(self.click)
        self.user_inf.triggered.connect(self.click_user)
        self.prog_inf.triggered.connect(self.click_program)
        self.sending.triggered.connect(self.click_email)

        #self.add_student.triggered.connect(self.add_student0)
    def click(self):
        self.crWindow = Crform()
        self.crWindow.show()
        self.close()
    def click_user(self):
        self.userwindow = Userinf()
        self.userwindow.show()
    def click_program(self):
        self.progwindow = Proginf()
        self.progwindow.show()

    def click_email(self):
        self.progwindow = Prog_email()
        self.progwindow.show()

class Userinf(QtWidgets.QMainWindow, Author.Ui_Athor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Proginf(QtWidgets.QMainWindow, Info.Ui_Info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Crform(QtWidgets.QMainWindow,createform.Ui_Createform, MainWindow.Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.crWindow = None
        self.ready_button.clicked.connect(self.click)
    def click(self):
        information=[self.Number.toPlainText(), self.date.toPlainText(),
                     self.hour.toPlainText(), self.kurs.toPlainText(),
                     self.group.toPlainText(), self.year.toPlainText(),
                     self.Form.toPlainText(), self.Sem.toPlainText(),
                     self.facultets.toPlainText(), self.spec.toPlainText(),
                     self.Discipline.toPlainText(), self.Teacher.toPlainText(),
                     ]
        #self.textEdit.clear()
        #self.textEdit.insertPlainText("w")
        #self.creating(information)
        self.mnWindow = Main(information)
        self.mnWindow.show()
        self.close()

class Prog_email(QtWidgets.QMainWindow, Email.Ui_Email):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




def main():
    app = QtWidgets.QApplication(sys.argv)
    splashScreen = SplashWindow()
    splashScreen.show()
    QTimer.singleShot(60000, lambda: splashScreen.close())
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
