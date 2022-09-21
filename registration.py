from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from main import *
class Ui_registration(object):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_main_Screen()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, registration):
        registration.setObjectName("registration")
        registration.resize(950, 650)
        self.label_6 = QtWidgets.QLabel(registration)
        self.label_6.setGeometry(QtCore.QRect(80, 350, 91, 41))
        self.label_6.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(registration)
        self.pushButton.setGeometry(QtCore.QRect(250, 540, 161, 41))
        self.pushButton.setStyleSheet("font: 90 16pt \"Garamond\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(243, 255, 110);\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.emailLineEdit = QtWidgets.QLineEdit(registration)
        self.emailLineEdit.setGeometry(QtCore.QRect(210, 350, 281, 41))
        self.emailLineEdit.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(0, 0, 0);")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.usernamelineEdit = QtWidgets.QLineEdit(registration)
        self.usernamelineEdit.setGeometry(QtCore.QRect(210, 430, 281, 41))
        self.usernamelineEdit.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(0, 0, 0);")
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.label_5 = QtWidgets.QLabel(registration)
        self.label_5.setGeometry(QtCore.QRect(360, 170, 271, 31))
        self.label_5.setStyleSheet("font: 75 22pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_5.setObjectName("label_5")
        self.firstNameLineEdit = QtWidgets.QLineEdit(registration)
        self.firstNameLineEdit.setGeometry(QtCore.QRect(210, 280, 281, 41))
        self.firstNameLineEdit.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(0, 0, 0);")
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.label_7 = QtWidgets.QLabel(registration)
        self.label_7.setGeometry(QtCore.QRect(80, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(registration)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 950, 651))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../CC15 Final Project/cool-geometric-triangular-figure-neon-laser-light-great-backgrounds-wallpapers_181624-9331.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(registration)
        self.label_3.setGeometry(QtCore.QRect(510, 430, 91, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(registration)
        self.label.setGeometry(QtCore.QRect(260, 90, 481, 51))
        self.label.setStyleSheet("font: 75 28pt \"Rockwell\";\n"
"color: rgb(243, 255, 110);")
        self.label.setObjectName("label")
        self.passwordLineEdit = QtWidgets.QLineEdit(registration)
        self.passwordLineEdit.setGeometry(QtCore.QRect(610, 430, 281, 41))
        self.passwordLineEdit.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(0, 0, 0);")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.label_2 = QtWidgets.QLabel(registration)
        self.label_2.setGeometry(QtCore.QRect(80, 430, 91, 41))
        self.label_2.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_2.setObjectName("label_2")
        self.lastNameLineEdit = QtWidgets.QLineEdit(registration)
        self.lastNameLineEdit.setGeometry(QtCore.QRect(610, 280, 281, 41))
        self.lastNameLineEdit.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(0, 0, 0);")
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.label_9 = QtWidgets.QLabel(registration)
        self.label_9.setGeometry(QtCore.QRect(510, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_9.setObjectName("label_9")
        self.phoneLineEdit = QtWidgets.QLineEdit(registration)
        self.phoneLineEdit.setGeometry(QtCore.QRect(610, 350, 281, 41))
        self.phoneLineEdit.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(0, 0, 0);")
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.label_10 = QtWidgets.QLabel(registration)
        self.label_10.setGeometry(QtCore.QRect(510, 350, 91, 41))
        self.label_10.setStyleSheet("font: 75 16pt \"Garamond\";\n"
"color: rgb(243, 255, 110);")
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(registration)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 540, 161, 41))
        self.pushButton_2.setStyleSheet("font: 90 16pt \"Garamond\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(243, 255, 110);\n"
"border-radius: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.emailLineEdit.raise_()
        self.usernamelineEdit.raise_()
        self.label_5.raise_()
        self.firstNameLineEdit.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.passwordLineEdit.raise_()
        self.label_2.raise_()
        self.lastNameLineEdit.raise_()
        self.label_9.raise_()
        self.phoneLineEdit.raise_()
        self.label_10.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "Dialog"))
        self.label_6.setText(_translate("registration", "Email"))
        self.pushButton.setText(_translate("registration", "Register"))
        self.pushButton.clicked.connect(self.database)
        self.emailLineEdit.setPlaceholderText(_translate("registration", "Email"))
        self.usernamelineEdit.setPlaceholderText(_translate("registration", "Username"))
        self.label_5.setText(_translate("registration", "CREATE ACCOUNT"))
        self.firstNameLineEdit.setPlaceholderText(_translate("registration", "First Name"))
        self.label_7.setText(_translate("registration", "First Name"))
        self.label_3.setText(_translate("registration", "Password"))
        self.label.setText(_translate("registration", "Queue Management System"))
        self.passwordLineEdit.setPlaceholderText(_translate("registration", "Password"))
        self.label_2.setText(_translate("registration", "Username"))
        self.lastNameLineEdit.setPlaceholderText(_translate("registration", "Last Name"))
        self.label_9.setText(_translate("registration", "Last Name"))
        self.phoneLineEdit.setPlaceholderText(_translate("registration", "Phone Number"))
        self.label_10.setText(_translate("registration", "Phone #"))
        self.pushButton_2.setText(_translate("registration", "Main Menu"))
        self.pushButton_2.clicked.connect(self.btn_exit_handler)

    def btn_exit_handler(self):
        self.openwindow()

    def pop_message(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def database(self):
        try:
            txt_firstname = self.firstNameLineEdit.text()
            txt_lastname = self.lastNameLineEdit.text()
            txt_phone = self.phoneLineEdit.text()
            txt_email = self.emailLineEdit.text()
            txt_username = self.usernamelineEdit.text()
            txt_password = self.passwordLineEdit.text()

            conn = sqlite3.connect('registeredUsers.db')
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS userCredentials
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                fname TEXT, 
                lname TEXT, 
                Phone TEXT, 
                email TEXT,
                username TEXT, 
                password TEXT)""")

            cursor.execute(""" INSERT INTO userCredentials
                (fname,
                lname,
                Phone,
                email,
                username, 
                password)

            VALUES 
            (?,?,?,?,?,?)
            """, (txt_firstname, txt_lastname, txt_phone, txt_email, txt_username, txt_password))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Added to Database ")
        except:
            self.pop_message("Cannot add  to  Database ")


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        registration = QtWidgets.QDialog()
        ui = Ui_registration()
        ui.setupUi(registration)
        registration.show()
        sys.exit(app.exec_())
