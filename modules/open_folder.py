from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from modules.api import conf
from filters._open_folder import check_open_folder


class OpenFolder:
    '''
    Кнопка открытия папки
    '''

    def __init__(self, main_window):
        self.mw = main_window
        check_open_folder(self.mw)
        self.mw.pushButton_open.clicked.connect(self.open_browser)

    def open_browser(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(conf['LAST_PATH']))
