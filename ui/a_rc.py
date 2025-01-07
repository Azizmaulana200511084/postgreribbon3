# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alumni.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 230, 981, 311))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(124, 0, 0);")
        self.frame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame.setObjectName("frame")
        self.txtNama = QtWidgets.QLineEdit(self.frame)
        self.txtNama.setGeometry(QtCore.QRect(120, 70, 201, 20))
        self.txtNama.setStyleSheet("color: rgb(255, 255, 255);")
        self.txtNama.setObjectName("txtNama")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.cboTelepon = QtWidgets.QLineEdit(self.frame)
        self.cboTelepon.setGeometry(QtCore.QRect(770, 100, 191, 20))
        self.cboTelepon.setStyleSheet("color: rgb(255, 255, 255);")
        self.cboTelepon.setObjectName("cboTelepon")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(340, 90, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.optPerempuan = QtWidgets.QRadioButton(self.frame)
        self.optPerempuan.setGeometry(QtCore.QRect(250, 100, 82, 17))
        self.optPerempuan.setStyleSheet("color: rgb(255, 255, 255);")
        self.optPerempuan.setObjectName("optPerempuan")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(670, 100, 91, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.btnClear = QtWidgets.QPushButton(self.frame)
        self.btnClear.setGeometry(QtCore.QRect(460, 120, 75, 23))
        self.btnClear.setStyleSheet("#btnClear{\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.btnClear.setObjectName("btnClear")
        self.cboJabatan = QtWidgets.QComboBox(self.frame)
        self.cboJabatan.setGeometry(QtCore.QRect(120, 120, 201, 22))
        self.cboJabatan.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.cboJabatan.setObjectName("cboJabatan")
        self.cboJabatan.addItem("")
        self.cboJabatan.setItemText(0, "")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.cboJabatan.addItem("")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(670, 70, 91, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(670, 40, 91, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.btnSimpan = QtWidgets.QPushButton(self.frame)
        self.btnSimpan.setGeometry(QtCore.QRect(380, 120, 75, 23))
        self.btnSimpan.setStyleSheet("#btnSimpan{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 255);\n"
"}")
        self.btnSimpan.setObjectName("btnSimpan")
        self.btnCari = QtWidgets.QPushButton(self.frame)
        self.btnCari.setGeometry(QtCore.QRect(280, 40, 41, 23))
        self.btnCari.setObjectName("btnCari")
        self.cboEmail = QtWidgets.QLineEdit(self.frame)
        self.cboEmail.setGeometry(QtCore.QRect(770, 130, 191, 20))
        self.cboEmail.setStyleSheet("color: rgb(255, 255, 255);")
        self.cboEmail.setObjectName("cboEmail")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(520, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(430, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.txtKODEALUMNI = QtWidgets.QLineEdit(self.frame)
        self.txtKODEALUMNI.setGeometry(QtCore.QRect(120, 40, 151, 20))
        self.txtKODEALUMNI.setStyleSheet("color: rgb(255, 255, 255);")
        self.txtKODEALUMNI.setObjectName("txtKODEALUMNI")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(670, 130, 91, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.cboBekerjaSejak = QtWidgets.QLineEdit(self.frame)
        self.cboBekerjaSejak.setGeometry(QtCore.QRect(770, 70, 191, 20))
        self.cboBekerjaSejak.setStyleSheet("color: rgb(255, 255, 255);")
        self.cboBekerjaSejak.setObjectName("cboBekerjaSejak")
        self.btnHapus = QtWidgets.QPushButton(self.frame)
        self.btnHapus.setGeometry(QtCore.QRect(540, 120, 75, 23))
        self.btnHapus.setStyleSheet("#btnHapus{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnHapus.setObjectName("btnHapus")
        self.cboKerja = QtWidgets.QLineEdit(self.frame)
        self.cboKerja.setGeometry(QtCore.QRect(770, 40, 191, 20))
        self.cboKerja.setStyleSheet("color: rgb(255, 255, 255);")
        self.cboKerja.setObjectName("cboKerja")
        self.optLaki = QtWidgets.QRadioButton(self.frame)
        self.optLaki.setGeometry(QtCore.QRect(120, 100, 82, 17))
        self.optLaki.setStyleSheet("color: rgb(255, 255, 255);")
        self.optLaki.setObjectName("optLaki")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridAlumni = QtWidgets.QTableWidget(self.frame)
        self.gridAlumni.setGeometry(QtCore.QRect(20, 160, 941, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.gridAlumni.setFont(font)
        self.gridAlumni.setAutoFillBackground(False)
        self.gridAlumni.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.gridAlumni.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gridAlumni.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridAlumni.setLineWidth(1)
        self.gridAlumni.setGridStyle(QtCore.Qt.SolidLine)
        self.gridAlumni.setCornerButtonEnabled(True)
        self.gridAlumni.setRowCount(10)
        self.gridAlumni.setColumnCount(9)
        self.gridAlumni.setObjectName("gridAlumni")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.gridAlumni.setItem(0, 0, item)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(410, 110, 161, 111))
        self.frame_2.setStyleSheet("border-image: url(:/a/a.jpg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "KODE ALUMNI"))
        self.label_10.setText(_translate("MainWindow", "AZIZ MAULANA"))
        self.label_5.setText(_translate("MainWindow", "Jabatan"))
        self.optPerempuan.setText(_translate("MainWindow", "Perempuan"))
        self.label_8.setText(_translate("MainWindow", "Telepon"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.cboJabatan.setItemText(1, _translate("MainWindow", "Direktur Utama"))
        self.cboJabatan.setItemText(2, _translate("MainWindow", "Direktur"))
        self.cboJabatan.setItemText(3, _translate("MainWindow", "Direktur Keuangan"))
        self.cboJabatan.setItemText(4, _translate("MainWindow", "Direktur Personalia"))
        self.cboJabatan.setItemText(5, _translate("MainWindow", "Manager"))
        self.cboJabatan.setItemText(6, _translate("MainWindow", "Manager Personalia"))
        self.cboJabatan.setItemText(7, _translate("MainWindow", "Manager Pemasaran"))
        self.cboJabatan.setItemText(8, _translate("MainWindow", "Administrasi Gudang"))
        self.label_7.setText(_translate("MainWindow", "Bekerja Sejak"))
        self.label_6.setText(_translate("MainWindow", "Tempat Kerja"))
        self.btnSimpan.setText(_translate("MainWindow", "Simpan"))
        self.btnCari.setText(_translate("MainWindow", "cari"))
        self.label_11.setText(_translate("MainWindow", "200511084"))
        self.label.setText(_translate("MainWindow", "Data Alumni"))
        self.label_9.setText(_translate("MainWindow", "Email"))
        self.btnHapus.setText(_translate("MainWindow", "Hapus"))
        self.optLaki.setText(_translate("MainWindow", "Laki-laki"))
        self.label_4.setText(_translate("MainWindow", "Jenis Kelamin"))
        self.label_3.setText(_translate("MainWindow", "Nama Lengkap"))
        __sortingEnabled = self.gridAlumni.isSortingEnabled()
        self.gridAlumni.setSortingEnabled(False)
        self.gridAlumni.setSortingEnabled(__sortingEnabled)
import a_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())