from PyQt5.QtSql import QSqlDatabase
from typing import Union

def createConnection() -> Union[QSqlDatabase, None]:
    db = QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName("127.0.0.1")
    db.setDatabaseName("OOP_finalProject")
    db.setUserName("root")
    db.setPassword("Bry01202004")
    return db