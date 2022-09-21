from PyQt5 import QtCore, QtGui, QtWidgets
from studentDashboard import *
from registration import *
from getNumberScreen import *
class Ui_main_Screen(object):
    def getNumber(self):
        self.getnumber_screen = QtWidgets.QMainWindow()
        self.ui = Ui_getnumber_screen()
        self.ui.setupUi(self.getnumber_screen)
        self.getnumber_screen.show()

    def openwindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_registration()
                self.ui.setupUi(self.window)
                self.window.show()
                main_Screen.hide()

    def studentDash(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self.window)
        self.window.show()
        main_Screen.hide()

    def setupUi(self, main_Screen):
        main_Screen.setObjectName("main_Screen")
        main_Screen.resize(950, 650)
        main_Screen.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(main_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 491, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("mainScreen_bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 321, 391))
        self.label_2.setStyleSheet("background-color: rgb(20, 35, 91);\n"
"border-radius: 25px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.user_Icon = QtWidgets.QLabel(self.centralwidget)
        self.user_Icon.setGeometry(QtCore.QRect(160, 80, 141, 141))
        self.user_Icon.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 60px;\n"
"")
        self.user_Icon.setText("")
        self.user_Icon.setPixmap(QtGui.QPixmap("user.png"))
        self.user_Icon.setScaledContents(True)
        self.user_Icon.setObjectName("user_Icon")
        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(110, 280, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 35, 91);\n"
"border: 0;")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 240, 91, 31))
        self.label_3.setStyleSheet("font: 63 22pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 320, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(110, 350, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(20, 35, 91);\n"
"border: 0;")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 390, 241, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.signin_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.signin_pushButton.clicked.connect(self.btn_login_handler)
        self.signin_pushButton.setGeometry(QtCore.QRect(150, 440, 161, 41))
        self.signin_pushButton.setStyleSheet("border: 1px solid white;\n"
"color: rgb(255,255,255);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"border-radius: 15px;")
        self.signin_pushButton.setObjectName("signin_pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 0, 475, 650))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(75, 103, 118);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.getNum_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getNum_pushButton.clicked.connect(self.getNumber)
        self.getNum_pushButton.clicked.connect(main_Screen.close)
        self.getNum_pushButton.setGeometry(QtCore.QRect(590, 510, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.getNum_pushButton.setFont(font)
        self.getNum_pushButton.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 15px;\n"
"")
        self.getNum_pushButton.setObjectName("getNum_pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 470, 131, 31))
        self.label_6.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 500, 151, 20))
        self.label_7.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.registerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerBtn.clicked.connect(self.btn_newuser_handler)
        self.registerBtn.setGeometry(QtCore.QRect(260, 500, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.registerBtn.setFont(font)
        self.registerBtn.setStyleSheet("background-color: rgb(154, 1, 1);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Segoe UI Semibold\";")
        self.registerBtn.setFlat(True)
        self.registerBtn.setObjectName("registerBtn")
        self.design = QtWidgets.QLabel(self.centralwidget)
        self.design.setGeometry(QtCore.QRect(550, 190, 331, 261))
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
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 75 30pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 150, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(600, 170, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label.raise_()
        self.label_2.raise_()
        self.user_Icon.raise_()
        self.username_lineEdit.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.password_lineEdit.raise_()
        self.line_2.raise_()
        self.signin_pushButton.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.registerBtn.raise_()
        self.design.raise_()
        self.getNum_pushButton.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        main_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_Screen)
        QtCore.QMetaObject.connectSlotsByName(main_Screen)

    def retranslateUi(self, main_Screen):
        _translate = QtCore.QCoreApplication.translate
        main_Screen.setWindowTitle(_translate("main_Screen", "Main Screen"))
        self.username_lineEdit.setPlaceholderText(_translate("main_Screen", "Username"))
        self.label_3.setText(_translate("main_Screen", "LOGIN"))
        self.password_lineEdit.setPlaceholderText(_translate("main_Screen", "Password"))
        self.signin_pushButton.setText(_translate("main_Screen", "SIGN IN"))
        self.getNum_pushButton.setText(_translate("main_Screen", "Get your ticket number here!"))
        self.label_6.setText(_translate("main_Screen", "Not enrolled yet?"))
        self.label_5.setText(_translate("main_Screen", "C U B I X "))
        self.label_8.setText(_translate("main_Screen", "WELCOME BACK!"))
        self.label_9.setText(_translate("main_Screen", "Enter your login details"))
        self.label_10.setText(_translate("main_Screen", "and start your journey with us!"))


    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setInformativeText('{}'.format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()

    def btn_newuser_handler(self):
        self.openwindow()

    def btn_login_handler(self):
            try:
                if len(self.password_lineEdit.text()) < 1:
                    self.pop_window("Enter Valid Data!")
                else:
                    username = self.username_lineEdit.text()
                    password = self.password_lineEdit.text()

                    conn = sqlite3.connect('cubixUniversity.db')
                    cursor = conn.cursor()

                    cursor.execute("SELECT username,password FROM studentCredentials")
                    val = cursor.fetchall()
                    if len(val) >= 0:
                        for x in val:
                            if username in x[0] and password in x[1]:
                                self.studentDash()
                            else:
                                pass
                    else:
                        self.pop_window("Unregistered!")
            except:
                self.pop_window("Invalid!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_Screen = QtWidgets.QMainWindow()
    ui = Ui_main_Screen()
    ui.setupUi(main_Screen)
    main_Screen.show()
    sys.exit(app.exec_())
