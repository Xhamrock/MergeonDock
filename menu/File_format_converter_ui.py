# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File_format_converter_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(308, 392)
        self.gridLayout_dialog = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_dialog.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_dialog.setObjectName("gridLayout_dialog")
        self.widget_main = QtWidgets.QWidget(Dialog)
        self.widget_main.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.widget_main.setObjectName("widget_main")
        self.gridLayout_widget = QtWidgets.QGridLayout(self.widget_main)
        self.gridLayout_widget.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_widget.setObjectName("gridLayout_widget")
        self.comboBox_format = QtWidgets.QComboBox(self.widget_main)
        self.comboBox_format.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox_format.setObjectName("comboBox_format")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.gridLayout_widget.addWidget(self.comboBox_format, 2, 0, 1, 2)
        self.pushButton_convert = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_convert.setStyleSheet("font: bold 14pt \"微軟正黑體\"; color:rgb(100, 100, 100);\n"
"background-color: rgb(30, 30, 30);")
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.gridLayout_widget.addWidget(self.pushButton_convert, 3, 1, 1, 1)
        self.tableWidget_file_list = QtWidgets.QTableWidget(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_file_list.sizePolicy().hasHeightForWidth())
        self.tableWidget_file_list.setSizePolicy(sizePolicy)
        self.tableWidget_file_list.setAutoFillBackground(False)
        self.tableWidget_file_list.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.tableWidget_file_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_file_list.setRowCount(0)
        self.tableWidget_file_list.setObjectName("tableWidget_file_list")
        self.tableWidget_file_list.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_file_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_file_list.setHorizontalHeaderItem(1, item)
        self.tableWidget_file_list.horizontalHeader().setVisible(True)
        self.tableWidget_file_list.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout_widget.addWidget(self.tableWidget_file_list, 1, 0, 1, 2)
        self.checkBox_customize_output_folder = QtWidgets.QCheckBox(self.widget_main)
        self.checkBox_customize_output_folder.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_customize_output_folder.setObjectName("checkBox_customize_output_folder")
        self.gridLayout_widget.addWidget(self.checkBox_customize_output_folder, 3, 0, 1, 1)
        self.pushButton_file_upload = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_file_upload.setStyleSheet("font: bold 12pt \"微軟正黑體\"; color:rgb(255, 255, 255); \n"
"background-color: rgb(60, 60, 60)")
        self.pushButton_file_upload.setObjectName("pushButton_file_upload")
        self.gridLayout_widget.addWidget(self.pushButton_file_upload, 0, 0, 1, 1)
        self.pushButton_clearall = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_clearall.setStyleSheet("font: bold 12pt \"微軟正黑體\"; color:rgb(255, 255, 255); \n"
"background-color: rgb(60, 60, 60)")
        self.pushButton_clearall.setObjectName("pushButton_clearall")
        self.gridLayout_widget.addWidget(self.pushButton_clearall, 0, 1, 1, 1)
        self.gridLayout_dialog.addWidget(self.widget_main, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Format convert (Openbabel 3.1)"))
        self.comboBox_format.setItemText(0, _translate("Dialog", "mol"))
        self.comboBox_format.setItemText(1, _translate("Dialog", "pdb"))
        self.comboBox_format.setItemText(2, _translate("Dialog", "pdbqt"))
        self.pushButton_convert.setText(_translate("Dialog", "Convert"))
        item = self.tableWidget_file_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "File name"))
        item = self.tableWidget_file_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Format"))
        self.checkBox_customize_output_folder.setText(_translate("Dialog", "Customize output folder"))
        self.pushButton_file_upload.setText(_translate("Dialog", "Files upload"))
        self.pushButton_clearall.setText(_translate("Dialog", "Clear all"))
