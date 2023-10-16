import pygetwindow as gw
from modules.api import conf

class DopSelect:
    '''
    Выбор всех вкладок для заметок
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.get_tabs()
        self.mw.comboBox_doptab.activated.connect(self.activate_dop)
        self.mw.comboBox_doptab.clicked.connect(self.on_combo_clicked)

    def get_tabs(self):
        self.mw.comboBox_doptab.clear()
        self.mw.comboBox_doptab.addItem('-')
        a = [i for i in gw.getAllTitles() if i not in ('', conf['NAME'], 'Параметры', 'Проводник', 'Program Manager')]
        for i in range(len(a)):
            self.mw.comboBox_doptab.addItem(a[i])

    def activate_dop(self, index):
        window = self.mw.comboBox_doptab.itemText(index)
        if window == '-':
            self.mw.dop_hWnd = None
        else:
            self.mw.dop_hWnd = gw.getWindowsWithTitle(window)[0]._hWnd
        
    def on_combo_clicked(self):
        selected = self.mw.comboBox_doptab.currentText()
        self.get_tabs()
        try:
            self.mw.comboBox_doptab.setCurrentText(selected)
        except Exception as e:
            print("can't set")
        
