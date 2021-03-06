# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OvergateExportApp2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.setEnabled(True)
        Dialog.resize(445, 289)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(445, 289))
        Dialog.setMaximumSize(QtCore.QSize(445, 289))
        Dialog.setToolTip("")
        Dialog.setSizeGripEnabled(False)
        self.dateEdit_FROM = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_FROM.setGeometry(QtCore.QRect(20, 90, 101, 21))
        self.dateEdit_FROM.setObjectName("dateEdit_FROM")
        self.comboBox_Cassa = QtWidgets.QComboBox(Dialog)
        self.comboBox_Cassa.setGeometry(QtCore.QRect(150, 40, 111, 22))
        self.comboBox_Cassa.setObjectName("comboBox_Cassa")
        self.comboBox_Filiale = QtWidgets.QComboBox(Dialog)
        self.comboBox_Filiale.setGeometry(QtCore.QRect(20, 40, 111, 22))
        self.comboBox_Filiale.setObjectName("comboBox_Filiale")
        self.dateEdit_TO = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_TO.setGeometry(QtCore.QRect(150, 90, 110, 22))
        self.dateEdit_TO.setObjectName("dateEdit_TO")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox_PPOS = QtWidgets.QCheckBox(Dialog)
        self.checkBox_PPOS.setGeometry(QtCore.QRect(320, 30, 92, 23))
        self.checkBox_PPOS.setChecked(True)
        self.checkBox_PPOS.setObjectName("checkBox_PPOS")
        self.checkBox_OVG = QtWidgets.QCheckBox(Dialog)
        self.checkBox_OVG.setGeometry(QtCore.QRect(320, 60, 92, 23))
        self.checkBox_OVG.setChecked(True)
        self.checkBox_OVG.setObjectName("checkBox_OVG")
        self.checkBox_RTF = QtWidgets.QCheckBox(Dialog)
        self.checkBox_RTF.setGeometry(QtCore.QRect(320, 90, 111, 23))
        self.checkBox_RTF.setChecked(True)
        self.checkBox_RTF.setObjectName("checkBox_RTF")
        self.textEdit_OUT = QtWidgets.QTextEdit(Dialog)
        self.textEdit_OUT.setGeometry(QtCore.QRect(20, 180, 281, 91))
        self.textEdit_OUT.setObjectName("textEdit_OUT")
        self.label_Fil = QtWidgets.QLabel(Dialog)
        self.label_Fil.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_Fil.setObjectName("label_Fil")
        self.label_Cassa = QtWidgets.QLabel(Dialog)
        self.label_Cassa.setGeometry(QtCore.QRect(150, 20, 67, 17))
        self.label_Cassa.setObjectName("label_Cassa")
        self.label_Date = QtWidgets.QLabel(Dialog)
        self.label_Date.setGeometry(QtCore.QRect(20, 70, 241, 17))
        self.label_Date.setObjectName("label_Date")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 140, 271, 21))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(340, 160, 101, 51))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.checkBox_PPOS.setText(_translate("Dialog", "PPOS"))
        self.checkBox_OVG.setText(_translate("Dialog", "Overgate"))
        self.checkBox_RTF.setText(_translate("Dialog", "FiscalPrinter"))
        self.label_Fil.setText(_translate("Dialog", "Filiale"))
        self.label_Cassa.setText(_translate("Dialog", "Cassa"))
        self.label_Date.setText(_translate("Dialog", "Data inizio:                Data fine:"))
        self.checkBox.setText(_translate("Dialog", "Invia email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
