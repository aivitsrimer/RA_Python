import sys

from PySide2.QtWidgets import QApplication

from DesktopApplication.Window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
