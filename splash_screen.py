from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen): # Создание окна
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(922, 707)
        SplashScreen.setMinimumSize(QtCore.QSize(922, 707))
        SplashScreen.setMaximumSize(QtCore.QSize(922, 707))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/mail_ikonka2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        SplashScreen.setStyleSheet("*{\n"
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
        self.label = QtWidgets.QLabel(SplashScreen)
        self.label.setGeometry(QtCore.QRect(130, 20, 601, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SplashScreen)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 651, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SplashScreen)
        self.label_3.setGeometry(QtCore.QRect(240, 180, 421, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SplashScreen)
        self.label_4.setGeometry(QtCore.QRect(80, 70, 731, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(SplashScreen)
        self.label_5.setGeometry(QtCore.QRect(220, 230, 161, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SplashScreen)
        self.label_6.setGeometry(QtCore.QRect(410, 230, 291, 31))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(SplashScreen)
        self.label_9.setGeometry(QtCore.QRect(540, 390, 301, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(SplashScreen)
        self.label_10.setGeometry(QtCore.QRect(540, 410, 261, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(SplashScreen)
        self.label_11.setGeometry(QtCore.QRect(540, 460, 261, 51))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(SplashScreen)
        self.label_12.setGeometry(QtCore.QRect(110, 350, 241, 201))
        self.label_12.setStyleSheet("QWidget { padding: 3px }")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("resources/mail_ikonka2.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(SplashScreen)
        self.label_13.setGeometry(QtCore.QRect(410, 570, 101, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(SplashScreen)
        self.pushButton.setGeometry(QtCore.QRect(60, 620, 351, 61))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SplashScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 620, 351, 61))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(SplashScreen)
        self.label_7.setGeometry(QtCore.QRect(130, 270, 681, 91))
        self.label_7.setStyleSheet("QTextEdit{ height: 100%; }")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen): # Дизайн окна
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "Информирование студентов"))
        self.label.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Белорусский Национальный Технический Университет<br/></span></p></body></html>"))
        self.label_2.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Факультет информационных технологий и робототехники</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Курсовая работа</span></p></body></html>"))
        self.label_4.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Кафедра программного обеспечения информационных систем и робототехники</span></p></body></html>"))
        self.label_5.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">по дисциплине </span></p></body></html>"))
        self.label_6.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:14pt;\">Языки программирования</span></p></body></html>"))
        self.label_9.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Выполнил: Студент группы 10701322</span></p></body></html>"))
        self.label_10.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Сахаревич Илья Николаевич</span></p></body></html>"))
        self.label_11.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Преподаватель: к.ф.-м.н., доц.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">Сидорик Валерий Владимирович</span></p></body></html>"))
        self.label_13.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Минск, 2023</span></p></body></html>"))
        self.pushButton.setText(_translate("SplashScreen", "Далее"))
        self.pushButton_2.setText(_translate("SplashScreen", "Выход"))
        self.label_7.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Информирование студентов о проходящих </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">мероприятиях</span></p><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QDialog()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
