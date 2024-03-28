from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Author(object):
    def setupUi(self, Author): # Создание окна
        Author.setObjectName("Author")
        Author.resize(529, 758)
        Author.setMinimumSize(QtCore.QSize(529, 758))
        Author.setMaximumSize(QtCore.QSize(529, 758))
        Author.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/mail_ikonka2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Author.setWindowIcon(icon)
        Author.setAutoFillBackground(False)
        Author.setStyleSheet("*{\n"
"    color: #FFF;\n"
"    background-color: rgb(68, 136, 204);\n"
"}\n"
"QPushButton\n"
"{\n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 58, 176);\n"
"    border-radius: 10px;                   \n"
"    border: 2px solid #094065;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 0, 0);\n"
"    background-color: rgb(0, 158, 176);\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FF0000;\n"
"}\n"
"QPushButton::released\n"
"{\n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 58, 176);\n"
"    border-radius: 10px;\n"
"    border: 2px solid #094065;\n"
"}")
        self.label = QtWidgets.QLabel(Author)
        self.label.setGeometry(QtCore.QRect(90, 20, 351, 441))
        self.label.setMinimumSize(QtCore.QSize(250, 410))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/Me1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Author)
        self.pushButton.setGeometry(QtCore.QRect(90, 660, 351, 61))
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(False)
        self.pushButton.clicked.connect(Author.close)  # Закрытие текущего окна
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Author)
        self.label_3.setGeometry(QtCore.QRect(50, 480, 431, 141))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Author)
        QtCore.QMetaObject.connectSlotsByName(Author)

    def retranslateUi(self, Author): # Дизайн окна
        _translate = QtCore.QCoreApplication.translate
        Author.setWindowTitle(_translate("Author", "Об авторе"))
        self.pushButton.setText(_translate("Author", "Назад"))
        self.label_3.setText(_translate("Author", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Автор</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Студент группы 10701322</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Сахаревич Илья Николаевич</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">saharevich2004@gmail.com</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Author = QtWidgets.QDialog()
    ui = Ui_Author()
    ui.setupUi(Author)
    Author.show()
    sys.exit(app.exec_())
