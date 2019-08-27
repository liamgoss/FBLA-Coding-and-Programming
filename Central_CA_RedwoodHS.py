# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LibrarySoftware_V1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# :::Identifier Explanation / List:::
#
# Identifiers are as follows:
# [Section Letter (C/L/R)]_[Widget Type (lbl, btn, etc.)]_
# [Human Readable Name(Item1, StudentSearch, etc.)]_[Tab Name (if applicable)]
# EX: C_tbl_ItemList = check out tab, QTableWidget, list items to check out
#
# C = Check Out tab
# R = Return tab
# L = Library tab
#
# lbl = labels
# btn = buttons
# le = line edits
# rb = radio buttons
# gv = graphics view
# cb = check box
# pb = progress bar
# tb = text browser
# tbl = table widget
#
# Numerical ex: C_lbl_1 = 1st label in Check Out tab
#
#
# Importing 'os' module for the 'getenv' feature to work in conjuction with QFileDialog for exporting/importing data
# 'sys' module imported for 'app.exec_()' feature to create a loop for the GUI
# PyQt5.QtWidgets separated for readability:
#   Main functionality of window -> Layout customization -> User interface components

import csv
import datetime
import pickle
import os
import sys
import traceback
import pyAesCrypt

from datetime import timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QVBoxLayout
from PyQt5.QtWidgets import qApp, QAction, QPushButton, QTableView, QGraphicsScene, QLabel, QGraphicsPixmapItem, \
    QInputDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    # This function as well as retranslateUI were made using Qt Designer and were edited along the way to as need be
    # The order of widget creation is based on Designer compiling and may not seem logical
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CLR_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.CLR_tabWidget.setMouseTracking(False)
        self.CLR_tabWidget.setTabsClosable(False)
        self.CLR_tabWidget.setObjectName("CLR_tabWidget")
        self.tab_CheckOut = QtWidgets.QWidget()
        self.tab_CheckOut.setObjectName("tab_CheckOut")


        self.C_Tabwidget = QtWidgets.QTabWidget(self.tab_CheckOut)
        self.C_Tabwidget.setGeometry(QtCore.QRect(0, 220, 1161, 171))
        self.C_Tabwidget.setObjectName("C_Tabwidget")



        self.C_lw_StudentInfo = QtWidgets.QListWidget(self.tab_CheckOut)
        self.C_lw_StudentInfo.setGeometry(QtCore.QRect(0, 0, 331, 131))
        self.C_lw_StudentInfo.setObjectName("C_lw_StudentInfo")


        self.C_calendarWidget = QtWidgets.QCalendarWidget(self.tab_CheckOut)
        self.C_calendarWidget.setGeometry(QtCore.QRect(870, 0, 291, 201))
        self.C_calendarWidget.setMinimumDate(QtCore.QDate(2000, 12, 31))
        self.C_calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.C_calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.C_calendarWidget.setNavigationBarVisible(True)
        self.C_calendarWidget.setDateEditEnabled(True)
        self.C_calendarWidget.setObjectName("C_calendarWidget")


        item = QtWidgets.QListWidgetItem()
        self.C_lw_StudentInfo.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.C_lw_StudentInfo.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.C_lw_StudentInfo.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.C_lw_StudentInfo.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.C_lw_StudentInfo.addItem(item)


        self.C_tbl_CO_Roll = QtWidgets.QTableWidget(self.tab_CheckOut)
        self.C_tbl_CO_Roll.setGeometry(QtCore.QRect(10, 400, 421, 321))
        self.C_tbl_CO_Roll.setObjectName("C_tbl_CO_Roll")
        self.C_tbl_CO_Roll.setColumnCount(0)
        self.C_tbl_CO_Roll.setRowCount(0)

        self.C_Tabwidget.raise_()
        self.C_calendarWidget.raise_()


        self.C_tbl_CO_Roll.raise_()
        self.CLR_tabWidget.addTab(self.tab_CheckOut, "")
        self.tab_Return = QtWidgets.QWidget()
        self.tab_Return.setObjectName("tab_Return")

        self.R_lw_StudentInfo = QtWidgets.QListWidget(self.tab_Return)
        self.R_lw_StudentInfo.setGeometry(QtCore.QRect(0, 0, 331, 131))
        self.R_lw_StudentInfo.setObjectName("R_lw_StudentInfo")

        itemR = QtWidgets.QListWidgetItem()
        self.R_lw_StudentInfo.addItem(itemR)
        itemR = QtWidgets.QListWidgetItem()
        self.R_lw_StudentInfo.addItem(itemR)
        itemR = QtWidgets.QListWidgetItem()
        self.R_lw_StudentInfo.addItem(itemR)
        itemR = QtWidgets.QListWidgetItem()
        self.R_lw_StudentInfo.addItem(itemR)
        itemR = QtWidgets.QListWidgetItem()
        self.R_lw_StudentInfo.addItem(itemR)
        self.R_lw_StudentInfo.raise_()

        self.C_tbl_ItemList = QtWidgets.QTableWidget(self.tab_CheckOut)
        self.C_tbl_ItemList.setGeometry(QtCore.QRect(0, 220, 1171, 171))
        self.C_tbl_ItemList.setObjectName("C_tbl_ItemList")
        self.C_tbl_ItemList.setColumnCount(10)
        self.C_tbl_ItemList.setRowCount(5)



        vHeaderCount0 = 0
        for vHeaderCount0 in range(5):
            item = QtWidgets.QTableWidgetItem()
            self.C_tbl_ItemList.setVerticalHeaderItem(vHeaderCount0, item)
        hHeaderCount0 = 0
        for hHeaderCount0 in range(10):
            item = QtWidgets.QTableWidgetItem()
            self.C_tbl_ItemList.setHorizontalHeaderItem(hHeaderCount0, item)

        cX = 0
        cY = 0
        for cY in range(10):
            item = QtWidgets.QTableWidgetItem()
            self.C_tbl_ItemList.setItem(cX, cY, item)
            if cX == 0 and cY == 9:
                cX = 1
                cY = 0
                item = QtWidgets.QTableWidgetItem()
                self.C_tbl_ItemList.setItem(cX, cY, item)

        self.R_calendarWidget = QtWidgets.QCalendarWidget(self.tab_Return)
        self.R_calendarWidget.setGeometry(QtCore.QRect(870, 0, 291, 201))
        self.R_calendarWidget.setMinimumDate(QtCore.QDate(2000, 12, 31))
        self.R_calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.R_calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.R_calendarWidget.setNavigationBarVisible(True)
        self.R_calendarWidget.setDateEditEnabled(True)
        self.R_calendarWidget.setObjectName("R_calendarWidget")
        self.R_Tabwidget = QtWidgets.QTabWidget(self.tab_Return)
        self.R_Tabwidget.setGeometry(QtCore.QRect(0, 220, 1161, 171))
        self.R_Tabwidget.setObjectName("R_Tabwidget")
        self.tab_IOL_R = QtWidgets.QWidget()
        self.tab_IOL_R.setObjectName("tab_IOL_R")

        self.C_tbl_R_Roll = QtWidgets.QTableWidget(self.tab_Return)
        self.C_tbl_R_Roll.setGeometry(QtCore.QRect(10, 400, 421, 321))
        self.C_tbl_R_Roll.setObjectName("C_tbl_CO_Roll")
        self.C_tbl_R_Roll.setColumnCount(0)
        self.C_tbl_R_Roll.setRowCount(0)
        self.C_tbl_CO_Roll.cellDoubleClicked.connect(self.onDoubleClickC)
        self.C_tbl_R_Roll.cellDoubleClicked.connect(self.onDoubleClickR)


        self.R_tbl_ItemList = QtWidgets.QTableWidget(self.tab_Return)
        self.R_tbl_ItemList.setGeometry(QtCore.QRect(0, 220, 1171, 171))
        self.R_tbl_ItemList.setObjectName("R_tbl_ItemList")
        self.R_tbl_ItemList.setColumnCount(10)
        self.R_tbl_ItemList.setRowCount(5)


        vHeaderCount = 0
        for vHeaderCount in range(5):

            item = QtWidgets.QTableWidgetItem()
            self.R_tbl_ItemList.setVerticalHeaderItem(vHeaderCount, item)

        hHeaderCount = 0
        for hHeaderCount in range(10):

            item = QtWidgets.QTableWidgetItem()
            self.R_tbl_ItemList.setHorizontalHeaderItem(hHeaderCount, item)


        rX = 0
        rY = 0
        for rY in range(10):

            item = QtWidgets.QTableWidgetItem()
            self.R_tbl_ItemList.setItem(rX, rY, item)
            if rX == 0 and rY == 9:
                rX == 1
                rY == 0
                item = QtWidgets.QTableWidgetItem()
                self.R_tbl_ItemList.setItem(rX, rY, item)



        self.R_btn_Confirm = QtWidgets.QPushButton(self.tab_Return)
        self.R_btn_Confirm.setGeometry(QtCore.QRect(1060, 280, 75, 41))
        self.R_btn_Confirm.setObjectName("R_btn_Confirm")

        self.C_btn_Confirm = QtWidgets.QPushButton(self.tab_CheckOut)
        self.C_btn_Confirm.setGeometry(QtCore.QRect(1060, 280, 75, 41))
        self.C_btn_Confirm.setObjectName("C_btn_Confirm")


        self.CLR_tabWidget.addTab(self.tab_Return, "")
        self.tab_Library = QtWidgets.QWidget()
        self.tab_Library.setObjectName("tab_Library")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_Library)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 109, 1151, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.L_VerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.L_VerticalLayout.setContentsMargins(0, 0, 625, 0)
        self.L_VerticalLayout.setObjectName("L_VerticalLayout")
        self.L_tbl_Library = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.L_tbl_Library.setObjectName("L_tbl_Library")
        self.L_tbl_Library.setColumnCount(0)
        self.L_tbl_Library.setRowCount(0)
        self.L_VerticalLayout.addWidget(self.L_tbl_Library)

        self.L_rb_ChkOut = QtWidgets.QRadioButton(self.tab_Library)
        self.L_rb_ChkOut.setGeometry(QtCore.QRect(70, 40, 82, 17))
        self.L_rb_ChkOut.setObjectName("L_rb_ChkOut")
        self.L_rb_Return = QtWidgets.QRadioButton(self.tab_Library)
        self.L_rb_Return.setGeometry(QtCore.QRect(70, 60, 82, 17))
        self.L_rb_Return.setObjectName("L_rb_Return")

        self.L_CalendarWidget = QtWidgets.QCalendarWidget(self.tab_Library)
        self.L_CalendarWidget.setGeometry(QtCore.QRect(671, 290, 381, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_CalendarWidget.sizePolicy().hasHeightForWidth())
        self.L_CalendarWidget.setSizePolicy(sizePolicy)
        self.L_CalendarWidget.setObjectName("L_CalendarWidget")

        self.L_rb_ChkOut.setChecked(True)
        self.L_rb_Return.setChecked(False)

        self.L_tbl_Library.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.L_tbl_Library.cellDoubleClicked.connect(self.onDoubleClick)


        self.CLR_tabWidget.addTab(self.tab_Library, "")
        self.horizontalLayout.addWidget(self.CLR_tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.L_lbl_ImportLibrary = QtWidgets.QLabel(self.tab_Library)
        self.L_lbl_ImportLibrary.setGeometry(QtCore.QRect(500, -10, 600, 100))
        self.L_lbl_ImportLibrary.setObjectName("L_lbl_ImportLibrary")
        self.L_lbl_ImportLibrary.setText("\nTo import library:\ngo to File > "
                                         "Import Library  \nthen select \"Library.csv\" \n"
                                         "\nNote: \"Roll Sheet.csv\" must be imported and\n"
                                         "a student must be selected first!   ")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setTitle("")
        self.menu_2.setObjectName("menu_2")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.File_Action_Quit = QtWidgets.QAction(MainWindow)
        self.File_Action_Quit.setObjectName("File_Action_Quit")
        self.File_Action_Import = QtWidgets.QAction(MainWindow)
        self.File_Action_Import.setObjectName("File_Action_Import")

        self.File_Action_ImportLibrary = QtWidgets.QAction(MainWindow)
        self.File_Action_ImportLibrary.setObjectName("File_Action_ImportLibrary")


        self.menuFile.addAction(self.File_Action_Import)
        self.menuFile.addAction(self.File_Action_ImportLibrary)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.File_Action_Quit)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.CLR_tabWidget.setCurrentIndex(0)


        self.File_Action_Quit.triggered.connect(self.fileQuit)
        self.File_Action_ImportLibrary.triggered.connect(self.importLibraryCSV)
        self.File_Action_Import.triggered.connect(self.importRollCSVs)

        self.R_btn_Confirm.clicked.connect(self.confirmReturn)
        self.C_btn_Confirm.clicked.connect(self.confirmCheckOut)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redwood High School Library"))

        __sortingEnabled = self.C_lw_StudentInfo.isSortingEnabled()
        self.C_lw_StudentInfo.setSortingEnabled(False)
        itemC = self.C_lw_StudentInfo.item(0)
        __sortingEnabled = self.R_lw_StudentInfo.isSortingEnabled()
        self.R_lw_StudentInfo.setSortingEnabled(False)
        itemR = self.R_lw_StudentInfo.item(0)

        placeHolderName = 'Student Name:   '
        placeHolderID = 'Student ID:          '
        placeHolderGrade = 'Grade Level:        '
        placeHolderChkOut = 'Checked Out:      '

        listItems = [placeHolderName, placeHolderID, placeHolderGrade, placeHolderChkOut]

        for i in listItems:

            itemC.setText(_translate('MainWindow', i))
            itemR.setText(_translate('MainWindow', i))
            itemC = self.C_lw_StudentInfo.item(listItems.index(i) + 1)
            itemR = self.R_lw_StudentInfo.item(listItems.index(i) + 1)





        self.C_lw_StudentInfo.setSortingEnabled(__sortingEnabled)
        self.R_lw_StudentInfo.setSortingEnabled(__sortingEnabled)

        item = self.C_tbl_ItemList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item 1"))
        item = self.C_tbl_ItemList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item 2"))
        item = self.C_tbl_ItemList.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item 3"))
        item = self.C_tbl_ItemList.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item 4"))
        item = self.C_tbl_ItemList.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Item 5"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Author"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Call No."))
        item = self.C_tbl_ItemList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Check Out Date"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Price"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Total Fine"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Renewed?"))
        item = self.C_tbl_ItemList.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Overdue?"))
        __sortingEnabled = self.C_tbl_ItemList.isSortingEnabled()
        self.C_tbl_ItemList.setSortingEnabled(False)
        item = self.C_tbl_ItemList.item(0, 0)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 1)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 2)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 3)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 4)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 5)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 6)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 7)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 8)

        item.setText(_translate("MainWindow", ""))
        item = self.C_tbl_ItemList.item(0, 9)

        item.setText(_translate("MainWindow", ""))
        self.C_tbl_ItemList.setSortingEnabled(__sortingEnabled)

        self.CLR_tabWidget.setTabText(self.CLR_tabWidget.indexOf(self.tab_CheckOut),
                                      _translate("MainWindow", "Check Out"))



        self.C_lw_StudentInfo.setSortingEnabled(__sortingEnabled)
        self.CLR_tabWidget.setTabText(self.CLR_tabWidget.indexOf(self.tab_CheckOut),
                                      _translate("MainWindow", "Check Out"))



        item = self.R_tbl_ItemList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item 1"))
        item = self.R_tbl_ItemList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item 2"))
        item = self.R_tbl_ItemList.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item 3"))
        item = self.R_tbl_ItemList.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item 4"))
        item = self.R_tbl_ItemList.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Item 5"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Author"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Call No."))
        item = self.R_tbl_ItemList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Check Out Date"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Price"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Total Fine"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Renewed?"))
        item = self.R_tbl_ItemList.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Overdue?"))

        __sortingEnabled = self.R_tbl_ItemList.isSortingEnabled()
        self.R_tbl_ItemList.setSortingEnabled(False)
        item = self.R_tbl_ItemList.item(0, 0)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 1)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 2)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 3)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 4)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 5)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 6)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 7)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 8)

        item.setText(_translate("MainWindow", ""))
        item = self.R_tbl_ItemList.item(0, 9)

        item.setText(_translate("MainWindow", ""))

        self.R_tbl_ItemList.setSortingEnabled(__sortingEnabled)
        self.R_btn_Confirm.setText(_translate("MainWindow", "Confirm"))
        self.C_btn_Confirm.setText(_translate("MainWindow", "Confirm"))

        self.L_rb_ChkOut.setText(_translate("MainWindow", "Check Out"))
        self.L_rb_Return.setText(_translate("MainWindow", "Return"))

        self.CLR_tabWidget.setTabText(self.CLR_tabWidget.indexOf(self.tab_Return), _translate("MainWindow", "Return"))
        self.CLR_tabWidget.setTabText(self.CLR_tabWidget.indexOf(self.tab_Library), _translate("MainWindow", "Library"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.File_Action_Quit.setText(_translate("MainWindow", "Quit"))
        self.File_Action_Import.setText(_translate("MainWindow", "Import Roll Sheet"))
        self.File_Action_ImportLibrary.setText(_translate("MainWindow", "Import Library"))

        # Now begins functions that were not created in Qt

    def onDoubleClick(self):
        selectedCell = self.L_tbl_Library.item(self.L_tbl_Library.currentRow(),
                                               self.L_tbl_Library.currentColumn()).text()


        rowData = []

        for x in range(5):
            curRow = self.L_tbl_Library.currentRow()
            rowItem = self.L_tbl_Library.item(curRow, x).text()
            rowData.append(rowItem)


        global finalTitle, finalAuthor, finalCallNo, finalISBN, finalPrice, finalChkOutDate, finalDueDate
        global finalTotalFine, finalIsRenewed, finalIsOverdue
        self.finalTitle = rowData[0]
        self.finalAuthor = rowData[1]
        self.finalCallNo = rowData[2]
        self.finalISBN = rowData[3]
        self.finalPrice = rowData[4]

        todaysDate = datetime.datetime.now()
        chkOutDate = todaysDate.date()
        self.finalChkOutDate = datetime.datetime.today().strftime('%Y-%m-%d')

        self.finalDueDate = chkOutDate + timedelta(days=14)

        self.finalIsRenewed = ""

        try:
            difference = self.finalDueDate - timedelta(days=14)

            if difference < chkOutDate:
                self.finalIsOverdue = 'Yes'
                self.finalTotalFine = '$2.50'

            elif difference > chkOutDate:
                self.finalIsOverdue = 'No'
                self.finalTotalFine = '$0.00'

            elif difference == chkOutDate:
                self.finalIsOverdue = 'No'
                self.finalTotalFine = '$0.00'

        except:
            # Some errors decide not to display in PyCharm when the program crashes so the traceback module forces it to
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
            raise






        if self.L_rb_ChkOut.isChecked() == True:
            self.insertItems_C()  # if the Check out option is selected then insert Items into C_tbl_ItemList
        elif self.L_rb_Return.isChecked() == True:
            self.insertItems()  # if the Return option is selected then insert items into R_tbl_ItemList




    def onDoubleClickC(self):
        try:


            self.defineSelectedItems()
            self.defineDisplayedItems()
            _translate = QtCore.QCoreApplication.translate
            __sortingEnabled = self.C_lw_StudentInfo.isSortingEnabled()
            self.C_lw_StudentInfo.setSortingEnabled(False)
            itemC = self.C_lw_StudentInfo.item(0)
            __sortingEnabled = self.R_lw_StudentInfo.isSortingEnabled()
            self.R_lw_StudentInfo.setSortingEnabled(False)
            itemR = self.R_lw_StudentInfo.item(0)


            selectedCell = self.C_tbl_CO_Roll.item(self.C_tbl_CO_Roll.currentRow(),
                                                   self.C_tbl_CO_Roll.currentColumn()).text()


            global rowData
            rowData = []


            for x in range(4):
                curRow = self.C_tbl_CO_Roll.currentRow()
                curCol = self.C_tbl_CO_Roll.currentColumn()
                rowItem = self.C_tbl_CO_Roll.item(curRow, 0 + x).text()
                rowData.append(rowItem)


            self.selName = rowData[0]
            self.selID = rowData[1]
            self.selGrade = rowData[2]
            self.selChkOut = ''
            self.selTeacher = rowData[3]
            self.defineDisplayedItems()
            self.finalID = rowData[1]


            listItems = [self.disName, self.disID, self.disGrade, self.disChkOut, self.disTeacher]

            for i in listItems:

                itemC.setText(_translate('MainWindow', i))
                itemR.setText(_translate('MainWindow', i))
                itemC = self.C_lw_StudentInfo.item(listItems.index(i) + 1)
                itemR = self.R_lw_StudentInfo.item(listItems.index(i) + 1)
            self.C_lw_StudentInfo.setSortingEnabled(__sortingEnabled)
            self.R_lw_StudentInfo.setSortingEnabled(__sortingEnabled)


        except:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
            raise

    def onDoubleClickR(self):
        try:
            self.defineSelectedItems()
            self.defineDisplayedItems()
            _translate = QtCore.QCoreApplication.translate
            __sortingEnabled = self.C_lw_StudentInfo.isSortingEnabled()
            self.C_lw_StudentInfo.setSortingEnabled(False)
            itemC = self.C_lw_StudentInfo.item(0)
            __sortingEnabled = self.R_lw_StudentInfo.isSortingEnabled()
            self.R_lw_StudentInfo.setSortingEnabled(False)
            itemR = self.R_lw_StudentInfo.item(0)


            selectedCell = self.C_tbl_R_Roll.item(self.C_tbl_R_Roll.currentRow(),
                                                   self.C_tbl_R_Roll.currentColumn()).text()

            rowData = []



            listItems = [self.disName, self.disID, self.disGrade, self.disChkOut]

            for i in listItems:

                item.setText(_translate('MainWindow', i))
                itemR.setText(_translate('MainWindow', i))
                itemC = self.C_lw_StudentInfo.item(listItems.index(i) + 1)
                itemR = self.R_lw_StudentInfo.item(listItems.index(i) + 1)
            self.C_lw_StudentInfo.setSortingEnabled(__sortingEnabled)
            self.R_lw_StudentInfo.setSortingEnabled(__sortingEnabled)
            self.C_lw_StudentInfo.update()
            self.R_lw_StudentInfo.update()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
            raise


    def defineSelectedItems(self):
        global selName, selID, selGrade, selChkOut, selTeacher
        self.selName = ''
        self.selID = ''
        self.selGrade = ''
        self.selChkOut = ''
        self.selTeacher = ''
    def defineDisplayedItems(self):
        global disName, disID, disGrade, disChkOut, disTeacher
        self.disName = "Student Name:   " + self.selName   # displayed name
        self.disID = "Student ID:          " + self.selID  # displayed student ID
        self.disGrade = "Grade Level:        " + self.selGrade  # displayed student grade level
        self.disChkOut = "Checked Out:      " + self.selChkOut  # displayed amount of books checked out
        self.disTeacher = "1st Period:           " + self.selTeacher  # displayed teacher


    def importLibraryCSV(self):
        libraryCSVPath = QFileDialog.getOpenFileName(None, 'Open Library CSV', os.getcwd(), 'CSV(*.csv)')
        if libraryCSVPath != '':
            with open(libraryCSVPath[0], newline='') as csvfile:
                self.L_tbl_Library.setRowCount(0)
                self.L_tbl_Library.setColumnCount(0)
                cellreader = csv.reader(csvfile, dialect='excel')

                for row_data in cellreader:
                    row = self.L_tbl_Library.rowCount()
                    self.L_tbl_Library.insertRow(row)
                    self.L_tbl_Library.setColumnCount(len(row_data))
                    col_headers = ['Title', 'Author', 'Call No.', 'ISBN', 'Price']
                    self.L_tbl_Library.setHorizontalHeaderLabels(col_headers)
                    for column, data in enumerate(row_data):
                        item = QTableWidgetItem(data)
                        self.L_tbl_Library.setItem(row, column, item)


    def importRollCSVs(self):
        # These functions are to import the 'Roll Sheet.csv'
        # importRollCSVC is for the Roll Table on the 'Check Out' tab
        # importRollCSVR is for the Roll Table on the 'Return' tab
        def importRollCSVC(self):
            # Program will crash if user cancels importing a file, the try/except statement is an attempt that is able
                # to successfully provide a default filename but the program still crashes regardless
            global rollCSVPath
            rollCSVPath = QFileDialog.getOpenFileName(None, 'Open Roll CSV', os.getcwd(), 'CSV(*.csv)',
                                                      options=QFileDialog.DontUseNativeDialog)
            try:
                if rollCSVPath != '':
                    with open(rollCSVPath[0], newline='') as csvfile:
                        self.C_tbl_CO_Roll.setRowCount(0)
                        self.C_tbl_CO_Roll.setColumnCount(0)
                        cellreader = csv.reader(csvfile, dialect='excel')
                        # dialect='excel' tells the csv reader that the delimiters are commas

                        for row_data in cellreader:
                            row = self.C_tbl_CO_Roll.rowCount()
                            self.C_tbl_CO_Roll.insertRow(row)
                            self.C_tbl_CO_Roll.setColumnCount(len(row_data))
                            col_headers = ['Name', 'ID Number', 'Grade', 'Period 1 Teacher']
                            self.C_tbl_CO_Roll.setHorizontalHeaderLabels(col_headers)
                            for column, data in enumerate(row_data):
                                item = QTableWidgetItem(data)
                                self.C_tbl_CO_Roll.setItem(row, column, item)
            except FileNotFoundError:
                cwd = os.getcwd().replace('\\', '/')
                defaultFileName = str(cwd) + '/Roll Sheet.csv'
                rollCSVPath = defaultFileName
                print('new path is: ', rollCSVPath)
                with open(rollCSVPath, newline='') as csvfile:
                    self.C_tbl_CO_Roll.setRowCount(0)
                    self.C_tbl_CO_Roll.setColumnCount(0)
                    cellreader = csv.reader(csvfile, dialect='excel')
                    # dialect='excel' tells the csv reader that the delimiters are commas

                    for row_data in cellreader:
                        row = self.C_tbl_CO_Roll.rowCount()
                        self.C_tbl_CO_Roll.insertRow(row)
                        self.C_tbl_CO_Roll.setColumnCount(len(row_data))
                        col_headers = ['Name', 'ID Number', 'Grade', 'Period 1 Teacher']
                        self.C_tbl_CO_Roll.setHorizontalHeaderLabels(col_headers)
                        for column, data in enumerate(row_data):
                            item = QTableWidgetItem(data)
                            self.C_tbl_CO_Roll.setItem(row, column, item)
                print('Finished with statement')



        def importRollCSVR(self):

            if rollCSVPath != '':
                with open(rollCSVPath[0], newline='') as csvfile:
                    self.C_tbl_R_Roll.setRowCount(0)
                    self.C_tbl_R_Roll.setColumnCount(0)
                    cellreader = csv.reader(csvfile, dialect='excel')

                    for row_data in cellreader:
                        row = self.C_tbl_R_Roll.rowCount()
                        self.C_tbl_R_Roll.insertRow(row)
                        self.C_tbl_R_Roll.setColumnCount(len(row_data))
                        col_headers = ['Name', 'ID Number', 'Grade', 'Period 1 Teacher']
                        self.C_tbl_R_Roll.setHorizontalHeaderLabels(col_headers)
                        for column, data in enumerate(row_data):
                            item = QTableWidgetItem(data)
                            self.C_tbl_R_Roll.setItem(row, column, item)

        importRollCSVC(self)
        importRollCSVR(self)

    # The moveToRow[X] functions are numerous and ugly but are designed to skip a row in the table if it is not empty
    def moveToRow4(self):

        if self.R_tbl_ItemList.item(4, 0).text() == '':
            global x
            x = 4
        elif self.R_tbl_ItemList.item(4, 0).text() != '':
            pass


    def moveToRow3(self):

        if self.R_tbl_ItemList.item(3, 0).text() == '':
            global x
            x = 3
        elif self.R_tbl_ItemList.item(3, 0).text() != '':
            self.moveToRow4()

    def moveToRow2(self):

        try:
            if self.R_tbl_ItemList.item(2, 0).text() == '':
                global x
                x = 2
            elif self.R_tbl_ItemList.item(2, 0).text() != '':
                self.moveToRow3()
        except AttributeError as e:
            pass

    def moveToRow1(self):

        if self.R_tbl_ItemList.item(1, 0).text() == '':
            global x
            x = 1
        elif self.R_tbl_ItemList.item(1, 0).text() != '':
            self.moveToRow2()

    def insertItems(self):
        try:
            if self.R_tbl_ItemList.item(0, 0).text() == '':
                global x
                x = 0
            elif self.R_tbl_ItemList.item(0, 0).text() != '':
                self.moveToRow1()

            try:
                for xval in range(1):

                    _translate = QtCore.QCoreApplication.translate

                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 0, item)
                    item = self.R_tbl_ItemList.item(x, 0)
                    item.setText(_translate("MainWindow", self.finalTitle))

                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 1, item)
                    item = self.R_tbl_ItemList.item(x, 1)
                    item.setText(_translate("MainWindow", self.finalAuthor))

                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 2, item)
                    item = self.R_tbl_ItemList.item(x, 2)
                    item.setText(_translate("MainWindow", self.finalCallNo))

                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 3, item)
                    item = self.R_tbl_ItemList.item(x, 3)
                    item.setText(_translate("MainWindow", self.finalISBN))

                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 4, item)
                    item = self.R_tbl_ItemList.item(x, 4)
                    item.setText(_translate("MainWindow", self.finalChkOutDate))


                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 5, item)
                    item = self.R_tbl_ItemList.item(x, 5)
                    item.setText(_translate("MainWindow", str(self.finalDueDate)))


                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 6, item)
                    item = self.R_tbl_ItemList.item(x, 6)
                    item.setText(_translate("MainWindow", self.finalPrice))


                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 7, item)
                    item = self.R_tbl_ItemList.item(x, 7)
                    item.setText(_translate("MainWindow", self.finalTotalFine))


                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 8, item)
                    item = self.R_tbl_ItemList.item(x, 8)

                    item.setText(_translate("MainWindow", 'N/A'))
                    # Renewal system is not yet in place

                    item = QtWidgets.QTableWidgetItem()
                    self.R_tbl_ItemList.setItem(x, 9, item)
                    item = self.R_tbl_ItemList.item(x, 9)
                    item.setText(_translate("MainWindow", self.finalIsOverdue))


                    x += 1

            except AttributeError:
                errorMsgBox = QMessageBox.question(None, 'Error!', "No more items left to return!", QMessageBox.Cancel)

        except:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
            raise

    def moveToRow4_C(self):

        if self.C_tbl_ItemList.item(4, 0).text() == '':
            global x
            x = 4
        elif self.C_tbl_ItemList.item(4, 0).text() != '':
            pass

    def moveToRow3_C_C(self):

        if self.C_tbl_ItemList.item(3, 0).text() == '':
            global x
            x = 3
        elif self.C_tbl_ItemList.item(3, 0).text() != '':
            self.moveToRow4_C()

    def moveToRow2_C(self):
        try:
            if self.C_tbl_ItemList.item(2, 0).text() == '':
                global x
                x = 2
            elif self.C_tbl_ItemList.item(2, 0).text() != '':
                self.moveToRow3_C_C()
        except AttributeError as e:
            pass

    def moveToRow1_C(self):

        if self.C_tbl_ItemList.item(1, 0).text() == '':
            global x
            x = 1
        elif self.C_tbl_ItemList.item(1, 0).text() != '':
            self.moveToRow2_C()

    def insertItems_C(self):
        try:
            if self.C_tbl_ItemList.item(0, 0).text() == '':
                global x
                x = 0
            elif self.C_tbl_ItemList.item(0, 0).text() != '':
                self.moveToRow1_C()

            try:
                for xval in range(1):

                    _translate = QtCore.QCoreApplication.translate

                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 0, item)
                    item = self.C_tbl_ItemList.item(x, 0)
                    item.setText(_translate("MainWindow", self.finalTitle))

                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 1, item)
                    item = self.C_tbl_ItemList.item(x, 1)
                    item.setText(_translate("MainWindow", self.finalAuthor))

                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 2, item)
                    item = self.C_tbl_ItemList.item(x, 2)
                    item.setText(_translate("MainWindow", self.finalCallNo))

                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 3, item)
                    item = self.C_tbl_ItemList.item(x, 3)
                    item.setText(_translate("MainWindow", self.finalISBN))

                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 4, item)
                    item = self.C_tbl_ItemList.item(x, 4)
                    item.setText(_translate("MainWindow", self.finalChkOutDate))


                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 5, item)
                    item = self.C_tbl_ItemList.item(x, 5)
                    item.setText(_translate("MainWindow", str(self.finalDueDate)))


                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 6, item)
                    item = self.C_tbl_ItemList.item(x, 6)
                    item.setText(_translate("MainWindow", self.finalPrice))


                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 7, item)
                    item = self.C_tbl_ItemList.item(x, 7)
                    item.setText(_translate("MainWindow", self.finalTotalFine))


                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 8, item)
                    item = self.C_tbl_ItemList.item(x, 8)
                    #item.setText(_translate("MainWindow", isRenewed))
                    item.setText(_translate("MainWindow", 'N/A'))
                    # Renewal system is not yet in place

                    item = QtWidgets.QTableWidgetItem()
                    self.C_tbl_ItemList.setItem(x, 9, item)
                    item = self.C_tbl_ItemList.item(x, 9)
                    item.setText(_translate("MainWindow", self.finalIsOverdue))


                    x += 1

            except AttributeError:
                print('Maximum number of items check out reached! Student must return one or more item(s)')
                errorMsgBox = QMessageBox.question(None, 'Error!', "Maximum number of items check out reached!"
                                                                   " Student must return one or more item(s)",
                                                   QMessageBox.Cancel)

        except:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
            raise

    def getPhotoPath(self):

        try:
            ID_number = self.selID
        except:
            try:
                QMessageBox.about(None, 'Notice!', 'A student must be selected from the roll table!')
                return
            except:
                print("Unexpected error:", sys.exc_info()[0])
                traceback.print_exc()
                raise


        filename = QFileDialog.getExistingDirectory(None, 'Select Folder', os.getenv('HOME'))
        global fileExt, image_path
        fileExtList = ['.jpeg', '.jpg', '.png']
        fileExt = fileExtList[0]
        image_path = str(filename + '/' + ID_number + str(fileExtList[0]))  # Try .jpeg ext
        try:

            photoExists = os.path.isfile(image_path)
            if photoExists == False:
                raise FileNotFoundError
            elif photoExists == True:
                pass



        except FileNotFoundError:
            try:
                image_path = str(filename + '/' + ID_number + str(fileExtList[1]))  # Try .jpg ext

                photoExists = os.path.isfile(image_path)
                if photoExists == False:
                    raise FileNotFoundError
                elif photoExists == True:
                    pass

            except FileNotFoundError:
                try:
                    image_path = str(filename + '/' + ID_number + str(fileExtList[2]))  # Try .png ext

                    photoExists = os.path.isfile(image_path)
                    if photoExists == False:
                        raise FileNotFoundError
                    elif photoExists == True:
                        pass


                except FileNotFoundError:
                    errorMsgBox = QMessageBox.question(None, 'Error!', "File does not exist!", QMessageBox.Cancel)


                    # File does not exist or is an unsupported format (ex: .gif)

        picPath = image_path
        studentPicC = QtGui.QPixmap(picPath)
        studentPicR = QtGui.QPixmap(picPath)

        self.labelC = QLabel()
        self.pixmapC = QPixmap(studentPicC)
        self.labelC.setPixmap(self.pixmapC)

        self.labelR = QLabel()
        self.pixmapR = QPixmap(studentPicR)
        self.labelR.setPixmap(self.pixmapR)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_CheckOut)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(329, -1, 231, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, -100, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.labelC)


        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_Return)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(329, -1, 231, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutR = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayoutR.setContentsMargins(0, 0, -100, 0)
        self.verticalLayoutR.setObjectName("verticalLayoutR")
        self.verticalLayoutR.addWidget(self.labelR)


        Ui_MainWindow.displayPhoto(self)


    def displayPhoto(self):
        # This function is unused, it was used but there was no clean solution to displaying the images on both tabs
        # As a result, the function remains here for a future fix but is not being called
        currentTab = self.CLR_tabWidget.currentIndex()
        currentIndex = currentTab


        if currentTab == 1:
            self.CLR_tabWidget.setCurrentIndex(2)
            self.labelR.show()
            self.labelC.show()
            QtGui.QGuiApplication.processEvents()
            self.CLR_tabWidget.setCurrentIndex(currentIndex)
        elif currentTab == 0:

            self.labelC.show()
            self.labelR.show()
            QtGui.QGuiApplication.processEvents()
            self.CLR_tabWidget.setCurrentIndex(currentIndex)
        self.labelR.show()



    def fileQuit(self):
        sys.exit(app.exec_())

    def readPickle(self):  # the purpose of this lovely function is to read the '.pickle' file that contains the saved
                           # data for each  ID, the for loops are to clear the table (is it ugly? Very, but it works!)
        for i in range(10):
            try:
                if self.C_tbl_ItemList.item(0, i).text() != '':
                    cell = self.C_tbl_ItemList.item(0, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.C_tbl_ItemList.item(1, i).text() != '':
                    cell = self.C_tbl_ItemList.item(1, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.C_tbl_ItemList.item(1, i).text() != '':
                    cell = self.C_tbl_ItemList.item(1, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.C_tbl_ItemList.item(2, i).text() != '':
                    cell = self.C_tbl_ItemList.item(2, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.C_tbl_ItemList.item(3, i).text() != '':
                    cell = self.C_tbl_ItemList.item(3, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.C_tbl_ItemList.item(4, i).text() != '':
                    cell = self.C_tbl_ItemList.item(4, i)
                    cell.setText('')
            except AttributeError:
                pass

        global newPasted


        buffersize = 64 * 1024
        password = "FBLA_CodingandProgramming_PICKLE"
        pyAesCrypt.decryptFile("dict.pickle.aes", "dict.pickle", password, bufferSize)
        pickle_in = open('dict.pickle', 'rb')
        self.newPasted = pickle.load(pickle_in)

    def readPickle_R(self):
        for i in range(10):
            try:
                if self.R_tbl_ItemList.item(0, i).text() != '':
                    cell = self.R_tbl_ItemList.item(0, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.R_tbl_ItemList.item(1, i).text() != '':
                    cell = self.R_tbl_ItemList.item(1, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.R_tbl_ItemList.item(1, i).text() != '':
                    cell = self.R_tbl_ItemList.item(1, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.R_tbl_ItemList.item(2, i).text() != '':
                    cell = self.R_tbl_ItemList.item(2, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.R_tbl_ItemList.item(3, i).text() != '':
                    cell = self.R_tbl_ItemList.item(3, i)
                    cell.setText('')
            except AttributeError:
                pass
        for i in range(10):
            try:
                if self.R_tbl_ItemList.item(4, i).text() != '':
                    cell = self.R_tbl_ItemList.item(4, i)
                    cell.setText('')
            except AttributeError:
                pass

        global newPastedR
        pickle_in = open('dict.pickle', 'rb')
        self.newPastedR = pickle.load(pickle_in)



    def loadItemsCheckOut(self):

        self.readPickle()
        try:
            listZero = self.newPasted[0]
            self.pickleID = listZero[0].get('ID', 'N/A')
            self.pickleTitle = listZero[0].get('Title', 'N/A')
            self.pickleAuthor = listZero[0].get('Author', 'N/A')
            self.pickleCallNo = listZero[0].get('Call No.', 'N/A')
            self.pickleISBN = listZero[0].get('ISBN', 'N/A')
            self.pickleChkOutDate = listZero[0].get('Check Out Date', 'N/A')
            self.pickleDueDate = listZero[0].get('Due Date', 'N/A')
            self.picklePrice = listZero[0].get('Price', 'N/A')
            self.pickleTotalFine = listZero[0].get('Total Fine', 'N/A')
            self.pickleIsRenewed = listZero[0].get('Renewed?', 'N/A')
            self.pickleIsOverdue = listZero[0].get('Overdue?', 'N/A')


            self.finalID = self.pickleID
            self.finalTitle = self.pickleTitle
            self.finalAuthor = self.pickleAuthor
            self.finalCallNo = self.pickleCallNo
            self.finalISBN = self.pickleISBN
            self.finalChkOutDate = self.pickleChkOutDate
            self.finalDueDate = self.pickleDueDate
            self.finalPrice = self.picklePrice
            self.finalTotalFine = self.pickleTotalFine
            self.finalIsRenewed = self.pickleIsRenewed
            self.finalIsOverdue = self.pickleIsOverdue
            self.insertItems_C()

        except IndexError:
            # This is a dirty, temporary solution to a weird glitch with the pickle file
            # The pickle file begins with "[[{" which completely messes up indexing and trying to access values
            # This is likely due to the initial dict_data set up as a list and then appended to another list
            pass





    def loadItemsReturn(self):
        self.readPickle_R()
    def saveItemListCSV(self):
        csv_col = ['ID', 'Title', 'Author', 'Call No.', 'ISBN', 'Check Out Date', 'Due Date', 'Price', 'Total Fine',
                   'Renewed?', 'Overdue?']
        dict_data = [
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': str(self.finalDueDate),
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
        ]
        def createPickle():
            # This function uses the built-in 'Pickle' module to create a flattened file (converting dict_data to bytes)
            # The pickle file acts as the storage for books tied to each student's ID
            pasted = []
            copied = dict_data.copy()
            pasted.append(copied)

            pickle_out = open('dict.pickle', 'wb')
            pickle.dump(pasted, pickle_out)
            pickle_out.close()

        def encryptPickle():
            # It was recommended to encrypt the storage so pyAesCrypt will be used.
            # Despite the poor practice of hardcoding the password, the password is temporary and could be obfusicated
            #   in the future/
            # The functions to encrypt will be after the creation of the PICKLE files and decrypt functions after
            #   loading in the files.
            buffersize = 64 * 1024
            password = "FBLA_CodingandProgramming_PICKLE"
            pyAesCrypt.encryptFile('dict.pickle', 'dict.pickle.aes', password, buffersize)
        createPickle()
        encryptPickle()

        self.loadItemsCheckOut()

    def saveItemListCSV_R(self):
        csv_col = ['ID', 'Title', 'Author', 'Call No.', 'ISBN', 'Check Out Date', 'Due Date', 'Price', 'Total Fine',
                   'Renewed?', 'Overdue?']
        dict_data = [
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': str(self.finalDueDate),
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
            {'ID': self.finalID, 'Title': self.finalTitle, 'Author': self.finalAuthor, 'Call No.': self.finalCallNo,
             'ISBN': self.finalISBN, 'Check Out Date': self.finalChkOutDate, 'Due Date': self.finalDueDate,
             'Price': self.finalPrice, 'Total Fine': self.finalTotalFine, 'Renewed?': self.finalIsRenewed,
             'Overdue?': self.finalIsOverdue},
        ]

        def createPickle():
            # This function uses the built-in 'Pickle' module to create a flattened file (converting dict_data to bytes)
            # The pickle file acts as the storage for books tied to each student's ID
            pasted = []
            copied = dict_data.copy()
            pasted.append(copied)

            pickle_out = open('dict.pickle', 'wb')
            pickle.dump(pasted, pickle_out)
            pickle_out.close()
        def encryptPickle():
            buffersize = 64 * 1024
            password = "FBLA_CodingandProgramming_PICKLE"
            pyAesCrypt.encryptFile('dict.pickle', 'dict.pickle.aes', password, buffersize)

        createPickle()
        encryptPickle()

        self.loadItemsReturn()





    def confirmCheckOut(self):
        try:
            self.saveItemListCSV()
        except:
            try:
                errorMsgBox = QMessageBox.question(None, 'Error!', "Nothing to check out!",
                                                   QMessageBox.Cancel | QMessageBox.Ignore)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                traceback.print_exc()
                raise

    def confirmReturn(self):
        try:
            self.saveItemListCSV_R()
        except:
            try:
                errorMsgBox = QMessageBox.question(None, 'Error!', "Nothing to return!",
                                                   QMessageBox.Cancel | QMessageBox.Ignore)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                traceback.print_exc()
                raise

    # Thus far, the pickle file is able to save the data but is having trouble loading it back into the table
    # Temporary solution = hope for the best and check Stack Overflow

if __name__ == "__main__":
    import sys
    # This simply creates an instance of the window and defines how to start and quit the application
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())