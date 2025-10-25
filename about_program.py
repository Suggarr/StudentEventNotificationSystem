from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info): # Создание окна
        Info.setObjectName("Info")
        Info.resize(1057, 665)
        Info.setMinimumSize(QtCore.QSize(1057, 665))
        Info.setMaximumSize(QtCore.QSize(1057, 665))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/mail_ikonka2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Info.setWindowIcon(icon)
        Info.setStyleSheet("*{\n"
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
        self.pushButton = QtWidgets.QPushButton(Info)
        self.pushButton.setGeometry(QtCore.QRect(630, 560, 351, 61))
        self.pushButton.setStyleSheet("")
        self.pushButton.clicked.connect(Info.close)  # Закрытие текущего окна
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(Info)
        self.label_7.setGeometry(QtCore.QRect(150, 60, 681, 111))
        self.label_7.setStyleSheet("QTextEdit{ height: 100%; }")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Info)
        self.label.setGeometry(QtCore.QRect(40, 180, 401, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/mail_program.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Info)
        self.label_2.setGeometry(QtCore.QRect(40, 560, 401, 61))
        self.label_2.setStyleSheet("border: 2px solid black;\n"
"background-color: white;\n"
"color: black;\n"
"font-size: 21px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Info)
        self.label_3.setGeometry(QtCore.QRect(500, 160, 531, 301))
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info): # Дизайн окна
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "О программе"))
        self.pushButton.setText(_translate("Info", "Назад"))
        self.label_7.setText(_translate("Info", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Информирование студентов о проходящих </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">мероприятиях</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("Info", "<html><head/><body><p align=\"center\"><span style=\" font-size:13pt;\">Версия ver. 1.0.0.2023</span></p></body></html>"))
        self.label_3.setText(_translate("Info", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Данное приложение имеет следующий возможности: </span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">1) Открывать и сохранять таблицу Excel</span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">2) Удалять пользователей по идентификатору(id)</span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">3) Отправлять email студентам, которые занесены </span></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">в таблицу</span></p><p><span style=\" font-size:11pt; font-weight:600;\">4) Проверка интернета при отправке email</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Info = QtWidgets.QDialog()
    ui = Ui_Info()
    ui.setupUi(Info)
    Info.show()
    sys.exit(app.exec_())
