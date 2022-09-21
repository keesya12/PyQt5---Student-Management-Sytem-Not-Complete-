from PyQt5 import QtCore, QtGui, QtWidgets
from adminDash import *

class Ui_adminloginscreen(object):

    def openAdminDashboard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =Ui_AdminDashboard()
        self.ui.setupUi(self.window)
        self.window.show()
        adminloginscreen.hide()

    def setupUi(self, adminloginscreen):
        adminloginscreen.setObjectName("adminloginscreen")
        adminloginscreen.resize(950, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("admin_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        adminloginscreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(adminloginscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 651))
        self.label.setStyleSheet("background-color: rgb(75, 103, 118);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 180, 331, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("welcome_screen logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 280, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 75 72pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(470, 60, 61, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setGeometry(QtCore.QRect(600, 270, 241, 31))
        self.usernameLineEdit.setStyleSheet("border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Garamond\";\n"
"background-color: rgb(65,65,65,30);\n"
"")
        self.usernameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.password_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_LineEdit.setGeometry(QtCore.QRect(610, 350, 241, 31))
        self.password_LineEdit.setStyleSheet("border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Garamond\";\n"
"background-color: rgb(65,65,65,30);\n"
"\n"
"")
        self.password_LineEdit.setText("")
        self.password_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_LineEdit.setReadOnly(False)
        self.password_LineEdit.setClearButtonEnabled(True)
        self.password_LineEdit.setObjectName("password_LineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 200, 131, 31))
        self.label_5.setStyleSheet("font: 25pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(600, 300, 261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(600, 380, 261, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.login_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.login_pushButton.clicked.connect(self.login)
        self.login_pushButton.setGeometry(QtCore.QRect(680, 430, 121, 41))
        self.login_pushButton.setStyleSheet("font: 75 25pt \"Agency FB\";\n"
"border: 1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.login_pushButton.setObjectName("login_pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 170, 351, 341))
        self.label_4.setStyleSheet("background-color: rgb(65, 65, 65,180);\n"
"border: 1px solid white;\n"
"border-radius: 25px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 260, 47, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("admin_icon.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 340, 47, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("password_icon.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.line_2.raise_()
        self.password_LineEdit.raise_()
        self.line_3.raise_()
        self.usernameLineEdit.raise_()
        self.login_pushButton.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        adminloginscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminloginscreen)
        QtCore.QMetaObject.connectSlotsByName(adminloginscreen)

    def retranslateUi(self, adminloginscreen):
        _translate = QtCore.QCoreApplication.translate
        adminloginscreen.setWindowTitle(_translate("adminloginscreen", "Admin"))
        self.label_3.setText(_translate("adminloginscreen", "C U B I X "))
        self.usernameLineEdit.setPlaceholderText(_translate("adminloginscreen", "Name"))
        self.password_LineEdit.setPlaceholderText(_translate("adminloginscreen", "Password"))
        self.label_5.setText(_translate("adminloginscreen", "ADMIN LOGIN"))
        self.login_pushButton.setText(_translate("adminloginscreen", "LOG IN"))

    def openWindow(self):
        self.openAdminDashboard()
    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()
    def login(self):
        try:
            username = self.usernameLineEdit.text()
            password = self.password_LineEdit.text()

            if username == 'admin' and password == '120300':
                    self.openWindow()
            else:
                    self.pop_window("Unregistered!")
        except:
            self.pop_window("Invalid!")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminloginscreen = QtWidgets.QMainWindow()
    ui = Ui_adminloginscreen()
    ui.setupUi(adminloginscreen)
    adminloginscreen.show()
    sys.exit(app.exec_())
