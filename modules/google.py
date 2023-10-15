from PyQt5.QtWidgets import QFileDialog, QMessageBox
from modules.api import conf, load_key_to_api
import os
import pygetwindow as gw


class GoogleSelect:
    '''
    Выбор вкладок гугл хром
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.google_window = None
        self.get_tabs()

    def get_tabs(self):
        a = [i.split(' - Google Chrome')[0] for i in gw.getAllTitles() if 'Google Chrome' in i]
        for i in a:
            self.mw.comboBox_chrome.addItem(i)
            self.mw.comboBox_chrome.setItemData(0, {i: gw.getWindowsWithTitle(i)})
        if self.google_window != None:
            self.mw.comboBox_chrome.setCurrentText(self.google_window)
        
