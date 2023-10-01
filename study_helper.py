import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtCore import QTimer, QUrl
import keyboard
import pygetwindow as gw
import time
import os
from design.design import Ui_Helper
from functools import partial

old_path = 'Study Helper v1.0'


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
        self.directory = None
        
        icon = QIcon(os.path.join("img", "icon.ico"))
        self.setWindowIcon(icon)
        
        self.pushButton.clicked.connect(partial(self.open_folder, 'button'))
        self.pushButton_open.clicked.connect(self.open_browser)
        self.lineEdit.returnPressed.connect(partial(self.open_folder, 'lineedit'))
        
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
        self.setWindowTitle('Study Helper v1.0')
        keyboard.on_press_key('num 4', self.simulate_left_arrow)
        keyboard.on_press_key('num 5', self.simulate_space)
        keyboard.on_press_key('num 6', self.simulate_right_arrow)
        keyboard.press(76)
        
    def open_folder(self, value):
        if value =='lineedit':
            directory = self.lineEdit.text()
        if value == 'button':
            directory = QFileDialog.getExistingDirectory(self)
        if os.path.exists(directory):
            self.files = [i for i in os.listdir(directory) if os.path.isfile(os.path.join(directory, i))]
            self.lineEdit.setText(directory)  
            self.directory = directory
            self.pushButton_open.setEnabled(True)
            QMessageBox.information(self, 'Информация', 'Папка выбрана')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Выберите корректный путь')
            self.lineEdit.setText('')
            self.pushButton_open.setEnabled(False)
            
            
    def open_browser(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.directory))
            
        
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
            # print(gw.getAllTitles())
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