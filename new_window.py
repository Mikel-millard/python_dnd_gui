# Imports
import sys
from PyQt5.QtWidgets import QWidget, QApplication


# Creates a new window to open with buttons
class NewWindow(QWidget):
    def __init__(self):
        super(NewWindow, self).__init__()
        self._new_window = None


# Main method
def main():
    app = QApplication(sys.argv)
    gui = NewWindow()
    gui.show()
    sys.exit(app.exec_())


# Runs the main method when it is the correct time to
if __name__ == '__main__':
    main()
