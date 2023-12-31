from databaseConn import createConnection
from werkzeug.security import generate_password_hash
from PyQt5.QtSql import QSqlQuery

username = input("Username: ")
password = input("Passsword: ")
hash_pass = generate_password_hash(password)

user_type = 1
db = createConnection()
db.open()
query = QSqlQuery()
statement = "INSERT INTO users (username, password, type) VALUES (:username, :password, :type)"
query.prepare(statement)
query.bindValue(":username", username)
query.bindValue(":password", hash_pass)
query.bindValue(":type", user_type)
status = query.exec_()
if status:
    print("Account Created!")
else:
    print(query.lastError().text())
db.close()
