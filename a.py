import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction

class window(QMainWindow):
    def __init__(self):

        super().__init__()

    def createUI(self):


        self.setGeometry(500, 300, 700, 700)

        self.setWindowTitle("window")


        quit = QAction("Quit", self)
        quit.triggered.connect(self.exit_window)

        menubar = self.menuBar()
        fmenu = menubar.addMenu("File")
        fmenu.addAction(quit)

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def exit_window(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                            "QUIT?",
                                            "Are you sure want to STOP and EXIT?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            # event.accept()
            sys.exit()
        else:
            pass


main = QApplication(sys.argv)
window = window()
window.createUI()
window.show()
sys.exit(main.exec_())