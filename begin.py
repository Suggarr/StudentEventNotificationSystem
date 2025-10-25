import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

import splash_screen
import MainWindow
import about_author
import about_program

class SplashWindow(QtWidgets.QMainWindow, splash_screen.Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Main = None
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.close()
        self.mnWindow = Main()
        self.mnWindow.show()

class Main(QtWidgets.QMainWindow, MainWindow.Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_inf.triggered.connect(self.click_user)
        self.prog_inf.triggered.connect(self.click_program)

    def click_user(self):
        self.userwindow = Userinf()
        self.userwindow.show()

    def click_program(self):
        self.progwindow = Proginf()
        self.progwindow.show()


class Userinf(QtWidgets.QMainWindow, about_author.Ui_Author):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Proginf(QtWidgets.QMainWindow, about_program.Ui_Info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    splashScreen = SplashWindow()
    # splashScreen.setWindowFlag(Qt.FramelessWindowHint)
    splashScreen.show()
    QTimer.singleShot(60000, lambda: splashScreen.close())
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
