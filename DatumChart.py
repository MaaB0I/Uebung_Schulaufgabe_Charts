from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen

class DatumChart(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Chart Linien erstellen
        self.series = QLineSeries()
        self.series2 = QLineSeries()
        self.series.setName("Series")
        self.series2.setName("Series2")

        #Farbe für die Chart Line ändern
        #pen = QPen(QColor(144, 238, 144))
        #pen.setWidth(5)
        #self.series.setPen(pen)

        #Andere Methode Chart Line Farbe ändern
        self.series.setColor(QColor("red"))
        self.series2.setColor(QColor("yellow"))


        #Chart erstellen und Linien hinzufügen
        self.chart = QChart()
        self.chart.setTitle("2te Chart")
        self.chart.setTitleBrush(QColor("green"))
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)

        #Achsen erstellen und Range eingeben
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)



        #Datum x-Achse erstellen
        axis_x = QDateTimeAxis()
        axis_x.setTickCount(10)  # Anzahl der Datenpunkte (Tage)
        axis_x.setFormat("dd.MM")  # Format des Datums
        axis_x.setTitleText("Datum")
        axis_x.setTitleBrush(QColor("green"))

        #Start Datum
        start_date = QDateTime.currentDateTime()
        #End Datum
        end_date = QDateTime.currentDateTime().addDays(-9)
        axis_x.setRange(end_date, start_date)

        #Achsen Label Farbe ändern
        axis_x.setLabelsColor(QColor("green"))
        axis_y.setLabelsColor(QColor("white"))

        #Gitter Farbe ändern
        pen_grid = QPen(QColor("yellow"))
        axis_x.setGridLinePen(pen_grid)
        axis_y.setGridLineColor(QColor("blue"))


        #Achsen zum Chart hinzufügen
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        self.series2.attachAxis(axis_x)
        self.series2.attachAxis(axis_y)

        #Werte für das Datum hinzufügen
        self.series.append(QDateTime.currentDateTime().addDays(-9).toMSecsSinceEpoch(), 1)
        self.series.append(QDateTime.currentDateTime().addDays(-8).toMSecsSinceEpoch(), 2)
        self.series.append(QDateTime.currentDateTime().addDays(-7).toMSecsSinceEpoch(), 3)
        self.series.append(QDateTime.currentDateTime().addDays(-6).toMSecsSinceEpoch(), 4)



        #Werte für das 2te Datum hinzufügen
        self.series2.append(QDateTime.currentDateTime().addDays(-9).toMSecsSinceEpoch(), 4)
        self.series2.append(QDateTime.currentDateTime().addDays(-8).toMSecsSinceEpoch(), 5)
        self.series2.append(QDateTime.currentDateTime().addDays(-7).toMSecsSinceEpoch(), 6)
        self.series2.append(QDateTime.currentDateTime().addDays(-6).toMSecsSinceEpoch(), 7)


        #Hintergrundfarbe hinzugefügt
        self.chart.setBackgroundBrush(QColor("black"))

        #Chart anzeigen
        self.setChart(self.chart)
