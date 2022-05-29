# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabWidget
from .movies_view import MoviesTab
from .games_view import GamesTab
from .music_view import MusicTab


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
    """Container for all the tabs."""

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tabs
        self.tabs = QTabWidget()
        self.moviesTab = MoviesTab(self)
        self.gamesTab = GamesTab(self)
        self.musicTab = MusicTab(self)

        # Add tabs for each media type
        self.tabs.addTab(self.moviesTab, "Movies")
        self.tabs.addTab(self.gamesTab, "Games")
        self.tabs.addTab(self.musicTab, "Music")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
