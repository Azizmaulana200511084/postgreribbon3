from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMahasiswa import MahasiswaWindow
from forms.frmMatakuliah import WindowMatakuliah
from forms.frmDosen import WindowDosen
from forms.frmAlumni import WindowAlumni
dock = QtWidgets.QDockWidget()
def child_panels(self):   
    matakuliah_panel(self)
    mahasiswa_panel(self)
    dosen_panel(self)
    alumni_panel(self)

def mahasiswa_panel(self):     
    mahasiswa_widget = MahasiswaWindow()
    mahasiswa_widget.select_data()
    self.centralwidget = mahasiswa_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)
        
def matakuliah_panel(self):
    matakuliah_widget = WindowMatakuliah()
    matakuliah_widget.select_data()
    self.centralwidget = matakuliah_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def dosen_panel(self):
    dosen_widget = WindowDosen()
    dosen_widget.select_data()
    self.centralwidget = dosen_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def alumni_panel(self):
    alumni_widget = WindowDosen()
    alumni_widget.select_data()
    self.centralwidget = alumni_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def mahasiswa_on(self):
    mahasiswa_widget = MahasiswaWindow()
    mahasiswa_widget.select_data()
    self.centralwidget = mahasiswa_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def matakuliah_on(self):
    matakuliah_widget = WindowMatakuliah()
    matakuliah_widget.select_data()
    self.centralwidget = matakuliah_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def dosen_on(self):
    dosen_widget = WindowDosen()
    dosen_widget.select_data()
    self.centralwidget = dosen_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def alumni_on(self):
    alumni_widget = WindowAlumni()
    alumni_widget.select_data()
    self.centralwidget = alumni_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()




        
     