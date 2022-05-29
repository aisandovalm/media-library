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

from ..models.music_model import MusicModel
from .tabs_interface import TabsInterface

class MusicTab(TabsInterface):
    def __init__(self, parent):
        """Implements TabsInterface.__init__() for Music."""
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()

        # Create the table view widget
        self.table = QTableView()
        self.musicModel = MusicModel()
        self.table.setModel(self.musicModel.model)
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
        """Implements TabsInterface.openAddDialog() for Music."""
        dialog = self.AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.musicModel.addItem(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteItem(self):
        """Implements TabsInterface.deleteItem() for Music."""
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
            self.musicModel.deleteItem(row)

    def clearItems(self):
        """Implements TabsInterface.clearItems() for Music."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your music?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.musicModel.clearItems()
    

    class AddDialog(QDialog):
        def __init__(self, parent=None):
            """Implements TabsInterface.AddDialog.__init__() for Music"""
            super().__init__(parent=parent)
            self.setWindowTitle("Add Game")
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            self.data = None

            self.setupUI()

        def setupUI(self):
            """Implements TabsInterface.AddDialog.setupUI() for Music"""
            # Create line edits for data fields
            self.titleField = QLineEdit()
            self.titleField.setObjectName("Title")
            self.artistField = QLineEdit()
            self.artistField.setObjectName("Artist")
            self.albumField = QLineEdit()
            self.albumField.setObjectName("Album")
            self.yearField = QLineEdit()
            self.yearField.setObjectName("Year")
            self.genreField = QLineEdit()
            self.genreField.setObjectName("Genre")
            # Lay out the data fields
            layout = QFormLayout()
            layout.addRow("Title:", self.titleField)
            layout.addRow("Artist:", self.artistField)
            layout.addRow("Album:", self.albumField)
            layout.addRow("Year:", self.yearField)
            layout.addRow("Genre:", self.genreField)
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
            """Implements TabsInterface.AddDialog.accept() for Music"""
            self.data = []
            for field in (self.titleField, self.artistField, self.albumField, self.yearField, self.genreField):
                if field.objectName() in ["Title", "Artist"] and not field.text():
                    QMessageBox.critical(
                        self,
                        "Error!",
                        f"You must provide a music's {field.objectName()}",
                    )
                    self.data = None  # Reset .data
                    return

                self.data.append(field.text())

            if not self.data:
                return

            super().accept()