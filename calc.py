# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\Калькулятор\calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(630, 460))
        MainWindow.setMaximumSize(QtCore.QSize(630, 460))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Groupbox_nums = QtWidgets.QGroupBox(self.centralwidget)
        self.Groupbox_nums.setGeometry(QtCore.QRect(50, 140, 281, 291))
        self.Groupbox_nums.setAutoFillBackground(False)
        self.Groupbox_nums.setTitle("")
        self.Groupbox_nums.setObjectName("Groupbox_nums")
        self.Button1 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button1.setGeometry(QtCore.QRect(10, 10, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button1.setFont(font)
        self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button2.setGeometry(QtCore.QRect(100, 10, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button2.setFont(font)
        self.Button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button3.setGeometry(QtCore.QRect(190, 10, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button3.sizePolicy().hasHeightForWidth())
        self.Button3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button3.setFont(font)
        self.Button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button3.setObjectName("Button3")
        self.Button5 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button5.setGeometry(QtCore.QRect(100, 80, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button5.sizePolicy().hasHeightForWidth())
        self.Button5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button5.setFont(font)
        self.Button5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button5.setObjectName("Button5")
        self.Button6 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button6.setGeometry(QtCore.QRect(190, 80, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button6.sizePolicy().hasHeightForWidth())
        self.Button6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button6.setFont(font)
        self.Button6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button6.setObjectName("Button6")
        self.Button4 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button4.setGeometry(QtCore.QRect(10, 80, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button4.sizePolicy().hasHeightForWidth())
        self.Button4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button4.setFont(font)
        self.Button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button4.setObjectName("Button4")
        self.Button8 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button8.setGeometry(QtCore.QRect(100, 150, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button8.sizePolicy().hasHeightForWidth())
        self.Button8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button8.setFont(font)
        self.Button8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button8.setObjectName("Button8")
        self.Button9 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button9.setGeometry(QtCore.QRect(190, 150, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button9.sizePolicy().hasHeightForWidth())
        self.Button9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button9.setFont(font)
        self.Button9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button9.setObjectName("Button9")
        self.Button7 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button7.setGeometry(QtCore.QRect(10, 150, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button7.sizePolicy().hasHeightForWidth())
        self.Button7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button7.setFont(font)
        self.Button7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button7.setObjectName("Button7")
        self.Button_point = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button_point.setGeometry(QtCore.QRect(190, 220, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_point.sizePolicy().hasHeightForWidth())
        self.Button_point.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_point.setFont(font)
        self.Button_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_point.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_point.setObjectName("Button_point")
        self.Button0 = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button0.setGeometry(QtCore.QRect(100, 220, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button0.sizePolicy().hasHeightForWidth())
        self.Button0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button0.setFont(font)
        self.Button0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button0.setObjectName("Button0")
        self.Button_unar_minus = QtWidgets.QPushButton(self.Groupbox_nums)
        self.Button_unar_minus.setGeometry(QtCore.QRect(10, 220, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_unar_minus.sizePolicy().hasHeightForWidth())
        self.Button_unar_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_unar_minus.setFont(font)
        self.Button_unar_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_unar_minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_unar_minus.setObjectName("Button_unar_minus")
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_minus.setGeometry(QtCore.QRect(470, 150, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_minus.sizePolicy().hasHeightForWidth())
        self.Button_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_minus.setFont(font)
        self.Button_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_minus.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Button_minus.setObjectName("Button_minus")
        self.Button_multipl = QtWidgets.QPushButton(self.centralwidget)
        self.Button_multipl.setGeometry(QtCore.QRect(380, 220, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_multipl.sizePolicy().hasHeightForWidth())
        self.Button_multipl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_multipl.setFont(font)
        self.Button_multipl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_multipl.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Button_multipl.setObjectName("Button_multipl")
        self.Button_sum = QtWidgets.QPushButton(self.centralwidget)
        self.Button_sum.setGeometry(QtCore.QRect(380, 150, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_sum.sizePolicy().hasHeightForWidth())
        self.Button_sum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_sum.setFont(font)
        self.Button_sum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_sum.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Button_sum.setIconSize(QtCore.QSize(20, 20))
        self.Button_sum.setObjectName("Button_sum")
        self.Button_div = QtWidgets.QPushButton(self.centralwidget)
        self.Button_div.setGeometry(QtCore.QRect(470, 220, 80, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_div.sizePolicy().hasHeightForWidth())
        self.Button_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_div.setFont(font)
        self.Button_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_div.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Button_div.setObjectName("Button_div")
        self.Button_eq = QtWidgets.QPushButton(self.centralwidget)
        self.Button_eq.setGeometry(QtCore.QRect(380, 290, 170, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_eq.sizePolicy().hasHeightForWidth())
        self.Button_eq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_eq.setFont(font)
        self.Button_eq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_eq.setObjectName("Button_eq")
        self.Button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.Button_clear.setGeometry(QtCore.QRect(380, 360, 170, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_clear.sizePolicy().hasHeightForWidth())
        self.Button_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_clear.setFont(font)
        self.Button_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_clear.setObjectName("Button_clear")
        self.Groupbox_operations = QtWidgets.QGroupBox(self.centralwidget)
        self.Groupbox_operations.setGeometry(QtCore.QRect(370, 140, 191, 291))
        self.Groupbox_operations.setTitle("")
        self.Groupbox_operations.setObjectName("Groupbox_operations")
        self.Groupbox_review = QtWidgets.QGroupBox(self.centralwidget)
        self.Groupbox_review.setGeometry(QtCore.QRect(20, 20, 591, 80))
        self.Groupbox_review.setTitle("")
        self.Groupbox_review.setObjectName("Groupbox_review")
        self.Label_operation = QtWidgets.QLabel(self.Groupbox_review)
        self.Label_operation.setGeometry(QtCore.QRect(190, 20, 16, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Label_operation.setFont(font)
        self.Label_operation.setObjectName("Label_operation")
        self.Label_eq = QtWidgets.QLabel(self.Groupbox_review)
        self.Label_eq.setGeometry(QtCore.QRect(390, 20, 16, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Label_eq.setFont(font)
        self.Label_eq.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Label_eq.setObjectName("Label_eq")
        self.TexBox_result = QtWidgets.QTextEdit(self.Groupbox_review)
        self.TexBox_result.setGeometry(QtCore.QRect(410, 20, 170, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TexBox_result.sizePolicy().hasHeightForWidth())
        self.TexBox_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TexBox_result.setFont(font)
        self.TexBox_result.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.TexBox_result.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TexBox_result.setFrameShape(QtWidgets.QFrame.Box)
        self.TexBox_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TexBox_result.setObjectName("TexBox_result")
        self.LineEdit1 = QtWidgets.QLineEdit(self.Groupbox_review)
        self.LineEdit1.setGeometry(QtCore.QRect(10, 20, 170, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit1.sizePolicy().hasHeightForWidth())
        self.LineEdit1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LineEdit1.setFont(font)
        self.LineEdit1.setReadOnly(True)
        self.LineEdit1.setStyleSheet("QLineEdit:focus { border: 2px solid black;}")
        self.LineEdit1.setTabletTracking(False)
        self.LineEdit1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.LineEdit1.setAutoFillBackground(False)
        self.LineEdit1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineEdit1.setClearButtonEnabled(False)
        self.LineEdit1.setObjectName("LineEdit1")
        self.LineEdit2 = QtWidgets.QLineEdit(self.Groupbox_review)
        self.LineEdit2.setGeometry(QtCore.QRect(210, 20, 170, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit2.sizePolicy().hasHeightForWidth())
        self.LineEdit2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LineEdit2.setFont(font)
        self.LineEdit2.setStyleSheet("QLineEdit:focus { border: 2px solid black;}")
        self.LineEdit2.setReadOnly(True)
        self.LineEdit2.setTabletTracking(False)
        self.LineEdit2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.LineEdit2.setAutoFillBackground(False)
        self.LineEdit2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineEdit2.setClearButtonEnabled(False)
        self.LineEdit2.setObjectName("LineEdit2")
        self.Groupbox_operations.raise_()
        self.Groupbox_review.raise_()
        self.Groupbox_nums.raise_()
        self.Button_clear.raise_()
        self.Button_multipl.raise_()
        self.Button_sum.raise_()
        self.Button_minus.raise_()
        self.Button_eq.raise_()
        self.Button_div.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button_point.setText(_translate("MainWindow", "."))
        self.Button0.setText(_translate("MainWindow", "0"))
        self.Button_unar_minus.setText(_translate("MainWindow", "+/-"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_multipl.setText(_translate("MainWindow", "*"))
        self.Button_sum.setText(_translate("MainWindow", "+"))
        self.Button_div.setText(_translate("MainWindow", ":"))
        self.Button_eq.setText(_translate("MainWindow", "="))
        self.Button_clear.setText(_translate("MainWindow", "CLEAR"))
        self.Label_operation.setText(_translate("MainWindow", "?"))
        self.Label_eq.setText(_translate("MainWindow", "="))
        self.TexBox_result.setPlaceholderText(_translate("MainWindow", "Результат"))
        self.LineEdit1.setPlaceholderText(_translate("MainWindow", "Введите число"))
        self.LineEdit2.setPlaceholderText(_translate("MainWindow", "Введите число"))
