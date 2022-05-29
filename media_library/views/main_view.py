# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    QTabWidget
)

from PyQt5.QtCore import pyqtSlot
from ..models.movie_model import MoviesModel
from .movie_view import MoviesTab

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Media Library")
        self.resize(550, 250)
        #self.centralWidget = QWidget()
        #self.setCentralWidget(self.centralWidget)
        #self.layout = QHBoxLayout()
        #self.centralWidget.setLayout(self.layout)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        #self.movieTab = QWidget()
        self.movieTab = MoviesTab(self)
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs for each media type
        self.tabs.addTab(self.movieTab,"Movies")
        self.tabs.addTab(self.tab2,"Games")
        self.tabs.addTab(self.tab3,"Music")

        '''# Create second tab
        self.movieTab.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.movieTab.layout.addWidget(self.pushButton1)
        self.movieTab.setLayout(self.movieTab.layout)

        # Create third tab
        self.movieTab.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.movieTab.layout.addWidget(self.pushButton1)
        self.movieTab.setLayout(self.movieTab.layout)'''
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
