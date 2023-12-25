from PyQt5.QtCore import QObject, pyqtSignal

class SignalConnector(QObject):
    clickedOk = pyqtSignal()