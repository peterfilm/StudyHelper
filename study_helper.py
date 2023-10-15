import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import keyboard
import pygetwindow as gw
import time
import os
from design.design import Ui_Helper
from modules import *
from filters._kmplayer_to_google import kmplayer_to_google

old_path = conf['NAME']


def activate_window_by_title(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        # Activate the first window with the given title
        window[0].activate()
        return True
    return False


class MyWindow(QMainWindow, Ui_Helper):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.files = []
        self.last_active = None
        self.pushButton_open.setEnabled(False)

        icon = QIcon(os.path.join("img", "icon.ico"))
        self.setWindowIcon(icon)
        self.lineEdit.setText(conf['LAST_PATH'])

        self.openFolder = OpenFolder(self)
        self.loadFolder = LoadFolder(self)
        self.kmplay = KMPlay(self)
        self.select_Path = SelectPath(self)
        self.google = GoogleSelect(self)
        self.kmplayer_chrome = KMPlayerToChrome(self)
        self.dop = DopSelect(self)
        kmplayer_to_google(self, 'kmplayer')

        # грузим qss в файл
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            qss_file_path = os.path.join(script_dir, "style.qss")
            with open(qss_file_path, "r") as qss_file:
                qss_content = qss_file.read()

            # Apply the QSS to your application
            self.setStyleSheet(qss_content)
        except Exception as e:
            print(e)

        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle(conf['NAME'])
        keyboard.on_press_key('num 4', self.simulate_left_arrow)
        keyboard.on_press_key('num 5', self.simulate_space)
        keyboard.on_press_key('num 6', self.simulate_right_arrow)
        keyboard.on_press_key('num 0', self.dop_tab_active)
        keyboard.press(76)

    def dop_tab_active(self, event):
        window = self.comboBox_doptab.currentText()
        if gw.getActiveWindowTitle() != window:
            self.last_active = gw.getActiveWindowTitle()
            dop = gw.getWindowsWithTitle(window)[0]
            dop.activate()
        else:
            window = gw.getWindowsWithTitle(self.last_active)[0]
            window.activate()

    def simulate_left_arrow(self, event):
        if self.files:
            if event.scan_code == 75 and event.is_keypad:
                self.activate_window('left')
                keyboard.press('right')

    def simulate_space(self, event):
        if self.files:
            if event.scan_code == 76 and event.is_keypad:
                self.activate_window('space')

    def simulate_right_arrow(self, event):
        if self.files:
            if event.scan_code == 77 and event.is_keypad:
                self.activate_window('right')
                keyboard.press('left')

    def activate_window(self, button):
        try:
            old_path = gw.getActiveWindow().title
            new_path = None
            for i in self.files:
                if len(gw.getWindowsWithTitle(i)):
                    new_path = gw.getWindowsWithTitle(i)[0]
            if new_path:
                old_active = gw.getActiveWindow().title
                new_path.activate()
                new_path.restore()
                keyboard.send(button)
                time.sleep(0.01)
                if new_path.title == old_active and not self.checkBox.checkState():
                    if button == 'space':
                        new_path.minimize()
                if self.checkBox.checkState():
                    a = gw.getWindowsWithTitle(old_path)[0]
                    a.activate()

        except:
            pass


def active_first_window():
    z = gw.getWindowsWithTitle(old_path)
    gw.getWindowsWithTitle(old_path)[0].activate()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    QTimer.singleShot(1, active_first_window)
    screen = QDesktopWidget().screenGeometry()
    window = MyWindow()

    # Calculate the position to center the window
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2

    # Move the window to the calculated position
    window.move(x, y)

    window.show()
    sys.exit(app.exec_())
