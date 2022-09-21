from PyQt5 import QtCore, QtGui, QtWidgets
from adminDash import *
import sqlite3

class Ui_studentRegistration(object):


    def setupUi(self, studentRegistration):
        studentRegistration.setObjectName("studentRegistration")
        studentRegistration.resize(950, 650)
        studentRegistration.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(studentRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 481, 650))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 431, 351))
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("welcome_screen logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(315, 80, 161, 61))
        self.label_3.setStyleSheet("font: 48pt \"Agency FB\";\n"
"font-weight: 900;\n"
"color: rgb(75, 103, 118);\n"
"background-color: none;")
        self.label_3.setObjectName("label_3")
        self.Idno_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.Idno_lineEdit.setGeometry(QtCore.QRect(140, 150, 221, 40))
        self.Idno_lineEdit.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"font: 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;")
        self.Idno_lineEdit.setObjectName("Idno_lineEdit")
        self.fname_lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.fname_lineEdit_2.setGeometry(QtCore.QRect(140, 250, 221, 40))
        self.fname_lineEdit_2.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"font: 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;")
        self.fname_lineEdit_2.setObjectName("fname_lineEdit_2")
        self.lname_lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lname_lineEdit_3.setGeometry(QtCore.QRect(140, 350, 221, 40))
        self.lname_lineEdit_3.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"font: 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;")
        self.lname_lineEdit_3.setObjectName("lname_lineEdit_3")
        self.address_lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.address_lineEdit_5.setGeometry(QtCore.QRect(140, 445, 221, 40))
        self.address_lineEdit_5.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"font: 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;")
        self.address_lineEdit_5.setObjectName("address_lineEdit_5")
        self.phone_lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.phone_lineEdit_6.setGeometry(QtCore.QRect(140, 540, 221, 40))
        self.phone_lineEdit_6.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"font: 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;")
        self.phone_lineEdit_6.setObjectName("phone_lineEdit_6")
        self.Idno = QtWidgets.QLabel(self.frame)
        self.Idno.setGeometry(QtCore.QRect(20, 150, 65, 40))
        self.Idno.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(75, 103, 118);\n"
"font-weight: 500;")
        self.Idno.setObjectName("Idno")
        self.fname = QtWidgets.QLabel(self.frame)
        self.fname.setGeometry(QtCore.QRect(20, 250, 121, 40))
        self.fname.setStyleSheet("font: 75 13.5pt \"Georgia\";\n"
"color: rgb(75, 103, 118);\n"
"font-weight: 500;")
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLabel(self.frame)
        self.lname.setGeometry(QtCore.QRect(20, 350, 111, 40))
        self.lname.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(75, 103, 118);\n"
"font-weight: 500;")
        self.lname.setObjectName("lname")
        self.address = QtWidgets.QLabel(self.frame)
        self.address.setGeometry(QtCore.QRect(20, 440, 91, 40))
        self.address.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(75, 103, 118);\n"
"font-weight: 500;")
        self.address.setObjectName("address")
        self.phone = QtWidgets.QLabel(self.frame)
        self.phone.setGeometry(QtCore.QRect(20, 535, 121, 40))
        self.phone.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(75, 103, 118);\n"
"font-weight: 500;")
        self.phone.setObjectName("phone")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(380, 20, 161, 61))
        self.label_9.setStyleSheet("font: 48pt \"Agency FB\";\n"
"font-weight: 900;\n"
"color: rgb(75, 103, 118);\n"
"background-color: none;")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 590, 161, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Rockwell\";\n"
"color:rgb(0,0,0);\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(73, 135, 255, 255), stop:1 rgba(185, 91, 225, 255));")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(480, 0, 475, 650))
        self.frame_2.setStyleSheet("background-color: rgb(75, 103, 118);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(-240, 170, 451, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("welcome_screen logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(-10, 80, 161, 61))
        self.label_4.setStyleSheet("font: 48pt \"Agency FB\";\n"
"font-weight: 900;\n"
"color: rgb(255,255,255);")
        self.label_4.setObjectName("label_4")
        self.password_lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.password_lineEdit_11.setGeometry(QtCore.QRect(230, 540, 221, 40))
        self.password_lineEdit_11.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Verdana\";")
        self.password_lineEdit_11.setObjectName("password_lineEdit_11")
        self.username_lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.username_lineEdit_10.setGeometry(QtCore.QRect(230, 445, 221, 40))
        self.username_lineEdit_10.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Verdana\";")
        self.username_lineEdit_10.setObjectName("username_lineEdit_10")
        self.Gender_lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.Gender_lineEdit_7.setGeometry(QtCore.QRect(230, 150, 221, 40))
        self.Gender_lineEdit_7.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Verdana\";")
        self.Gender_lineEdit_7.setObjectName("Gender_lineEdit_7")
        self.Email_lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.Email_lineEdit_8.setGeometry(QtCore.QRect(230, 250, 221, 40))
        self.Email_lineEdit_8.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Verdana\";")
        self.Email_lineEdit_8.setObjectName("Email_lineEdit_8")
        self.course_lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.course_lineEdit_9.setGeometry(QtCore.QRect(230, 350, 221, 40))
        self.course_lineEdit_9.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Verdana\";")
        self.course_lineEdit_9.setObjectName("course_lineEdit_9")
        self.Gender = QtWidgets.QLabel(self.frame_2)
        self.Gender.setGeometry(QtCore.QRect(95, 150, 91, 40))
        self.Gender.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(255,255,255);\n"
"font-weight: 500;")
        self.Gender.setObjectName("Gender")
        self.Email = QtWidgets.QLabel(self.frame_2)
        self.Email.setGeometry(QtCore.QRect(95, 250, 91, 40))
        self.Email.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(255,255,255);\n"
"font-weight: 500;\n"
"background-color: none;")
        self.Email.setObjectName("Email")
        self.course = QtWidgets.QLabel(self.frame_2)
        self.course.setGeometry(QtCore.QRect(95, 350, 131, 40))
        self.course.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(255,255,255);\n"
"font-weight: 500;\n"
"background-color: none;\n"
"")
        self.course.setObjectName("course")
        self.Username = QtWidgets.QLabel(self.frame_2)
        self.Username.setGeometry(QtCore.QRect(95, 440, 131, 40))
        self.Username.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(255,255,255);\n"
"font-weight: 500;")
        self.Username.setObjectName("Username")
        self.password = QtWidgets.QLabel(self.frame_2)
        self.password.setGeometry(QtCore.QRect(95, 540, 131, 40))
        self.password.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(255,255,255);\n"
"font-weight: 500;")
        self.password.setObjectName("password")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(-10, 20, 111, 61))
        self.label_10.setStyleSheet("font: 48pt \"Agency FB\";\n"
"font-weight: 900;\n"
"color: rgb(255,255,255);")
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 590, 161, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Rockwell\";\n"
"color:rgb(0,0,0);\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.329727, y1:0.432, x2:0.938, y2:0.619318, stop:0.215909 rgba(162, 223, 176, 255), stop:0.698864 rgba(200, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        studentRegistration.setCentralWidget(self.centralwidget)

        self.retranslateUi(studentRegistration)
        QtCore.QMetaObject.connectSlotsByName(studentRegistration)

    def retranslateUi(self, studentRegistration):
        _translate = QtCore.QCoreApplication.translate
        studentRegistration.setWindowTitle(_translate("studentRegistration", "Student Registration"))
        self.label_3.setText(_translate("studentRegistration", "REGISTER"))
        self.Idno.setText(_translate("studentRegistration", "ID No:"))
        self.fname.setText(_translate("studentRegistration", "First Name :"))
        self.lname.setText(_translate("studentRegistration", "Last Name :"))
        self.address.setText(_translate("studentRegistration", "Address :"))
        self.phone.setText(_translate("studentRegistration", "Phone No.:"))
        self.label_9.setText(_translate("studentRegistration", "STUD"))
        self.pushButton.setText(_translate("studentRegistration", "ADD STUDENT"))
        self.pushButton.clicked.connect(self.addingData)
        self.pushButton.clicked.connect(studentRegistration.close)
        self.label_4.setText(_translate("studentRegistration", "RATION"))
        self.Gender.setText(_translate("studentRegistration", "Gender :"))
        self.Email.setText(_translate("studentRegistration", "Email :"))
        self.course.setText(_translate("studentRegistration", "Course :"))
        self.Username.setText(_translate("studentRegistration", "Username :"))
        self.password.setText(_translate("studentRegistration", "Password :"))
        self.label_10.setText(_translate("studentRegistration", "DENT"))
        self.pushButton_2.setText(_translate("studentRegistration", "BACK"))
        self.pushButton_2.clicked.connect(self.btn_exit_handler)
    def btn_exit_handler(self):
        self.openAdminDashboard()

    def pop_message(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()
    def addingData(self):
        self.database()
    def database(self):
        try:
            txt_id_no = self.Idno_lineEdit.text()
            txt_firstname = self.fname_lineEdit_2.text()
            txt_lastname = self.lname_lineEdit_3.text()
            txt_address = self.address_lineEdit_5.text()
            txt_phone = self.phone_lineEdit_6.text()
            txt_gender=self.Gender_lineEdit_7.text()
            txt_email = self.Email_lineEdit_8.text()
            txt_course = self.course_lineEdit_9.text()
            txt_username = self.username_lineEdit_10.text()
            txt_password = self.password_lineEdit_11.text()

            conn = sqlite3.connect('cubixUniversity.db')
            cursor = conn.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS studentCredentials
             ( ID_Number	INTEGER PRIMARY KEY NOT NULL, 
               fname	TEXT NOT NULL,
	           lname	TEXT NOT NULL,
               address	TEXT NOT NULL,
	           Phone	TEXT NOT NULL,
	           gender	TEXT NOT NULL,
	           email	TEXT NOT NULL,
	           course	TEXT NOT NULL,
	           username	TEXT NOT NULL,
	           password	TEXT NOT NULL)""")

            cursor.execute("INSERT INTO studentCredentials (ID_Number,fname,lname,address, Phone, gender,email,course,username, password) VALUES (?,?,?,?,?,?,?,?,?,?)", (txt_id_no,txt_firstname, txt_lastname, txt_address, txt_phone, txt_gender, txt_email, txt_course, txt_username, txt_password))
            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Added to Database ")
        except:
            self.pop_message("Cannot add  to  Database ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentRegistration = QtWidgets.QMainWindow()
    ui = Ui_studentRegistration()
    ui.setupUi(studentRegistration)
    studentRegistration.show()
    sys.exit(app.exec_())
