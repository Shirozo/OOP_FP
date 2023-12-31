from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore, QtWidgets

class SignalConnector(QObject):
    """
    Singal connector from one UI to another UI
    """
    clickedOk = pyqtSignal()