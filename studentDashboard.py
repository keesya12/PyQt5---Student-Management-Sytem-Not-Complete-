from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import sqlite3, queue

class Ui_dashboard(object):
    count = 0

    def btn_is_clicked(self):
        global count
        if self.count <= 99:
            self.count += 1
            self.lcdNumber.display(self.count)

    def openwindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_main_Screen()
                self.ui.setupUi(self.window)
                self.window.show()

    def setupUi(self, dashboard):
        dashboard.setObjectName("dashboard")
        dashboard.resize(950, 600)
        dashboard.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 241, 31))
        self.label_8.setStyleSheet("font: 75 20pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 491, 51))
        self.label.setStyleSheet("font: 75 28pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.dashboard_student = QtWidgets.QTabWidget(self.centralwidget)
        self.dashboard_student.setGeometry(QtCore.QRect(-9, 120, 961, 650))
        self.dashboard_student.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Southiya")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dashboard_student.setFont(font)
        self.dashboard_student.setAutoFillBackground(False)
        self.dashboard_student.setStyleSheet("background-color: rgb(75, 103, 118);\n"
"border: 0px;\n"
"font: 13pt \"Southiya\";")
        self.dashboard_student.setTabPosition(QtWidgets.QTabWidget.North)
        self.dashboard_student.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.dashboard_student.setIconSize(QtCore.QSize(16, 16))
        self.dashboard_student.setElideMode(QtCore.Qt.ElideNone)
        self.dashboard_student.setTabBarAutoHide(False)
        self.dashboard_student.setObjectName("dashboard_student")
        self.myapp = QtWidgets.QWidget()
        self.myapp.setObjectName("myapp")
        self.label_10 = QtWidgets.QLabel(self.myapp)
        self.label_10.setGeometry(QtCore.QRect(350, 70, 211, 21))
        self.label_10.setStyleSheet("font: 75 14pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.myapp)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(110, 180, 201, 141))
        self.plainTextEdit_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setBackgroundVisible(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.myapp)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(350, 180, 201, 141))
        self.plainTextEdit_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.myapp)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(590, 180, 201, 141))
        self.plainTextEdit_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_12 = QtWidgets.QLabel(self.myapp)
        self.label_12.setGeometry(QtCore.QRect(110, 150, 201, 31))
        self.label_12.setStyleSheet("font: 75 14pt \"Rockwell\";\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 4px;\n"
"text-alignment: center;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.myapp)
        self.label_13.setGeometry(QtCore.QRect(350, 150, 201, 31))
        self.label_13.setStyleSheet("font: 75 14pt \"Rockwell\";\n"
"background-color:  rgb(255, 255, 127);\n"
"border-radius: 4px;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.myapp)
        self.label_14.setGeometry(QtCore.QRect(590, 150, 201, 31))
        self.label_14.setStyleSheet("font: 75 13pt \"Rockwell\";\n"
"background-color: rgb(170, 255, 0);")
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.myapp)
        self.label_16.setGeometry(QtCore.QRect(70, 40, 831, 351))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.sentApp_num = QtWidgets.QLCDNumber(self.myapp)
        self.sentApp_num.setGeometry(QtCore.QRect(130, 210, 141, 81))
        self.sentApp_num.setStyleSheet("border: 0;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.sentApp_num.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sentApp_num.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sentApp_num.setObjectName("sentApp_num")
        self.label_18 = QtWidgets.QLabel(self.myapp)
        self.label_18.setGeometry(QtCore.QRect(120, 210, 81, 71))
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("sent_icon.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.myapp)
        self.label_19.setGeometry(QtCore.QRect(380, 210, 61, 71))
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("past_icon.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.sentApp_num_2 = QtWidgets.QLCDNumber(self.myapp)
        self.sentApp_num_2.setGeometry(QtCore.QRect(380, 210, 141, 81))
        self.sentApp_num_2.setStyleSheet("border: 0;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.sentApp_num_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sentApp_num_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sentApp_num_2.setObjectName("sentApp_num_2")
        self.sentApp_num_3 = QtWidgets.QLCDNumber(self.myapp)
        self.sentApp_num_3.setGeometry(QtCore.QRect(630, 210, 141, 81))
        self.sentApp_num_3.setStyleSheet("border: 0;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.sentApp_num_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sentApp_num_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sentApp_num_3.setObjectName("sentApp_num_3")
        self.label_20 = QtWidgets.QLabel(self.myapp)
        self.label_20.setGeometry(QtCore.QRect(630, 210, 61, 71))
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("cancelled_icon.ico"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_16.raise_()
        self.label_10.raise_()
        self.plainTextEdit_2.raise_()
        self.plainTextEdit_3.raise_()
        self.plainTextEdit_4.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.sentApp_num.raise_()
        self.label_18.raise_()
        self.sentApp_num_2.raise_()
        self.label_19.raise_()
        self.sentApp_num_3.raise_()
        self.label_20.raise_()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/d90fb743-f0c7-49ba-8a0f-37ea0ccf7924b6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_student.addTab(self.myapp, icon, "")
        self.setApp = QtWidgets.QWidget()
        self.setApp.setObjectName("setApp")
        self.label_3 = QtWidgets.QLabel(self.setApp)
        self.label_3.setGeometry(QtCore.QRect(270, 110, 31, 31))
        self.label_3.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.setApp)
        self.label_2.setGeometry(QtCore.QRect(380, 10, 181, 21))
        self.label_2.setStyleSheet("font: 75 14pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.setApp)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 161, 31))
        self.label_4.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.setApp)
        self.label_5.setGeometry(QtCore.QRect(270, 160, 51, 31))
        self.label_5.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.setApp)
        self.label_6.setGeometry(QtCore.QRect(70, 160, 51, 31))
        self.label_6.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.set = QtWidgets.QPushButton(self.setApp)
        self.set.clicked.connect(self.getData)
        self.set.setGeometry(QtCore.QRect(730, 330, 141, 41))
        self.set.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Rockwell\";\n"
"border-radius:10px;")
        self.set.setObjectName("set")
        self.prionum = QtWidgets.QPushButton(self.setApp)
        self.prionum.clicked.connect(self.btn_is_clicked)
        self.prionum.setGeometry(QtCore.QRect(80, 260, 191, 41))
        self.prionum.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.prionum.setObjectName("prionum")
        self.label_17 = QtWidgets.QLabel(self.setApp)
        self.label_17.setGeometry(QtCore.QRect(0, 10, 971, 461))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_9 = QtWidgets.QLabel(self.setApp)
        self.label_9.setGeometry(QtCore.QRect(530, 450, 31, 21))
        self.label_9.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_21 = QtWidgets.QLabel(self.setApp)
        self.label_21.setGeometry(QtCore.QRect(410, 450, 31, 21))
        self.label_21.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.setApp)
        self.label_22.setGeometry(QtCore.QRect(570, 450, 31, 21))
        self.label_22.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.toRecipient_lineEdit = QtWidgets.QLineEdit(self.setApp)
        self.toRecipient_lineEdit.setGeometry(QtCore.QRect(300, 110, 161, 31))
        self.toRecipient_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.toRecipient_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.toRecipient_lineEdit.setObjectName("toRecipient_lineEdit")
        self.date_lineEdit = QtWidgets.QLineEdit(self.setApp)
        self.date_lineEdit.setGeometry(QtCore.QRect(120, 160, 141, 31))
        self.date_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.date_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.date_lineEdit.setObjectName("date_lineEdit")
        self.time_lineEdit = QtWidgets.QLineEdit(self.setApp)
        self.time_lineEdit.setGeometry(QtCore.QRect(320, 160, 141, 31))
        self.time_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.time_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.concern_lineEdit = QtWidgets.QLineEdit(self.setApp)
        self.concern_lineEdit.setGeometry(QtCore.QRect(230, 210, 231, 31))
        self.concern_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.concern_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.concern_lineEdit.setObjectName("concern_lineEdit")
        self.purpose_lineEdit = QtWidgets.QLineEdit(self.setApp)
        self.purpose_lineEdit.setGeometry(QtCore.QRect(510, 110, 361, 201))
        self.purpose_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 5px;")
        self.purpose_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.purpose_lineEdit.setReadOnly(False)
        self.purpose_lineEdit.setObjectName("purpose_lineEdit")
        self.lcdNumber = QtWidgets.QLCDNumber(self.setApp)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 260, 101, 41))
        self.lcdNumber.setBaseSize(QtCore.QSize(15, 25))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("font: 14pt \"Rockwell\";\n"
"background-color: none;")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_24 = QtWidgets.QLabel(self.setApp)
        self.label_24.setGeometry(QtCore.QRect(70, 110, 51, 31))
        self.label_24.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.name_lineEdit = QtWidgets.QLineEdit(self.setApp)
        self.name_lineEdit.setGeometry(QtCore.QRect(120, 110, 141, 31))
        self.name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.label_17.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.set.raise_()
        self.prionum.raise_()
        self.label_9.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.toRecipient_lineEdit.raise_()
        self.date_lineEdit.raise_()
        self.time_lineEdit.raise_()
        self.concern_lineEdit.raise_()
        self.purpose_lineEdit.raise_()
        self.lcdNumber.raise_()
        self.label_24.raise_()
        self.name_lineEdit.raise_()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/301-3017875_group-fitness-training-icons-training-schedule-icon-png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_student.addTab(self.setApp, icon1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.set_2 = QtWidgets.QPushButton(self.tab)
        self.set_2.setGeometry(QtCore.QRect(520, 400, 201, 41))
        self.set_2.setStyleSheet("background-color: rgb(148, 0, 1);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.set_2.setObjectName("set_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(370, 20, 231, 21))
        self.label_7.setStyleSheet("font: 75 14pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.dataTable = QtWidgets.QTableWidget(self.tab)
        self.dataTable.setGeometry(QtCore.QRect(50, 60, 861, 331))
        self.dataTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.dataTable.setShowGrid(True)
        self.dataTable.setRowCount(10)
        self.dataTable.setColumnCount(6)
        self.dataTable.setObjectName("dataTable")
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, item)
        self.dataTable.horizontalHeader().setVisible(True)
        self.dataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.dataTable.horizontalHeader().setDefaultSectionSize(167)
        self.dataTable.horizontalHeader().setHighlightSections(True)
        self.dataTable.verticalHeader().setVisible(False)
        self.dataTable.verticalHeader().setDefaultSectionSize(41)
        self.dataTable.verticalHeader().setSortIndicatorShown(False)
        self.loaddata = QtWidgets.QPushButton(self.tab)
        self.loaddata.clicked.connect(self.loadData)
        self.loaddata.setGeometry(QtCore.QRect(200, 400, 151, 41))
        self.loaddata.setStyleSheet("background-color: rgb(255, 250, 98);\n"
"color: rgb(0,0,0);\n"
"font: 75 10pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.loaddata.setObjectName("loaddata")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ww/img/product-doc-management.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_student.addTab(self.tab, icon2, "")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(0, -70, 951, 381))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("studdashboard_bg.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.logout_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.logout_pushButton.clicked.connect(self.openwindow)
        self.logout_pushButton.clicked.connect(dashboard.close)
        self.logout_pushButton.setGeometry(QtCore.QRect(880, 10, 61, 61))
        self.logout_pushButton.setStyleSheet("border: none;\n"
"boder-radius: 25px;")
        self.logout_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("logout_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_pushButton.setIcon(icon3)
        self.logout_pushButton.setIconSize(QtCore.QSize(60, 70))
        self.logout_pushButton.setObjectName("logout_pushButton")
        self.label_15.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.dashboard_student.raise_()
        self.logout_pushButton.raise_()
        dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard)
        self.dashboard_student.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(dashboard)

    def retranslateUi(self, dashboard):
        _translate = QtCore.QCoreApplication.translate
        dashboard.setWindowTitle(_translate("dashboard", "Student Dashboard"))
        self.label_8.setText(_translate("dashboard", "Student Dashboard"))
        self.label.setText(_translate("dashboard", "Queue Management System"))
        self.label_10.setText(_translate("dashboard", "APPOINTMENT STATUS"))
        self.label_12.setText(_translate("dashboard", "Sent Appointments"))
        self.label_13.setText(_translate("dashboard", "Past Appointments"))
        self.label_14.setText(_translate("dashboard", "Cancelled Appointments"))
        self.dashboard_student.setTabText(self.dashboard_student.indexOf(self.myapp), _translate("dashboard", "My Appointments"))
        self.label_3.setText(_translate("dashboard", "TO"))
        self.label_2.setText(_translate("dashboard", "SET APPOINTMENT"))
        self.label_4.setText(_translate("dashboard", "TYPE OF CONCERN:"))
        self.label_5.setText(_translate("dashboard", "TIME:"))
        self.label_6.setText(_translate("dashboard", "DATE:"))
        self.set.setText(_translate("dashboard", "Set Appointment"))
        self.prionum.setText(_translate("dashboard", "Get Priority Number"))
        self.label_9.setText(_translate("dashboard", "TO"))
        self.label_21.setText(_translate("dashboard", "TO"))
        self.label_22.setText(_translate("dashboard", "TO"))
        self.toRecipient_lineEdit.setPlaceholderText(_translate("dashboard", "Recipient"))
        self.date_lineEdit.setPlaceholderText(_translate("dashboard", "Date"))
        self.time_lineEdit.setPlaceholderText(_translate("dashboard", "Time"))
        self.concern_lineEdit.setPlaceholderText(_translate("dashboard", "Concerns"))
        self.purpose_lineEdit.setPlaceholderText(_translate("dashboard", "Purpose"))
        self.label_24.setText(_translate("dashboard", "NAME"))
        self.name_lineEdit.setPlaceholderText(_translate("dashboard", "Name"))
        self.dashboard_student.setTabText(self.dashboard_student.indexOf(self.setApp), _translate("dashboard", "Set Appointment"))
        self.set_2.setText(_translate("dashboard", "CHECK APPOINTMENT QUEUE"))
        self.label_7.setText(_translate("dashboard", "APPOINTMENT RECORDS"))
        self.dataTable.setSortingEnabled(False)
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("dashboard", "Appointment No."))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("dashboard", "Recipient"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("dashboard", "Date"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("dashboard", "Time"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("dashboard", "Concern"))
        item = self.dataTable.horizontalHeaderItem(5)
        item.setText(_translate("dashboard", "Purpose"))
        self.loaddata.setText(_translate("dashboard", "LOAD DATA"))
        self.dashboard_student.setTabText(self.dashboard_student.indexOf(self.tab), _translate("dashboard", "Appointment Records"))

    def loadData(self):
        connection = sqlite3.connect('cubixUniversity.db')
        cur = connection.cursor()
        sqlstr = 'SELECT studentAppointments.AppointmentID, studentAppointments.Recipient, studentAppointments.date,studentAppointments.time, studentAppointments.concern,  studentAppointments.purpose FROM studentAppointments '
        self.dataTable.setRowCount(0)

        results = cur.execute(sqlstr)

        for row_number, row_data in enumerate(results):
            self.dataTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.dataTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def pop_message(self, text):
                    msg = QtWidgets.QMessageBox()
                    msg.setText("{}".format(text))
                    msg.exec_()

    def getData(self):
        try:
            txt_name = self.name_lineEdit.text()
            txt_toRecipient = self.toRecipient_lineEdit.text()
            txt_message = self.purpose_lineEdit.text()
            txt_date = self.date_lineEdit.text()
            txt_time = self.time_lineEdit.text()
            txt_concerns = self.concern_lineEdit.text()

            conn = sqlite3.connect('cubixUniversity.db')
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS studentAppointments (
            AppointmentID	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            NameOfStudent	TEXT,
            Recipient	TEXT,
            date	TEXT,
            time	TEXT,
            concern	TEXT,
            purpose	TEXT,
            StudentID	INTEGER,
            FacultyID	INTEGER,
            FOREIGN KEY(StudentID) REFERENCES studentCredentials(ID_Number),
            FOREIGN KEY(FacultyID) REFERENCES facultyCredentials(ID_Number)
            
)""")

            cursor.execute("INSERT INTO studentAppointments (NameOfStudent, Recipient,date, time, concern, purpose) VALUES (?,?,?,?,?,?)",(txt_name,txt_toRecipient, txt_date, txt_time, txt_concerns, txt_message))
            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Added to Database ")

        except:
            self.pop_message("Cannot add to  Database ")

1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboard = QtWidgets.QMainWindow()
    ui = Ui_dashboard()
    ui.setupUi(dashboard)
    dashboard.show()
    sys.exit(app.exec_())
