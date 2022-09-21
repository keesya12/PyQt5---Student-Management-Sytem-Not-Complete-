from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from facultyDash import *


class Ui_main_Screen(object):


    def facultyDash(self):
        self.facultyDashboard = QtWidgets.QMainWindow()
        self.ui = Ui_facultyDashboard()
        self.ui.setupUi(self.facultyDashboard)
        self.facultyDashboard.show()

    def setupUi(self, main_Screen):
        main_Screen.setObjectName("main_Screen")
        main_Screen.resize(950, 650)
        main_Screen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.216, x2:1, y2:0, stop:0.267045 rgba(133, 221, 203, 255), stop:1 rgba(75, 103, 118, 255));")
        main_Screen.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(main_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(150, 240, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0;")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 180, 121, 31))
        self.label_3.setStyleSheet("font: 63 22pt \"Verdana\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 280, 300, 20))
        self.line.setStyleSheet("\n"
"background-color: none;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(150, 320, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 0;")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(150, 360, 300, 20))
        self.line_2.setStyleSheet("\n"
"background-color: none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.signin_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.signin_pushButton.setGeometry(QtCore.QRect(190, 440, 211, 51))
        self.signin_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signin_pushButton.setAutoFillBackground(False)
        self.signin_pushButton.clicked.connect(self.btn_login_handler)
        self.signin_pushButton.setStyleSheet("color: rgb(0,0,0);\n"
"font: 63 14pt \"Verdana\";\n"
"border-radius: 15px;\n"
"background-color: rgb(75, 103, 118,150);")
        self.signin_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.signin_pushButton.setObjectName("signin_pushButton")
        self.design = QtWidgets.QLabel(self.centralwidget)
        self.design.setGeometry(QtCore.QRect(490, 150, 431, 331))
        self.design.setStyleSheet("background-color: none;")
        self.design.setText("")
        self.design.setPixmap(QtGui.QPixmap("welcome_screen logo.png"))
        self.design.setScaledContents(True)
        self.design.setObjectName("design")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 290, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 75 72pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_5.setObjectName("label_5")
        main_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_Screen)
        QtCore.QMetaObject.connectSlotsByName(main_Screen)

    def retranslateUi(self, main_Screen):
        _translate = QtCore.QCoreApplication.translate
        main_Screen.setWindowTitle(_translate("main_Screen", "Main Screen"))
        self.username_lineEdit.setPlaceholderText(_translate("main_Screen", "Username"))
        self.label_3.setText(_translate("main_Screen", "SIGN IN"))
        self.password_lineEdit.setPlaceholderText(_translate("main_Screen", "Password"))
        self.signin_pushButton.setText(_translate("main_Screen", "LOG IN"))
        self.signin_pushButton.clicked.connect(main_Screen.close)
        self.label_5.setText(_translate("main_Screen", "C U B I X "))



    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.NoIcon)
        msg.setText('{}'.format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()

    def btn_login_handler(self):
        try:
            if len(self.password_lineEdit.text()) < 1:
                self.pop_window("Enter Valid Data!")
            else:
                username = self.username_lineEdit.text()
                password = self.password_lineEdit.text()

                conn = sqlite3.connect('cubixUniversity.db')
                cursor = conn.cursor()

                cursor.execute("SELECT username,password FROM facultyCredentials")
                val = cursor.fetchall()
                if len(val) >= 0:
                    for x in val:
                        if username in x[0] and password in x[1]:
                            self.facultyDash()
                        else:
                            pass
                else:
                    self.pop_window("Unregistered!")
        except:
            self.pop_window("Invalid Login!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_Screen = QtWidgets.QMainWindow()
    ui = Ui_main_Screen()
    ui.setupUi(main_Screen)
    main_Screen.show()
    sys.exit(app.exec_())
