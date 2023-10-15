from PyQt5.QtWidgets import QFileDialog, QMessageBox
from modules.api import conf, load_key_to_api
import os
from PyQt5.QtWidgets import QComboBox
import pygetwindow as gw
from PyQt5.QtCore import Qt


class DopSelect:
    '''
    Выбор всех вкладок
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.get_tabs()
        self.mw.comboBox_doptab.view().viewport().mousePressEvent = self.handle_combo_box_click
        self.mw.comboBox_doptab.activated.connect(self.handle_combo_box_activation)

    def get_tabs(self):
        a = [i for i in gw.getAllTitles() if i != '']
        for i in range(len(a)):
            self.mw.comboBox_doptab.addItem(a[i])
            
    def handle_combo_box_click(self, event):
        # Slot function called when the combobox is clicked
        if event.button() == Qt.LeftButton:
            print("Combo box clicked before item selection")
        super(QComboBox, self.mw.comboBox_doptab).mousePressEvent(event)
        
    def handle_combo_box_activation(self, index):
        # Slot function called when the combobox item is activated (clicked)
        selected_item = self.mw.comboBox_doptab.currentText()
        print(f"Selected item: {selected_item}")
        # Add your code here to refresh data based on the selected item
            
    def clicked(self):
        print('asd')
