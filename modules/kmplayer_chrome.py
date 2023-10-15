from PyQt5.QtWidgets import QFileDialog
from modules.api import conf, load_key_to_api
import os
from filters._kmplayer_to_google import kmplayer_to_google
from filters._CHECKER_kmplayer import checker_kmplayer


class KMPlayerToChrome:
    '''
    Выбираем между Kmplayer и Chrome
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.radioButton_kmplayer.toggled.connect(self.radio_selected)
        self.mw.radioButton_google.toggled.connect(self.radio_selected)
        checker_kmplayer(self.mw)
        

    def radio_selected(self):
        radio_btn = self.mw.sender()
        if radio_btn.isChecked():
            kmplayer_to_google(self.mw, radio_btn.text())
