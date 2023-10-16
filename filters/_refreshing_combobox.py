from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import pyqtSignal

class RefreshingComboBox(QComboBox):
    '''
    Кликабельный QCombobox - чтобы ловить сишнал клика
    '''
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)