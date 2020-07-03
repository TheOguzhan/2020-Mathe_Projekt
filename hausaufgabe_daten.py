#Das sind Bibliotheken. Wir bracuhen sie, um zu programmieren
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from hausaufgabe_übersetzer import Übersetzer
#Das ist ein Class, das das Diagramm macht und zeigt.
class Diagramm_Zeiger():
    #Die Funktion arbeitet, wenn wir Class deklarieren
    def __init__(self,datei_name:str,wahle:list,lande:list):
        #Wir bekommen Daten, die wir brauchen.
        self.datei_name = datei_name
        self.wahle = wahle
        self.lande = lande
        self.daten = pd.read_csv(datei_name)
        #Pandas Bibliothek liest Datei
    #Die Funktion bringt die Daten, die wir brauchen, in Form.
    def _daten_trenner_(self):
        daten = self.daten
        daten = daten.set_index("Date")
        daten["Active Case"] = daten["Confirmed"]-daten["Recovered"]-daten["Deaths"]
        land_wörterbuch = dict()
        for land in daten.groupby("Country"):
            land_wörterbuch[land[0]] = land[1]
        lande = set()
        for land in daten["Country"]:
            lande.add(land)
        lande = list(lande)
        lande = sorted(lande)
        lande[lande.index("Taiwan*")] = "Taiwan"
        return land_wörterbuch
    #Die Funktion zeigt uns das Diagramm.
    def zeig_liniendiagramm_diagramm(self):
        #Zieht das Diagramm
        diagramm = plt
        style.use("ggplot")
        diagramm.rc("font",size=8)
        land_wörterbuch = self._daten_trenner_()
        übersetzer=Übersetzer()
        for land in self.lande:
            for wahl in self.wahle:
                land_wörterbuch[land][wahl].plot(label="{}-{}".format(land,wahl))
        schrift="Genesene in/im/in der"
        for land in self.lande:
            schrift += land
        diagramm.legend(loc=2)
        diagramm.xlabel("Geschehnis")
        diagramm.ylabel("Datum")
        #Zeigt Diagramm
        diagramm.show()