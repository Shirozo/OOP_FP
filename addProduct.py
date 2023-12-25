# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI's/AddProduct.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Message import Ui_MessageForm
from databaseConn import createConnection
from signalConnection import SignalConnector
from PyQt5.QtSql import QSqlQuery

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(601, 387)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AddFormTitleContainer = QtWidgets.QWidget(Dialog)
        self.AddFormTitleContainer.setMinimumSize(QtCore.QSize(0, 30))
        self.AddFormTitleContainer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AddFormTitleContainer.setObjectName("AddFormTitleContainer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.AddFormTitleContainer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddFormTitle = QtWidgets.QLabel(self.AddFormTitleContainer)
        self.AddFormTitle.setObjectName("AddFormTitle")
        self.horizontalLayout.addWidget(self.AddFormTitle, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.AddFormTitleContainer)
        self.AddFormLine = QtWidgets.QFrame(Dialog)
        self.AddFormLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.AddFormLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AddFormLine.setObjectName("AddFormLine")
        self.verticalLayout.addWidget(self.AddFormLine)
        self.FormCodeContainer = QtWidgets.QWidget(Dialog)
        self.FormCodeContainer.setObjectName("FormCodeContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FormCodeContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CodeTitle = QtWidgets.QLabel(self.FormCodeContainer)
        self.CodeTitle.setMinimumSize(QtCore.QSize(80, 0))
        self.CodeTitle.setObjectName("CodeTitle")
        self.horizontalLayout_2.addWidget(self.CodeTitle)
        self.CodeField = QtWidgets.QLineEdit(self.FormCodeContainer)
        self.CodeField.setMinimumSize(QtCore.QSize(499, 0))
        self.CodeField.setMaximumSize(QtCore.QSize(499, 16777215))
        self.CodeField.setObjectName("CodeField")
        self.horizontalLayout_2.addWidget(self.CodeField)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.FormCodeContainer)
        self.FormNameContainer = QtWidgets.QWidget(Dialog)
        self.FormNameContainer.setObjectName("FormNameContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FormNameContainer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NameTitle = QtWidgets.QLabel(self.FormNameContainer)
        self.NameTitle.setMinimumSize(QtCore.QSize(80, 0))
        self.NameTitle.setObjectName("NameTitle")
        self.horizontalLayout_3.addWidget(self.NameTitle)
        self.NameField = QtWidgets.QLineEdit(self.FormNameContainer)
        self.NameField.setMinimumSize(QtCore.QSize(499, 0))
        self.NameField.setMaximumSize(QtCore.QSize(499, 16777215))
        self.NameField.setObjectName("NameField")
        self.horizontalLayout_3.addWidget(self.NameField)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.FormNameContainer)
        self.FromQuantityContainer = QtWidgets.QWidget(Dialog)
        self.FromQuantityContainer.setObjectName("FromQuantityContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.FromQuantityContainer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.QuantityTitle = QtWidgets.QLabel(self.FromQuantityContainer)
        self.QuantityTitle.setMinimumSize(QtCore.QSize(80, 0))
        self.QuantityTitle.setObjectName("QuantityTitle")
        self.horizontalLayout_5.addWidget(self.QuantityTitle)
        self.QuantityField = QtWidgets.QSpinBox(self.FromQuantityContainer)
        self.QuantityField.setMinimumSize(QtCore.QSize(150, 0))
        self.QuantityField.setMaximumSize(QtCore.QSize(150, 16777215))
        self.QuantityField.setMinimum(1)
        self.QuantityField.setMaximum(2147483647)
        self.QuantityField.setObjectName("QuantityField")
        self.horizontalLayout_5.addWidget(self.QuantityField, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.FromQuantityContainer)
        self.FormPriceContainer = QtWidgets.QWidget(Dialog)
        self.FormPriceContainer.setObjectName("FormPriceContainer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.FormPriceContainer)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PriceTitle = QtWidgets.QLabel(self.FormPriceContainer)
        self.PriceTitle.setMinimumSize(QtCore.QSize(80, 0))
        self.PriceTitle.setObjectName("PriceTitle")
        self.horizontalLayout_4.addWidget(self.PriceTitle)
        self.PriceField = QtWidgets.QDoubleSpinBox(self.FormPriceContainer)
        self.PriceField.setMinimumSize(QtCore.QSize(150, 0))
        self.PriceField.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PriceField.setMaximum(2147483648.0)
        self.PriceField.setObjectName("PriceField")
        self.horizontalLayout_4.addWidget(self.PriceField)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.FormPriceContainer)
        self.AddFormEndLine = QtWidgets.QFrame(Dialog)
        self.AddFormEndLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.AddFormEndLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AddFormEndLine.setObjectName("AddFormEndLine")
        self.verticalLayout.addWidget(self.AddFormEndLine)
        self.FormButtonContainer = QtWidgets.QWidget(Dialog)
        self.FormButtonContainer.setObjectName("FormButtonContainer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.FormButtonContainer)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.LeftWidgetButtonContainer = QtWidgets.QWidget(self.FormButtonContainer)
        self.LeftWidgetButtonContainer.setObjectName("LeftWidgetButtonContainer")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.LeftWidgetButtonContainer)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.FormCancelButton = QtWidgets.QPushButton(self.LeftWidgetButtonContainer)
        self.FormCancelButton.setObjectName("FormCancelButton")
        self.horizontalLayout_7.addWidget(self.FormCancelButton)
        self.ButtonSpacer = QtWidgets.QFrame(self.LeftWidgetButtonContainer)
        self.ButtonSpacer.setFrameShape(QtWidgets.QFrame.VLine)
        self.ButtonSpacer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ButtonSpacer.setObjectName("ButtonSpacer")
        self.horizontalLayout_7.addWidget(self.ButtonSpacer)
        self.FormAddButton = QtWidgets.QPushButton(self.LeftWidgetButtonContainer)
        self.FormAddButton.setObjectName("FormAddButton")
        self.horizontalLayout_7.addWidget(self.FormAddButton)
        self.horizontalLayout_6.addWidget(self.LeftWidgetButtonContainer, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.FormButtonContainer)

        self.retranslateUi(Dialog)
        self.FormAddButton.clicked.connect(self.AddProduct)
        self.FormCancelButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.signals = SignalConnector()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AddFormTitle.setText(_translate("Dialog", "Add Product"))
        self.CodeTitle.setText(_translate("Dialog", "Code: "))
        self.NameTitle.setText(_translate("Dialog", "Name: "))
        self.QuantityTitle.setText(_translate("Dialog", "Quantity: "))
        self.PriceTitle.setText(_translate("Dialog", "Price: "))
        self.FormCancelButton.setText(_translate("Dialog", "Cancel"))
        self.FormAddButton.setText(_translate("Dialog", "Add"))

    def showError(self, message : str, code : str) -> None:
        """
        Display an error message using a custom QDialog with Ui_MessageForm.

        Parameters:
        - message (str): The error message to be displayed.
        - code (str): The error code associated with the message.

        Usage:
        ```python
        instance_of_your_class.showError("This is an error message.", "E001")
        ```

        This method creates a QDialog window with a custom UI form (Ui_MessageForm) to show an error message along with an associated error code. The method takes two parameters, 'message' and 'code', both of type str.
        """
        self.error = QtWidgets.QDialog()            #Create a QDialog instance
        erorr_ui = Ui_MessageForm(message, code)    #Create a Ui_MessageForm object instance
        erorr_ui.setupUi(self.error)                #Call the setupUi passing the QDialog instance to create the UI
        self.error.exec_()                          #Run the QDialog window
    
    def clear_input(self) -> None:
        """
        Clear input fields and emit a signal indicating that the 'OK' button has been clicked.

        Usage:
        ```python
        instance_of_your_class.clear_input()
        ```

        This method clears the input fields in a user interface, typically used for resetting or clearing form fields. The following fields are affected:

        - `CodeField`: Clears any text entered in the code field.
        - `NameField`: Clears any text entered in the name field.
        - `PriceField`: Resets the value to 0.0.
        - `QuantityField`: Resets the value to 1.

        This method also emits a custom signal named 'clickedOk'. This signal can be connected to perform specific actions when the 'OK' button is clicked.
        """
        self.CodeField.clear()          #Clear the code field
        self.NameField.clear()          #Clear the name field
        self.PriceField.setValue(0.0)   #Reset the value of price field to 0
        self.QuantityField.setValue(1)  #Reset the value of quantity field to 1
        self.signals.clickedOk.emit()   #This will send a signal to main.py to execute setUpTable and re-render the table data
    
    def AddProduct(self):
        """
        Add a new product to the database.

        Usage:
        ```
        instance_of_your_class.AddProduct()
        ```

        This method retrieves product information from input fields, validates the input, and adds a new product to the database. The following steps are performed:

        1. Retrieve values from input fields:
        - `code`: Product code from the 'CodeField' input.
        - `name`: Product name from the 'NameField' input.
        - `price`: Product price from the 'PriceField' input (converted to float).
        - `quantity`: Product quantity from the 'QuantityField' input (converted to int).

        2. Validate the input:
        - Ensure that both product code and name are provided. If not, display an error message.

        3. Connect to the database:
        - Create a database connection using the `createConnection` function.

        4. Insert the new product into the 'products' table:
        - Prepare an SQL statement for insertion.
        - Bind values to the prepared statement.
        - Execute the query.

        5. Handle the result:
        - If the query execution fails, display an error message with details.
        - If successful, close the database connection, display a success message, and clear input fields.
        """

        code = self.CodeField.text().strip()        #Get the value of code field removing all the whitespace
        name = self.NameField.text().strip()        #Get the value of name field removing all the whitespace
        price = float(self.PriceField.text())       #Get the value of price field
        quantity = int(self.QuantityField.text())   #Get the value of quantity field

        if not code or not name:                        #If the code or name is empty, Then
            if not code:                                    #If no code, Then
                message = "Product Code is Required!"           #Set the message that the code is required
            else:                                           #If the code exist, Then
                message = "Product Name is Required!"           #Set the message that the name is required
            message_code = "Erorr"                          #Set the message code to error
        else:                                           #If name and code both exist, then
            db = createConnection()                         #Create a database connection
            if not db:                                      #If can't connect to database, then
                message = "Database Close"                      #Set the message telling that the database is close
                message_code = "Erorr"                          #Set the message code to error
            try:                                        #Handle any error
                db.open()                                   #Open database connection
                query = QSqlQuery()                         #Create a QSqlQuery object instance
                statement = """INSERT INTO products (       
                    code, name, price, quantity) 
                    VALUES (:code, :name, :price, :quantity)
                """                                         #Set your SQL query
                query.prepare(statement)                    #Prepare the SQL query for value binding
                
                query.bindValue(":code", code)              #Bind the code value to SQL statement
                query.bindValue(":name", name)              #Bind the name value to SQL statement
                query.bindValue(":price", price)            #Bind the price value to SQL statement
                query.bindValue(":quantity", quantity)      #Bind the quantity value to SQL statement

                status = query.exec_()                      #Execute the query
                if not status:                              #If the query fails, then
                    erorr = query.lastError().text()            #Extract the error
                    message = f"{erorr[:14]}...."               #Set the message to the 14 character of error
                    message_code = "Error"                      #Set the code to Error 
                else:                                       #If the query succedd, then
                    message = "Product Added"                   #Message the user that the product is added
                    message_code = "Success"                    #Set the message code to Success
                    self.clear_input()                          #Clear all the fields
            except Exception as e:                      #If an error happens, then
                message = f"{e[:14]}..."                    #Set tht message to whatever the error is                               
                message_code = "Erorr"                      #Set the message code to error

        db.close()                                   #Close the connectiom to the database
        self.showError(message, message_code)           #Show message Dialog


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
