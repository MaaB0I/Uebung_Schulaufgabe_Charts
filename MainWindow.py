from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #CentralWidget ins MainWindow
        self.central_widget = CentralWidget(parent)
        self.setCentralWidget(self.central_widget)

        #Größe des Windows
        #self.setFixedSize(1000, 1500)

        #Titel des Windows
        self.setWindowTitle("Chart Indiana")
