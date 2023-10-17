import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import keyboard
import pygetwindow as gw
import time
import os
from design.design import Ui_Helper
from modules import *
from filters._kmplayer_to_google import kmplayer_to_google
import ctypes

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
        self.dop_hWnd = None
        self.google_hWnd = None
        self.lang = None

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
        self.change_lang = ChangeLang(self)

        self.player = 'KMPlayer'
        kmplayer_to_google(self, 'KMPlayer')

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

        keyboard.on_press_key('num 4', self.simulate_left_arrow, suppress=True)
        keyboard.on_press_key('num 5', self.simulate_space, suppress=True)
        keyboard.on_press_key(
            'num 6', self.simulate_right_arrow, suppress=True)
        keyboard.on_press_key('num 0', self.dop_tab_active, suppress=True)
        keyboard.press(76)

    def dop_tab_active(self, event):
        lang = self.lang_now()
        if event.scan_code == 82 and event.is_keypad:
            try:
                window = self.comboBox_doptab.currentText()
                if gw.getActiveWindowTitle() != gw._pygetwindow_win.Win32Window(hWnd=self.dop_hWnd).title:
                    self.last_active = gw.getActiveWindowTitle()
                    dop = gw._pygetwindow_win.Win32Window(hWnd=self.dop_hWnd)
                    dop.activate()
                    if not dop.isMaximized:
                        dop.restore()
                else:
                    dop = gw._pygetwindow_win.Win32Window(hWnd=self.dop_hWnd)
                    window = gw.getWindowsWithTitle(self.last_active)[0]
                    window.activate()
                    dop.minimize()
                # меняем язык, если есть
                if self.comboBox_language.currentText() != '-':
                    self.change_lang.switch_input_language(lang)
            except Exception as e:
                print(e)
        elif event.scan_code == 82 and not event.is_keypad:
            keyboard.press_and_release('insert')
        elif event.scan_code == 11 and not event.is_keypad:
            keyboard.press_and_release('0')

    def simulate_left_arrow(self, event):
        if self.files:
            if event.scan_code == 75 and event.is_keypad:
                if gw.getActiveWindowTitle() != conf['NAME']:
                    self.activate_window('left')
            elif event.scan_code == 75 and not event.is_keypad:
                keyboard.press_and_release('left')
            elif event.scan_code == 5 and not event.is_keypad:
                keyboard.press_and_release('4')

    def simulate_space(self, event):
        if self.files:
            if event.scan_code == 76 and event.is_keypad:
                self.activate_window('space')
            elif event.scan_code == 6 and not event.is_keypad:
                keyboard.press_and_release('5')

    def simulate_right_arrow(self, event):
        if self.files:
            if event.scan_code == 77 and event.is_keypad:
                if gw.getActiveWindowTitle() != conf['NAME']:
                    self.activate_window('right')
            elif event.scan_code == 77 and not event.is_keypad:
                keyboard.press_and_release('right')
            elif event.scan_code == 7 and not event.is_keypad:
                keyboard.press_and_release('6')

    def activate_window(self, button):
        try:
            lang = self.lang_now()
            old_path = gw.getActiveWindow().title
            new_path = None

            # Выбираем что будет играть плеер или гугл хром
            if self.player == 'KMPlayer':
                for i in self.files:
                    if len(gw.getWindowsWithTitle(i)):
                        new_path = gw.getWindowsWithTitle(i)[0]
            elif self.player == 'Google Chrome':
                new_path = gw._pygetwindow_win.Win32Window(
                    hWnd=self.google_hWnd)

            # настраиваем переключение между окнами
            if new_path:
                old_active = gw.getActiveWindow().title
                new_path.activate()
                if not new_path.isMaximized:
                    new_path.restore()
                keyboard.send(button)
                time.sleep(0.01)
                if new_path.title == old_active and not self.checkBox.checkState():
                    if conf['MINIMIZE']:
                        if button == 'space':
                            new_path.minimize()
                if self.checkBox.checkState():
                    a = gw.getWindowsWithTitle(old_path)[0]
                    a.activate()

            # меняем язык, если есть
            if self.comboBox_language.currentText() != '-':
                self.change_lang.switch_input_language(lang)

        except:
            pass

    def lang_now(self):
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        handle = user32.GetForegroundWindow()
        threadid = user32.GetWindowThreadProcessId(handle, 0)
        layout_id = user32.GetKeyboardLayout(threadid)
        return layout_id & 0xFFFF


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
