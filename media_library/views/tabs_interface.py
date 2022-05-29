from PyQt5.QtWidgets import (
    QWidget,
    QDialog,
)


class TabsInterface(QWidget):
    def __init__(self, parent: QWidget) -> None:
        """Initializer."""
        pass

    def openAddDialog(self) -> None:
        """Open the Add Item dialog."""
        pass

    def deleteItem(self) -> None:
        """Delete the selected item from the database."""
        pass

    def clearAllItems(self) -> None:
        """Remove all items from the database."""
        pass

    class AddDialog(QDialog):
        def __init__(self, parent: QWidget) -> None:
            """Initializer."""
            pass

        def setupUI(self) -> None:
            """Setup the Add Item dialog's GUI."""
            pass

        def accept(self) -> None:
            """Accept the data provided through the dialog."""
            pass
