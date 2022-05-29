# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from .views.main_view import Window
from .database import createConnection


def main():
    # Create the application
    app = QApplication(sys.argv)

    # Connect to the database before creating any window
    if not createConnection("media.sqlite"):
        sys.exit(1)

    # Create the main window
    win = Window()
    win.show()

    # Run the event loop
    sys.exit(app.exec())
