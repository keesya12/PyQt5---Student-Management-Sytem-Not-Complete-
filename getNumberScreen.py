from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sqlite3
class Ui_getnumber_screen(object):



    def setupUi(self, getnumber_screen):
        getnumber_screen.setObjectName("getnumber_screen")
        getnumber_screen.resize(950, 650)
        self.centralwidget = QtWidgets.QWidget(getnumber_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 651))
        self.label.setStyleSheet("background-color: rgb(75, 103, 118);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 90, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(65)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 75 65pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 230, 331, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("welcome_screen logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 330, 261, 71))
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
        self.name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_lineEdit.setGeometry(QtCore.QRect(600, 260, 241, 41))
        self.name_lineEdit.setStyleSheet("border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Garamond\";\n"
"background-color: rgb(75, 103, 118);\n"
"")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.course_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.course_LineEdit.setGeometry(QtCore.QRect(600, 340, 241, 41))
        self.course_LineEdit.setStyleSheet("border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Garamond\";\n"
"background-color: rgb(75, 103, 118);\n"
"")
        self.course_LineEdit.setText("")
        self.course_LineEdit.setObjectName("course_LineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 180, 281, 31))
        self.label_5.setStyleSheet("font: 12pt \"Verdana\";\n"
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 440, 141, 51))
        self.pushButton.setStyleSheet("font: 75 14pt \"Agency FB\";\n"
"border: 1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_clicked)
        getnumber_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(getnumber_screen)
        QtCore.QMetaObject.connectSlotsByName(getnumber_screen)

    def retranslateUi(self, getnumber_screen):
        _translate = QtCore.QCoreApplication.translate
        getnumber_screen.setWindowTitle(_translate("getnumber_screen", "Get Your Ticket Number!"))
        self.label_4.setText(_translate("getnumber_screen", "WELCOME"))
        self.label_3.setText(_translate("getnumber_screen", "C U B I X "))
        self.name_lineEdit.setPlaceholderText(_translate("getnumber_screen", "Name"))
        self.course_LineEdit.setPlaceholderText(_translate("getnumber_screen", "Course"))
        self.label_5.setText(_translate("getnumber_screen", "Enter details to get your number!"))
        self.pushButton.setText(_translate("getnumber_screen", "GET NUMBER"))

    def pop_message(self, text):
            msg = QtWidgets.QMessageBox()
            msg.setText("{}".format(text))
            msg.exec_()
    def getNumber(self):
        try:
            txt_Name = self.name_lineEdit.text()
            txt_Course = self.course_LineEdit.text()

            conn = sqlite3.connect('cubixUniversity.db')
            cursor = conn.cursor()
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS queueNumbers
                     ( ID_Number	INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                       Name TEXT,
                       Course TEXT)""")

            cursor.execute("INSERT INTO queueNumbers (Name,course,queueNum) VALUES (?,?,?)", (txt_Name,txt_Course,))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Added to Database ")
        except:
            print("Cannot add  to  Database ")

    def on_clicked(self):
        print('yo')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    getnumber_screen = QtWidgets.QMainWindow()
    ui = Ui_getnumber_screen()
    ui.setupUi(getnumber_screen)
    getnumber_screen.show()
    sys.exit(app.exec_())
