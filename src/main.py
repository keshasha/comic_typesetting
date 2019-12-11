import sys
from PyQt5 import QtWidgets

from mainForm import Form


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
