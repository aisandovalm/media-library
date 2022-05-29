# -*- coding: utf-8 -*-

"""This module defines the interface for the models."""

class ModelInterface:
    def __init__(self) -> None:
        """Initializer."""
        pass

    @staticmethod
    def _createModel() -> None:
        """Create and set up the model."""
        pass

    def addItem(self, data) -> None:
        """Add a item to the database."""
        pass

    def deleteItem(self, row) -> None:
        """Remove a item from the database."""
        pass

    def clearItems(self) -> None:
        """Remove all item in the database."""
        pass
