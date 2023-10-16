import pygetwindow as gw


class GoogleSelect:
    '''
    Выбор вкладок гугл хром
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.google_window = None
        self.get_tabs()
        self.mw.comboBox_chrome.activated.connect(self.activate_hWnd)
        self.mw.comboBox_chrome.clicked.connect(self.on_combo_clicked)
        self.activate_hWnd(0)

    def get_tabs(self):
        self.mw.comboBox_chrome.clear()
        a = [i.split(' - Google Chrome')[0] for i in gw.getAllTitles() if 'Google Chrome' in i]
        for i in a:
            self.mw.comboBox_chrome.addItem(i)
            self.mw.comboBox_chrome.setItemData(0, {i: gw.getWindowsWithTitle(i)})
        if self.google_window != None:
            self.mw.comboBox_chrome.setCurrentText(self.google_window)
            
    def activate_hWnd(self, index):
        window = self.mw.comboBox_chrome.itemText(index)
        try:
            self.mw.google_hWnd = gw.getWindowsWithTitle(window)[0]._hWnd
        except Exception as e:
            print(e)
            
    def on_combo_clicked(self):
        selected = self.mw.comboBox_chrome.currentText()
        self.get_tabs()
        try:
            self.mw.comboBox_doptab.setCurrentText(selected)
        except Exception as e:
            print("can't set")
        
