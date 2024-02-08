from PyQt6.QtWidgets import QWidget, QGridLayout
from UebungChart import UebungChart
from DatumChart import DatumChart

class CentralWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Charts ins CentralWidget hinzufügen
        self.uebungchart = UebungChart(parent)
        self.datumchart = DatumChart(parent)

        #Layout für das CentralWidget
        layout = QGridLayout()

        layout.addWidget(self.uebungchart)
        layout.addWidget(self.datumchart)

        self.setLayout(layout)