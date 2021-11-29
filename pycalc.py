import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'
__author__ = 'Joe'

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        # Set the central widget
        self.__centralWidget = QWidget(self)
        self.setCentralWidget(self.__centralWidget)

# Client code
def main():
    """Main function"""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculators GUI
    view = PyCalcUi()
    view.show()
    # Execute calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()