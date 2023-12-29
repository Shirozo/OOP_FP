# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI's/Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from addProduct import Ui_Dialog
from PyQt5.QtSql import QSqlQuery
from confirmation import Ui_ConfirmDialog
from databaseConn import createConnection
from functools import partial
import sys

class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.id_to_row = {}

    def showAddWidget(self):
        self.add_form = QtWidgets.QDialog()
        add_form_ui = Ui_Dialog()
        add_form_ui.setupUi(self.add_form)
        add_form_ui.signals.clickedOk.connect(self.setUpTable)
        add_form_ui.FormAddButton.clicked.connect(lambda: add_form_ui.AddProduct())
        self.add_form.exec_()
    
    def handleUpdater(self):
        print("Hello world")
 
    def removeTableEntry(self, id : int) -> None:
        found = False
        for i in list(self.id_to_row.keys()):
            if i == id:
                row = self.id_to_row[i]
                print(row)
                self.tableWidget.removeRow(row)
                del self.id_to_row[i]
                found = True
                continue
            if found:
                self.id_to_row[i] = int(self.id_to_row[i]) - 1

    def showHandleRemove(self, id_rem : int) -> None:
        self.remover_form = QtWidgets.QDialog()
        remover_form_ui = Ui_ConfirmDialog()
        remover_form_ui.setupUi(self.remover_form)
        remover_form_ui.signal.clickedOk.connect(lambda:self.removeTableEntry(id_rem))
        remover_form_ui.ConfirmYesButton.clicked.connect(partial(remover_form_ui.removeEntry, id_rem))
        self.remover_form.exec_()
        
    
    def setUpTable(self) -> None:
        self.id_to_row = {}
        db = createConnection()
        db.open()
        query = QSqlQuery("SELECT * FROM products ORDER BY code")
        number_of_column = query.record().count()
        row = 0
        while query.next():
            current_count = self.tableWidget.rowCount()
            if row >=  current_count:
                self.tableWidget.insertRow(row)
            current_id = query.value(0)
            for col in range(1, number_of_column):
                item = QtWidgets.QTableWidgetItem(str(query.value(col)))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.tableWidget.setItem(row, col-1, item)

            self.id_to_row[current_id] = row
            
            widget = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout(widget)

            button = QtWidgets.QPushButton("Delete")
            button.setMaximumSize(88, 16777215)
            button.clicked.connect(partial(self.showHandleRemove, current_id))
            button_layout.addWidget(button)

            button2 = QtWidgets.QPushButton("Update")
            button2.setMaximumSize(88, 16777215)
            button2.clicked.connect(self.handleUpdater)
            button_layout.addWidget(button2)

            self.tableWidget.setCellWidget(row, col, widget )
            self.tableWidget.setRowHeight(row, 40)

            row += 1
        db.close()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_3 = QtWidgets.QFrame(self.widget_7)
        self.line_3.setMinimumSize(QtCore.QSize(0, 30))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.label = QtWidgets.QLabel(self.widget_7)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout.addWidget(self.widget_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.widget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 34))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.widget_4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.showAddWidget) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setUpTable()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "asdasd"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Search"))
        self.tableWidget.setSortingEnabled(True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Action"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
