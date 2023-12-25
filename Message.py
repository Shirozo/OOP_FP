from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_MessageForm(object):
    def __init__(self, message : str, code : str) -> None:
        self.message = message
        self.code = code

    def setupUi(self, MessageForm):
        MessageForm.setObjectName("MessageForm")
        MessageForm.setFixedSize(318, 116)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MessageForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MessageWidget = QtWidgets.QWidget(MessageForm)
        self.MessageWidget.setObjectName("MessageWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MessageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Message = QtWidgets.QLabel(self.MessageWidget)
        self.Message.setObjectName("Message")
        self.verticalLayout.addWidget(self.Message, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget = QtWidgets.QWidget(self.MessageWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.ExitMessage = QtWidgets.QPushButton(self.widget)
        self.ExitMessage.setObjectName("ExitMessage")
        self.verticalLayout_2.addWidget(self.ExitMessage, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.MessageWidget)
        
        self.retranslateUi(MessageForm)
        self.ExitMessage.clicked.connect(MessageForm.close)
        QtCore.QMetaObject.connectSlotsByName(MessageForm)
        

    def retranslateUi(self, MessageForm):
        _translate = QtCore.QCoreApplication.translate
        MessageForm.setWindowTitle(_translate("MessageForm", self.code))
        self.Message.setText(_translate("MessageForm", self.message))
        self.ExitMessage.setText(_translate("MessageForm", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageForm = QtWidgets.QDialog()
    ui = Ui_MessageForm("Hello world", "try")
    ui.setupUi(MessageForm)
    MessageForm.show()
    sys.exit(app.exec_())
