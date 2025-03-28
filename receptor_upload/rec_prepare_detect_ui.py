# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec_prepare_detect_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rec_prepare_detect(object):
    def setupUi(self, rec_prepare_detect):
        rec_prepare_detect.setObjectName("rec_prepare_detect")
        rec_prepare_detect.resize(626, 373)
        self.gridLayout_rec_prepare_detect = QtWidgets.QGridLayout(rec_prepare_detect)
        self.gridLayout_rec_prepare_detect.setObjectName("gridLayout_rec_prepare_detect")
        self.tableWidget_sequence_detect = QtWidgets.QTableWidget(rec_prepare_detect)
        self.tableWidget_sequence_detect.setStyleSheet("")
        self.tableWidget_sequence_detect.setObjectName("tableWidget_sequence_detect")
        self.tableWidget_sequence_detect.setColumnCount(6)
        self.tableWidget_sequence_detect.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_sequence_detect.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sequence_detect.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sequence_detect.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tableWidget_sequence_detect.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tableWidget_sequence_detect.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tableWidget_sequence_detect.setHorizontalHeaderItem(5, item)
        self.gridLayout_rec_prepare_detect.addWidget(self.tableWidget_sequence_detect, 0, 0, 1, 3)
        self.pushButton_Abort = QtWidgets.QPushButton(rec_prepare_detect)
        self.pushButton_Abort.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_Abort.setStyleSheet("font: 11pt \"Arial\";")
        self.pushButton_Abort.setObjectName("pushButton_Abort")
        self.gridLayout_rec_prepare_detect.addWidget(self.pushButton_Abort, 1, 0, 1, 1)
        self.pushButton_Skip_preparation = QtWidgets.QPushButton(rec_prepare_detect)
        self.pushButton_Skip_preparation.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_Skip_preparation.setToolTipDuration(-1)
        self.pushButton_Skip_preparation.setStatusTip("")
        self.pushButton_Skip_preparation.setWhatsThis("")
        self.pushButton_Skip_preparation.setStyleSheet("font: 11pt \"Arial\";")
        self.pushButton_Skip_preparation.setObjectName("pushButton_Skip_preparation")
        self.gridLayout_rec_prepare_detect.addWidget(self.pushButton_Skip_preparation, 1, 1, 1, 1)
        self.pushButton_Contiune = QtWidgets.QPushButton(rec_prepare_detect)
        self.pushButton_Contiune.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_Contiune.setStyleSheet("font: 11pt \"Arial\";")
        self.pushButton_Contiune.setObjectName("pushButton_Contiune")
        self.gridLayout_rec_prepare_detect.addWidget(self.pushButton_Contiune, 1, 2, 1, 1)

        self.retranslateUi(rec_prepare_detect)
        QtCore.QMetaObject.connectSlotsByName(rec_prepare_detect)

    def retranslateUi(self, rec_prepare_detect):
        _translate = QtCore.QCoreApplication.translate
        rec_prepare_detect.setWindowTitle(_translate("rec_prepare_detect", "Sequence detect system"))
        item = self.tableWidget_sequence_detect.horizontalHeaderItem(0)
        item.setText(_translate("rec_prepare_detect", "Sequence"))
        item = self.tableWidget_sequence_detect.horizontalHeaderItem(1)
        item.setText(_translate("rec_prepare_detect", "Chain"))
        item = self.tableWidget_sequence_detect.horizontalHeaderItem(2)
        item.setText(_translate("rec_prepare_detect", "Discription"))
        item = self.tableWidget_sequence_detect.horizontalHeaderItem(3)
        item.setText(_translate("rec_prepare_detect", "Ref. ligand"))
        item = self.tableWidget_sequence_detect.horizontalHeaderItem(4)
        item.setText(_translate("rec_prepare_detect", "Preserve"))
        item.setToolTip(_translate("rec_prepare_detect", "<html><head/><body><p>Preserve sequence in preparation steps (keep this sequence in pdbqt format, not always works because some structure is complicated)</p></body></html>"))
        item = self.tableWidget_sequence_detect.horizontalHeaderItem(5)
        item.setText(_translate("rec_prepare_detect", "Remove"))
        self.pushButton_Abort.setText(_translate("rec_prepare_detect", "Abort"))
        self.pushButton_Skip_preparation.setToolTip(_translate("rec_prepare_detect", "<html><head/><body><p><span style=\" color:#a20000;\">Skip any preparation steps, only load original file for manual edit or view</span></p></body></html>"))
        self.pushButton_Skip_preparation.setText(_translate("rec_prepare_detect", "Skip preparation"))
        self.pushButton_Contiune.setText(_translate("rec_prepare_detect", "Continue"))
