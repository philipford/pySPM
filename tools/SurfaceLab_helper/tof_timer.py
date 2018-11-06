from win32_helper import *
from timer_display import Ui_ToF_Timer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QTimer
import sys

class GUI_Timer(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_ToF_Timer()
        self.ui.setupUi(self)
        self.timer = QTimer(self);
        self.timer.timeout.connect(self.update)
        self.timer.start(1000);
        
    def update(self):
        ok = False
        A = findWindow("Measurement Progress")
        if len(A)>0:
            B = findWindow(C="Edit", parent=A[0])
            if len(B)>0:
                AnalTime = int(B[2].text.replace(",",""))
                TotScans = int(R[1].text.replace(",",""))
                Scans = int(R[0].text.replace(",",""))
                self.ui.label_2.setText("Scans: {} / {}".format(Scans, TotScans));
                self.ui.label_3.setText("Analysis Time: {} s".format(AnalTime));
                self.ui.progressBar.setValue(Scans);
                self.ui.progressBar.setMaximum(TotScans);
                ok = True
        if not ok:
            self.ui.label.setText("Remaining time: Unavailable (measurement not in progress?)")
            return
        if Scans>0:
            r = AnalTime*(TotScans-Scans)/Scans;
            h = r//3600
            m = (r-h*3600)//60
            s = int(r-h*3600-m*60)
            self.ui.label.setText("Remaining time: {:02d}:{:02d}:{:02d}".format(h,m,s));
        else:
            self.ui.label.setText("Remaining time: Unknown");

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI_Timer()
    window.show()
    sys.exit(app.exec_())