from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_facultyRegistration(object):
    def setupUi(self, facultyRegistration):
        facultyRegistration.setObjectName("facultyRegistration")
        facultyRegistration.resize(950, 650)
        facultyRegistration.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(facultyRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 481, 650))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 431, 351))
        self.label_2.setStyleSheet("background-color: none;")
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
        self.Age_lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.Age_lineEdit_6.setGeometry(QtCore.QRect(140, 540, 221, 40))
        self.Age_lineEdit_6.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"font: 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;")
        self.Age_lineEdit_6.setObjectName("Age_lineEdit_6")
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
        self.Age = QtWidgets.QLabel(self.frame)
        self.Age.setGeometry(QtCore.QRect(20, 535, 91, 40))
        self.Age.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(75, 103, 118);\n"
"font-weight: 500;")
        self.Age.setObjectName("Age")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(380, 20, 161, 61))
        self.label_9.setStyleSheet("font: 48pt \"Agency FB\";\n"
"font-weight: 900;\n"
"color: rgb(75, 103, 118);\n"
"background-color: none;")
        self.label_9.setObjectName("label_9")
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
        self.Department_lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.Department_lineEdit_9.setGeometry(QtCore.QRect(230, 350, 221, 40))
        self.Department_lineEdit_9.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Verdana\";")
        self.Department_lineEdit_9.setObjectName("Department_lineEdit_9")
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
        self.dept = QtWidgets.QLabel(self.frame_2)
        self.dept.setGeometry(QtCore.QRect(95, 350, 131, 40))
        self.dept.setStyleSheet("font: 75 14pt \"Georgia\";\n"
"color: rgb(255,255,255);\n"
"font-weight: 500;\n"
"background-color: none;\n"
"")
        self.dept.setObjectName("dept")
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
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(270, 590, 151, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Rockwell\";\n"
"color:rgb(0,0,0);\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.153, y1:0.284091, x2:0.898, y2:0.153409, stop:0.244318 rgba(230, 183, 122, 255), stop:0.829545 rgba(194, 144, 198, 255));")
        self.pushButton.setObjectName("pushButton")
        facultyRegistration.setCentralWidget(self.centralwidget)

        self.retranslateUi(facultyRegistration)
        QtCore.QMetaObject.connectSlotsByName(facultyRegistration)

    def retranslateUi(self, facultyRegistration):
        _translate = QtCore.QCoreApplication.translate
        facultyRegistration.setWindowTitle(_translate("facultyRegistration", "Faculty Registration"))
        self.label_3.setText(_translate("facultyRegistration", "REGISTR"))
        self.Idno.setText(_translate("facultyRegistration", "ID No:"))
        self.fname.setText(_translate("facultyRegistration", "First Name :"))
        self.lname.setText(_translate("facultyRegistration", "Last Name :"))
        self.address.setText(_translate("facultyRegistration", "Address :"))
        self.Age.setText(_translate("facultyRegistration", "Phone No.:"))
        self.label_9.setText(_translate("facultyRegistration", "FACU"))
        self.label_4.setText(_translate("facultyRegistration", "RATION"))
        self.Gender.setText(_translate("facultyRegistration", "Gender :"))
        self.Email.setText(_translate("facultyRegistration", "Email :"))
        self.dept.setText(_translate("facultyRegistration", "Department :"))
        self.Username.setText(_translate("facultyRegistration", "Username :"))
        self.password.setText(_translate("facultyRegistration", "Password :"))
        self.label_10.setText(_translate("facultyRegistration", "ULTY"))
        self.pushButton.setText(_translate("facultyRegistration", "ADD FACULTY"))
        self.pushButton.clicked.connect(self.addingData)
        self.pushButton.clicked.connect(facultyRegistration.close)

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
            txt_phone = self.Age_lineEdit_6.text()
            txt_gender=self.Gender_lineEdit_7.text()
            txt_email = self.Email_lineEdit_8.text()
            txt_dept = self.Department_lineEdit_9.text()
            txt_username = self.username_lineEdit_10.text()
            txt_password = self.password_lineEdit_11.text()

            conn = sqlite3.connect('cubixUniversity.db')
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS facultyCredentials
             ( ID_Number	INTEGER PRIMARY KEY NOT NULL, 
               firstname	TEXT NOT NULL,
	           lastname	TEXT NOT NULL,
               address	TEXT NOT NULL,
	           Phone	TEXT NOT NULL,
	           gender	TEXT NOT NULL,
	           email	TEXT NOT NULL,
	           department	TEXT NOT NULL,
	           username	TEXT NOT NULL,
	           password	TEXT NOT NULL)""")

            cursor.execute("INSERT INTO facultyCredentials (ID_Number,firstname,lastname,address, Phone, gender,email,department,username, password) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (txt_id_no,txt_firstname, txt_lastname, txt_address, txt_phone, txt_gender, txt_email, txt_dept, txt_username,txt_password, ))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Added to Database ")
        except:
            self.pop_message("Cannot add  to  Database ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    facultyRegistration = QtWidgets.QMainWindow()
    ui = Ui_facultyRegistration()
    ui.setupUi(facultyRegistration)
    facultyRegistration.show()
    sys.exit(app.exec_())
