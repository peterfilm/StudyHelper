from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal()  # Custom click signal

    def mousePressEvent(self, event):
        # Emit the custom click signal when the label is clicked
        self.clicked.emit()
        super().mousePressEvent(event)