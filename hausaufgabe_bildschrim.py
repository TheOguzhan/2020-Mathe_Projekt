import sys
from hausaufgabe_übersetzer import Übersetzer
from hausaufgabe_daten import Diagramm_Zeiger
import pandas as pd
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QCheckBox,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog
#Das ist Class des Bildschrims
class Bildschrim(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textArea = QTextEdit()
        self.textAreaLabel = QLabel("Schreiben Sie bitte, die Landen. Zwischen die Landen muss , (Kommas) sein.")
        self.checkBoxTod = QCheckBox("Tod")
        self.checkBoxGenesene = QCheckBox("Genesene")
        self.checkBoxBestätigt = QCheckBox("Bestätigt")
        self.button = QPushButton("Zeig")

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.checkBoxBestätigt)
        self.h_box.addWidget(self.checkBoxGenesene)
        self.h_box.addWidget(self.checkBoxTod)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.textAreaLabel)    
        self.v_box.addWidget(self.textArea)
        self.v_box.addWidget(self.button)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box)
        self.setWindowTitle("Landen")
        self.button.clicked.connect(self._zeig_)
        self.show()
    def _zeig_(self):
        übersetzer = Übersetzer()
        wörterbuch = {"Genesene":"Recovered","Bestätigt":"Confirmed","Tod":"Deaths"}
        wahl_liste = list()
        lande = self.textArea.toPlainText().split(",")
        lande2 = list()
        checkListe = [self.checkBoxBestätigt,self.checkBoxGenesene,self.checkBoxTod]
        for checkBox in checkListe:
            if checkBox.isChecked():
                wahl_liste.append(wörterbuch[checkBox.text()])
        for land in lande:
            lande2.append(übersetzer.übersetzen_deutsch_in_englisch(land).title())
        diagramm_zeiger = Diagramm_Zeiger("dataset.csv",wahl_liste,lande2)
        try:
            diagramm_zeiger.zeig_liniendiagramm_diagramm()
        except KeyError:
            lande2 = list()
            self.textAreaLabel.setText("Schreiben Sie Bitte ordentlich")
if __name__=="__main__":
    app = QApplication(sys.argv)
    bildschrim = Bildschrim()
    sys.exit(app.exec_())