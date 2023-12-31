# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI's/LogInDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from Message import Ui_MessageForm
from werkzeug.security import check_password_hash
from databaseConn import createConnection
from SessionManager import Session

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(570, 473)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(250, 60))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setMinimumSize(QtCore.QSize(250, 60))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.lineEdit_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.logInClick)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Log In Your Account"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Log In"))
    
    def logInClick(self) -> None:
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if not username or not password:
            msg = "Please Fill all Field"
            code = "Field"
            self.messageError(msg, code)
        else:
            db = createConnection()
            db.open()
            user_data = QSqlQuery()
            statement = "SELECT * FROM users WHERE username = :username"
            user_data.prepare(statement)
            user_data.bindValue(":username", username)
            user_data.exec_()
            user_data.next()
            hash_pass = user_data.value(2)
            if not hash_pass:
                msg = "Account Error!"
                code = "Account"
                self.messageError(msg, code)
            else:
                if check_password_hash(hash_pass, password):
                    session = Session()
                    session.set(username, user_data.value(0), user_data.value(3))
                    self.Dialog.close()
                else:
                    msg = "Can't Find Account!"
                    code = "Account"
                    self.messageError(msg, code)
            db.close()


    def messageError(self, msg: str, code : str) -> None:
        self.log_in_error_ui = QtWidgets.QDialog()
        log_in_error_ui = Ui_MessageForm(msg, code)
        log_in_error_ui.setupUi(self.log_in_error_ui)
        self.log_in_error_ui.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())