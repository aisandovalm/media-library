# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTabWidget
)

from PyQt5.QtCore import pyqtSlot
from .movies_view import MoviesTab
from .games_view import GamesTab

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Media Library")
        self.resize(720, 360)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.moviesTab = MoviesTab(self)
        self.gamesTab = GamesTab(self)
        self.tab3 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs for each media type
        self.tabs.addTab(self.moviesTab,"Movies")
        self.tabs.addTab(self.gamesTab,"Games")
        self.tabs.addTab(self.tab3,"Music")
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
