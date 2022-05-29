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

from ..models.games_model import GamesModel
from .tabs_interface import TabsInterface

class GamesTab(TabsInterface):
    def __init__(self, parent):
        """Implements TabsInterface.__init__() for Games."""
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()

        # Create the table view widget
        self.table = QTableView()
        self.gamesModel = GamesModel()
        self.table.setModel(self.gamesModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Create the buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteItem)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearItems)

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
        """Implements TabsInterface.openAddDialog() for Games."""
        dialog = self.AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.gamesModel.addItem(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteItem(self):
        """Implements TabsInterface.deleteItem() for Games."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        title = self.table.model().data(self.table.model().index(row, 1))
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            f"Do you want to remove the '{title}' game?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.gamesModel.deleteItem(row)

    def clearItems(self):
        """Implements TabsInterface.clearItems() for Games."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your games?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.gamesModel.clearItems()
    

    class AddDialog(QDialog):
        def __init__(self, parent=None):
            """Implements TabsInterface.AddDialog.__init__() for Games"""
            super().__init__(parent=parent)
            self.setWindowTitle("Add Game")
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            self.data = None

            self.setupUI()

        def setupUI(self):
            """Implements TabsInterface.AddDialog.setupUI() for Games"""
            # Create line edits for data fields
            self.titleField = QLineEdit()
            self.titleField.setObjectName("Title")
            self.yearField = QLineEdit()
            self.yearField.setObjectName("Year")
            self.genreField = QLineEdit()
            self.genreField.setObjectName("Genre")
            self.creatorField = QLineEdit()
            self.creatorField.setObjectName("Creator")
            self.studioField = QLineEdit()
            self.studioField.setObjectName("Studio")
            # Lay out the data fields
            layout = QFormLayout()
            layout.addRow("Title:", self.titleField)
            layout.addRow("Year:", self.yearField)
            layout.addRow("Genre:", self.genreField)
            layout.addRow("Creator:", self.creatorField)
            layout.addRow("Studio:", self.studioField)
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
            """Implements TabsInterface.AddDialog.accept() for Games"""
            self.data = []
            for field in (self.titleField, self.yearField, self.genreField, self.creatorField, self.studioField):
                if field.objectName() == "Title" and not field.text():
                    QMessageBox.critical(
                        self,
                        "Error!",
                        f"You must provide a games's {field.objectName()}",
                    )
                    self.data = None  # Reset .data
                    return

                self.data.append(field.text())

            if not self.data:
                return

            super().accept()