# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modules.api import conf
from filters._ClicableLabel import ClickableLabel

class Ui_Helper(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 480)
        MainWindow.setMinimumSize(QtCore.QSize(390, 480))
        MainWindow.setMaximumSize(QtCore.QSize(390, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 355, 442))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(161, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.radioButton_kmplayer = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_kmplayer.setChecked(True)
        self.radioButton_kmplayer.setObjectName("radioButton_kmplayer")
        self.horizontalLayout.addWidget(self.radioButton_kmplayer)
        self.radioButton_google = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_google.setObjectName("radioButton_google")
        self.horizontalLayout.addWidget(self.radioButton_google)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_kmplayer = QtWidgets.QLabel(self.layoutWidget)
        self.label_kmplayer.setMinimumSize(QtCore.QSize(197, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_kmplayer.setFont(font)
        self.label_kmplayer.setObjectName("label_kmplayer")
        self.horizontalLayout_2.addWidget(self.label_kmplayer)
        self.label_kmplayer_path = ClickableLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_kmplayer_path.setFont(font)
        self.label_kmplayer_path.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_kmplayer_path.setObjectName("label_kmplayer_path")
        self.horizontalLayout_2.addWidget(self.label_kmplayer_path)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(247, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_kmplay = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_kmplay.setMinimumSize(QtCore.QSize(51, 31))
        self.pushButton_kmplay.setObjectName("pushButton_kmplay")
        self.pushButton_kmplay.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_3.addWidget(self.pushButton_kmplay)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(191, 41))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_open = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_open.setMinimumSize(QtCore.QSize(151, 41))
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout_4.addWidget(self.pushButton_open)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_choose_chrome = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose_chrome.setFont(font)
        self.label_choose_chrome.setObjectName("label_choose_chrome")
        self.label_choose_chrome.hide()
        self.verticalLayout.addWidget(self.label_choose_chrome)
        self.comboBox_chrome = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_chrome.setMinimumSize(QtCore.QSize(351, 31))
        self.comboBox_chrome.setObjectName("comboBox_chrome")
        self.verticalLayout.addWidget(self.comboBox_chrome)
        self.comboBox_chrome.hide()
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_doptab = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_doptab.setFont(font)
        self.label_doptab.setObjectName("label_doptab")
        self.verticalLayout_2.addWidget(self.label_doptab)
        self.comboBox_doptab = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_doptab.setMinimumSize(QtCore.QSize(351, 31))
        self.comboBox_doptab.setObjectName("comboBox_doptab")
        self.verticalLayout_2.addWidget(self.comboBox_doptab)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.comboBox_language = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_language.setMinimumSize(QtCore.QSize(121, 31))
        self.comboBox_language.setObjectName("comboBox_language")
        self.horizontalLayout_5.addWidget(self.comboBox_language)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(40, 0))
        self.label_5.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", conf['NAME']))
        self.label_8.setText(_translate("MainWindow", "Где воспроизводится:"))
        self.radioButton_kmplayer.setText(_translate("MainWindow", "KMPlayer"))
        self.radioButton_google.setText(
            _translate("MainWindow", "Google Chrome"))
        self.label_kmplayer.setText(_translate("MainWindow", "KMPlayer"))
        self.label_kmplayer_path.setText(_translate(
            "MainWindow", "Выбрать путь до плеера"))
        self.pushButton_kmplay.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate(
            "MainWindow", "Выбрать папку с видео"))
        self.pushButton_open.setText(_translate("MainWindow", "Открыть папку"))
        self.label_choose_chrome.setText(_translate(
            "MainWindow", "Выберите окно Google Chrome:"))
        self.label_doptab.setText(_translate(
            "MainWindow", "Дополнительная вкладка:"))
        self.label_15.setText(_translate(
            "MainWindow", "Автоматически менять язык ввода:"))
        self.checkBox.setText(_translate("MainWindow", "Два экрана"))
        self.label_5.setText(_translate("MainWindow", "Num 4"))
        self.label.setText(_translate("MainWindow", "-  назад на 5 секунд"))
        self.label_6.setText(_translate("MainWindow", "Num 5"))
        self.label_2.setText(_translate(
            "MainWindow", "-  воспроизвести / остановить"))
        self.label_7.setText(_translate("MainWindow", "Num 6"))
        self.label_3.setText(_translate("MainWindow", "-  вперед на 5 секунд"))
        self.label_13.setText(_translate("MainWindow", "Num 0"))
        self.label_12.setText(_translate(
            "MainWindow", "-  переключение на дополнительную вкладку"))
