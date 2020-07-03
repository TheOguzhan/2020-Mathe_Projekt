from PyQt5.QtWidgets import QWidget,QApplication
from hausaufgabe_bildschrim import Bildschrim
import sys
if __name__=="__main__":
    app = QApplication(sys.argv)
    bildschrim = Bildschrim()
    sys.exit(app.exec_())