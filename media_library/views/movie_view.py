# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from ..models.movie_model import MoviesModel
from .tabs_interface import TabsInterface

class MoviesTab(TabsInterface):
    def __init__(self, parent):
        """Implements TabsInterface.__init__() for Movies."""
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()

        # Create the table view widget
        self.table = QTableView()
        self.moviesModel = MoviesModel()
        self.table.setModel(self.moviesModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Create the buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteItem)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearAllItems)

        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
        self.setLayout(self.layout)

    def openAddDialog(self):
        """Implements TabsInterface.openAddDialog() for Movies."""
        dialog = self.AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.moviesModel.addMovie(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteItem(self):
        """Implements TabsInterface.deleteItem() for Movies."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected movie?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.moviesModel.deleteItem(row)

    def clearAllItems(self):
        """Implements TabsInterface.clearAllItems() for Movies."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your movies?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.moviesModel.clearAllItems()
    

    class AddDialog(QDialog):
        def __init__(self, parent=None):
            """Implements TabsInterface.AddDialog.__init__() for Movies"""
            super().__init__(parent=parent)
            self.setWindowTitle("Add Movie")
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            self.data = None

            self.setupUI()

        def setupUI(self):
            """Implements TabsInterface.AddDialog.setupUI() for Movies"""
            # Create line edits for data fields
            self.titleField = QLineEdit()
            self.titleField.setObjectName("Title")
            self.yearField = QLineEdit()
            self.yearField.setObjectName("Year")
            self.directorField = QLineEdit()
            self.directorField.setObjectName("Director")
            self.genreField = QLineEdit()
            self.genreField.setObjectName("Genre")
            self.writerField = QLineEdit()
            self.writerField.setObjectName("Writer")
            # Lay out the data fields
            layout = QFormLayout()
            layout.addRow("Title:", self.titleField)
            layout.addRow("Year:", self.yearField)
            layout.addRow("Director:", self.directorField)
            layout.addRow("Genre:", self.genreField)
            layout.addRow("Writer:", self.writerField)
            self.layout.addLayout(layout)
            # Add standard buttons to the dialog and connect them
            self.buttonsBox = QDialogButtonBox(self)
            self.buttonsBox.setOrientation(Qt.Horizontal)
            self.buttonsBox.setStandardButtons(
                QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )
            self.buttonsBox.accepted.connect(self.accept)
            self.buttonsBox.rejected.connect(self.reject)
            self.layout.addWidget(self.buttonsBox)

        def accept(self):
            """Implements TabsInterface.AddDialog.accept() for Movies"""
            self.data = []
            for field in (self.titleField):
                if not field.text():
                    QMessageBox.critical(
                        self,
                        "Error!",
                        f"You must provide a movies's {field.objectName()}",
                    )
                    self.data = None  # Reset .data
                    return

                self.data.append(field.text())

            if not self.data:
                return

            super().accept()