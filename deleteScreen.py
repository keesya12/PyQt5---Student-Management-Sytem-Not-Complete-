from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_deleteDialog(object):
    def setupUi(self, deleteDialog):
        deleteDialog.setObjectName("deleteDialog")
        deleteDialog.resize(300, 150)
        deleteDialog.setStyleSheet("background-color: rgb(75, 103, 118);")
        self.lineEdit = QtWidgets.QLineEdit(deleteDialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 200, 31))
        self.lineEdit.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell\";\n"
"border-bottom: 1px solid white;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.deleteBtn = QtWidgets.QPushButton(deleteDialog)
        self.deleteBtn.setGeometry(QtCore.QRect(40, 100, 81, 31))
        self.deleteBtn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.329727, y1:0.432, x2:0.938, y2:0.619318, stop:0.215909 rgba(162, 223, 176, 255), stop:0.698864 rgba(200, 255, 255, 255));\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.deleteBtn.setObjectName("deleteBtn")
        self.deleteBtn.clicked.connect(self.deletion)
        self.cancelbtn = QtWidgets.QPushButton(deleteDialog)
        self.cancelbtn.setGeometry(QtCore.QRect(160, 100, 81, 31))
        self.cancelbtn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.329727, y1:0.432, x2:0.938, y2:0.619318, stop:0.215909 rgba(162, 223, 176, 255), stop:0.698864 rgba(200, 255, 255, 255));\n"
"font: 14pt \"Rockwell\";\n"
"border-radius: 10px;")
        self.cancelbtn.setObjectName("cancelbtn")
        self.label = QtWidgets.QLabel(deleteDialog)
        self.label.setGeometry(QtCore.QRect(85, 20, 131, 20))
        self.label.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(deleteDialog)
        QtCore.QMetaObject.connectSlotsByName(deleteDialog)

    def retranslateUi(self, deleteDialog):
        _translate = QtCore.QCoreApplication.translate
        deleteDialog.setWindowTitle(_translate("deleteDialog", "Delete"))
        self.lineEdit.setPlaceholderText(_translate("deleteDialog", "Enter your ID Number"))
        self.deleteBtn.setText(_translate("deleteDialog", "Delete"))
        self.cancelbtn.setText(_translate("deleteDialog", "Cancel"))
        self.label.setText(_translate("deleteDialog", "Enter ID Number"))

    def pop_message(self, text):
                    msg = QtWidgets.QMessageBox()
                    msg.setText("{}".format(text))
                    msg.exec_()

    def deletion(self):
        try:
            delID = self.lineEdit.text()


            conn = sqlite3.connect('cubixUniversity.db')
            cursor = conn.cursor()
            cursor.execute()

            cursor.execute("""SELECT * FROM studentCredentials""")

            cursor.execute("DELETE FROM studentCredentials WHERE ID_Number =?",(delID,))

            conn.commit()

            conn.close()
            self.pop_message("Record Deleted.")
        except:
            self.pop_message("Record is not deleted ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteDialog = QtWidgets.QDialog()
    ui = Ui_deleteDialog()
    ui.setupUi(deleteDialog)
    deleteDialog.show()
    sys.exit(app.exec_())
