import sys
from PySide2.QtWidgets import QApplication, QSlider, QLayout, QWidget, QVBoxLayout
from PySide2.QtGui import QPainter, QPaintEvent, QPen
from PySide2 import QtCore
from PySide2.QtCore import QTimer

class monHorloge (QWidget):
    def __init__ (self, parent=None) :
        super(monHorloge, self).__init__(parent)

        self.setMinimumSize(100,100)

        self.seconde = 0
        self.minute = 0
        self.heure = 0

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.increaseTime)
        self.timer.start()

    def augmentVitesse(self,val):
        self.timer.setInterval(1000/val)
        self.timer.start()

    def increaseTime (self):
        self.seconde+=1
        if self.seconde == 59 :
            self.minute += 1
            self.seconde = 0
            if self.minute == 59 :
                self.heure += 1
                self.minute = 0
                if self.heure == 11 :
                    self.heure =0
        self.update()

    def paintEvent (self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(QtCore.Qt.black)

        taille = min(self.width(), self.height())

        p.drawRect (10, 10, taille-20, taille-20)
        p.setBrush(QtCore.Qt.white)
        p.drawEllipse(20,20,taille-40, taille-40)

        p.save()

        p.translate(taille/2, taille/2)

        p.save()

        p.rotate(270+(self.seconde*360/60))

        pen = QPen(QtCore.Qt.red, 2)
        p.setPen(pen)
        p.drawLine (0,0,(taille-40)/3,0)

        p.restore()

        p.save()

        p.rotate(270+(self.minute*360/60))

        pen = QPen(QtCore.Qt.black, 4)
        p.setPen(pen)
        p.drawLine (0,0,(taille-40)/3,0)

        p.restore()

        p.rotate(270+(self.heure*360/12))

        pen = QPen(QtCore.Qt.blue, 8)
        p.setPen(pen)
        p.drawLine (0,0,(taille-40)/6,0)

        p.restore()
        p.restore()

        pen = QPen(QtCore.Qt.black, 5)
        p.setPen(pen)
        p.setBrush(QtCore.Qt.red)
        p.drawEllipse((taille/2)-20, (taille/2)-20, 40,40)


class maFenetreprincipale(QWidget):
    def __init__(self, parent=None) :
        super(maFenetreprincipale, self).__init__(parent)

        self.compteur = monHorloge()
        self.slider = QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(1,1000)
        self.setMinimumSize(200,200)

        layout = QVBoxLayout()
        layout.addWidget(self.compteur)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.compteur.augmentVitesse)

if __name__ == '__main__' :
    app=QApplication(sys.argv)
    fen = maFenetreprincipale()
    fen.show()
    sys.exit(app.exec_())