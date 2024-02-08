from turtle import color

from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen


class UebungChart(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Hintergrund Bild setzen
        self.background_image = QPixmap("venv/Pictures/placeholder-1-1.png")
        self.background_image = self.background_image.scaled(1200, 600)

        #Chart Linien erstellen
        self.series = QLineSeries()
        self.series.setName("Series")

        #Farbe für die Chart Line ändern
        pen = QPen(QColor(144, 238, 144))
        pen.setWidth(5)
        self.series.setPen(pen)

        #Andere Methode Chart Line Farbe ändern
        #self.series.setColor(QColor("blue"))


        #Chart erstellen und Linien hinzufügen
        self.chart = QChart()
        self.chart.setTitle("Karte")
        self.chart.addSeries(self.series)

        #Achsen erstellen und Range eingeben
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)
        axis_x = QValueAxis()
        axis_x.setRange(0, 10)

        #Achsen zum Chart hinzufügen
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        #Werte für den Chart hinzufügen
        self.series.append(1,1)
        self.series.append(2, 2)
        self.series.append(3, 3)
        self.series.append(4,4)

        #Bild sichtbar stellen
        self.chart.setBackgroundVisible(True)
        self.chart.setBackgroundBrush(QBrush(self.background_image))

        #Chart anzeigen
        self.setChart(self.chart)
