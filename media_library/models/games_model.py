# -*- coding: utf-8 -*-

"""This module provides a model to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

from .models_interface import ModelInterface

class GamesModel(ModelInterface):
    def __init__(self):
        """Implements ModelInterface.__init__() for Games."""
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Implements ModelInterface._createModel() for Games."""
        tableModel = QSqlTableModel()
        tableModel.setTable("games")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Title", "Year", "Genre", "Creator", "Studio")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addItem(self, data):
        """Implements ModelInterface.addItem() for Games."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()

    def deleteItem(self, row):
        """Implements ModelInterface.deleteItem() for Games."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearItems(self):
        """Implements ModelInterface.clearItems() for Games."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
