from PyQt5.QtSql import QSqlDatabase
from typing import Union

def createConnection() -> Union[QSqlDatabase, None]:
    """
    Create and return a connection to the MySQL database.

    Returns:
    - QSqlDatabase: A connection to the MySQL database.
    - None: If the connection cannot be established.

    Usage:
    ```python
    connection = createConnection()
    if connection:
        # Perform database operations using the 'connection' object
    else:
        # Handle connection failure
    ```
    This function creates a connection to a MySQL database using the PyQt5.QtSql module. The connection parameters (hostname, database name, username, and password) are set within the function.
    """

    db = QSqlDatabase.addDatabase("QMYSQL")     #Add database engine
    db.setHostName("127.0.0.1")                 #Set the host
    db.setDatabaseName("OOP_finalProject")      #Set the database you want to use
    db.setUserName("root")                      #Set the username
    db.setPassword("Bry01202004")               #Set the password
    return db                                   #Return the database