from PyQt5.QtCore import QObject, pyqtSignal

class SignalConnector(QObject):
    """
    Singal connector from one UI to another UI
    """
    clickedOk = pyqtSignal()