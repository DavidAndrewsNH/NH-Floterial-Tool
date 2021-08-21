import math
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(330, 130, 71, 141))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_10 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.state_deviation_pop = QtWidgets.QTextEdit(self.splitter_4)
        self.state_deviation_pop.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state_deviation_pop.setFont(font)
        self.state_deviation_pop.setReadOnly(True)
        self.state_deviation_pop.setObjectName("state_deviation_pop")
        self.label_12 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.county_deviation_pop = QtWidgets.QTextEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.county_deviation_pop.setFont(font)
        self.county_deviation_pop.setReadOnly(True)
        self.county_deviation_pop.setObjectName("county_deviation_pop")
        self.County_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.County_comboBox.setGeometry(QtCore.QRect(20, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.County_comboBox.setFont(font)
        self.County_comboBox.setObjectName("County_comboBox")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.County_comboBox.addItem("")
        self.Population_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Population_comboBox.setGeometry(QtCore.QRect(180, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Population_comboBox.setFont(font)
        self.Population_comboBox.setObjectName("Population_comboBox")
        self.Population_comboBox.addItem("")
        self.Population_comboBox.addItem("")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 60, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(180, 60, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setGeometry(QtCore.QRect(230, 130, 81, 141))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_18 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.state_deviation_per = QtWidgets.QTextEdit(self.splitter_5)
        self.state_deviation_per.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state_deviation_per.setFont(font)
        self.state_deviation_per.setReadOnly(True)
        self.state_deviation_per.setObjectName("state_deviation_per")
        self.label_20 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.county_deviation_per = QtWidgets.QTextEdit(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.county_deviation_per.setFont(font)
        self.county_deviation_per.setReadOnly(True)
        self.county_deviation_per.setObjectName("county_deviation_per")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 60, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.NumOfReps_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NumOfReps_3.setGeometry(QtCore.QRect(370, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumOfReps_3.setFont(font)
        self.NumOfReps_3.setObjectName("NumOfReps_3")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(520, 130, 81, 141))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.state_target_onerep = QtWidgets.QTextEdit(self.splitter_3)
        self.state_target_onerep.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state_target_onerep.setFont(font)
        self.state_target_onerep.setReadOnly(True)
        self.state_target_onerep.setObjectName("state_target_onerep")
        self.label_21 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.county_target_onerep = QtWidgets.QTextEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.county_target_onerep.setFont(font)
        self.county_target_onerep.setReadOnly(True)
        self.county_target_onerep.setObjectName("county_target_onerep")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 130, 81, 141))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NumOfReps = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumOfReps.setFont(font)
        self.NumOfReps.setObjectName("NumOfReps")
        self.checkBox = QtWidgets.QCheckBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Population = QtWidgets.QLineEdit(self.splitter)
        self.Population.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population.setFont(font)
        self.Population.setText("")
        self.Population.setReadOnly(True)
        self.Population.setObjectName("Population")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(120, 130, 91, 141))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.state_target_pop = QtWidgets.QTextEdit(self.splitter_2)
        self.state_target_pop.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state_target_pop.setFont(font)
        self.state_target_pop.setReadOnly(True)
        self.state_target_pop.setObjectName("state_target_pop")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.county_target_pop = QtWidgets.QTextEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.county_target_pop.setFont(font)
        self.county_target_pop.setReadOnly(True)
        self.county_target_pop.setObjectName("county_target_pop")
        self.splitter_6 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_6.setGeometry(QtCore.QRect(420, 130, 81, 141))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.label_15 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_22 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.state_deviation_pop_2 = QtWidgets.QTextEdit(self.splitter_6)
        self.state_deviation_pop_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state_deviation_pop_2.setFont(font)
        self.state_deviation_pop_2.setReadOnly(True)
        self.state_deviation_pop_2.setObjectName("state_deviation_pop_2")
        self.label_23 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.county_deviation_pop_2 = QtWidgets.QTextEdit(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.county_deviation_pop_2.setFont(font)
        self.county_deviation_pop_2.setReadOnly(True)
        self.county_deviation_pop_2.setObjectName("county_deviation_pop_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(780, 60, 151, 711))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(50)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.verticalHeader().setVisible(True)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(480, 460, 291, 301))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../../../.designer/backup/ComponentMethod2.PNG"))
        self.label_13.setObjectName("label_13")
        self.Dev_Target = QtWidgets.QLineEdit(self.centralwidget)
        self.Dev_Target.setEnabled(True)
        self.Dev_Target.setGeometry(QtCore.QRect(640, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev_Target.setFont(font)
        self.Dev_Target.setText("")
        self.Dev_Target.setObjectName("Dev_Target")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(510, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 310, 451, 529))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Dev4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev4.setFont(font)
        self.Dev4.setText("")
        self.Dev4.setReadOnly(True)
        self.Dev4.setObjectName("Dev4")
        self.gridLayout.addWidget(self.Dev4, 7, 3, 1, 1)
        self.Dev5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev5.setFont(font)
        self.Dev5.setText("")
        self.Dev5.setReadOnly(True)
        self.Dev5.setObjectName("Dev5")
        self.gridLayout.addWidget(self.Dev5, 9, 3, 1, 1)
        self.Dev6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev6.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev6.setFont(font)
        self.Dev6.setText("")
        self.Dev6.setReadOnly(True)
        self.Dev6.setObjectName("Dev6")
        self.gridLayout.addWidget(self.Dev6, 11, 3, 1, 1)
        self.Dev3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev3.setFont(font)
        self.Dev3.setText("")
        self.Dev3.setReadOnly(True)
        self.Dev3.setObjectName("Dev3")
        self.gridLayout.addWidget(self.Dev3, 5, 3, 1, 1)
        self.Dev7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev7.setFont(font)
        self.Dev7.setText("")
        self.Dev7.setReadOnly(True)
        self.Dev7.setObjectName("Dev7")
        self.gridLayout.addWidget(self.Dev7, 13, 3, 1, 1)
        self.Max_Dev2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev2.setFont(font)
        self.Max_Dev2.setText("")
        self.Max_Dev2.setReadOnly(True)
        self.Max_Dev2.setObjectName("Max_Dev2")
        self.gridLayout.addWidget(self.Max_Dev2, 3, 4, 1, 1)
        self.Dev8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev8.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev8.setFont(font)
        self.Dev8.setText("")
        self.Dev8.setReadOnly(True)
        self.Dev8.setObjectName("Dev8")
        self.gridLayout.addWidget(self.Dev8, 15, 3, 1, 1)
        self.Max_Dev1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev1.setFont(font)
        self.Max_Dev1.setText("")
        self.Max_Dev1.setReadOnly(True)
        self.Max_Dev1.setObjectName("Max_Dev1")
        self.gridLayout.addWidget(self.Max_Dev1, 1, 4, 1, 1)
        self.Max_Dev4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev4.setFont(font)
        self.Max_Dev4.setText("")
        self.Max_Dev4.setReadOnly(True)
        self.Max_Dev4.setObjectName("Max_Dev4")
        self.gridLayout.addWidget(self.Max_Dev4, 7, 4, 1, 1)
        self.Max_Dev5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev5.setFont(font)
        self.Max_Dev5.setText("")
        self.Max_Dev5.setReadOnly(True)
        self.Max_Dev5.setObjectName("Max_Dev5")
        self.gridLayout.addWidget(self.Max_Dev5, 9, 4, 1, 1)
        self.Max_Dev3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev3.setFont(font)
        self.Max_Dev3.setText("")
        self.Max_Dev3.setReadOnly(True)
        self.Max_Dev3.setObjectName("Max_Dev3")
        self.gridLayout.addWidget(self.Max_Dev3, 5, 4, 1, 1)
        self.Max_Dev8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev8.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev8.setFont(font)
        self.Max_Dev8.setText("")
        self.Max_Dev8.setReadOnly(True)
        self.Max_Dev8.setObjectName("Max_Dev8")
        self.gridLayout.addWidget(self.Max_Dev8, 15, 4, 1, 1)
        self.Max_Dev7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev7.setFont(font)
        self.Max_Dev7.setText("")
        self.Max_Dev7.setReadOnly(True)
        self.Max_Dev7.setObjectName("Max_Dev7")
        self.gridLayout.addWidget(self.Max_Dev7, 13, 4, 1, 1)
        self.Max_Dev6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Max_Dev6.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Max_Dev6.setFont(font)
        self.Max_Dev6.setText("")
        self.Max_Dev6.setReadOnly(True)
        self.Max_Dev6.setObjectName("Max_Dev6")
        self.gridLayout.addWidget(self.Max_Dev6, 11, 4, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 0, 3, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 0, 4, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.gridLayout.addWidget(self.label_63, 2, 3, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.gridLayout.addWidget(self.label_56, 6, 3, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.gridLayout.addWidget(self.label_64, 4, 3, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.gridLayout.addWidget(self.label_65, 8, 3, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.gridLayout.addWidget(self.label_66, 12, 3, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.gridLayout.addWidget(self.label_69, 2, 4, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.gridLayout.addWidget(self.label_75, 12, 4, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.gridLayout.addWidget(self.label_74, 8, 4, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout.addWidget(self.label_71, 10, 4, 1, 1)
        self.Dev2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev2.setFont(font)
        self.Dev2.setText("")
        self.Dev2.setReadOnly(True)
        self.Dev2.setObjectName("Dev2")
        self.gridLayout.addWidget(self.Dev2, 3, 3, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.gridLayout.addWidget(self.label_67, 14, 3, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.gridLayout.addWidget(self.label_68, 10, 3, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.gridLayout.addWidget(self.label_70, 4, 4, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout.addWidget(self.label_73, 6, 4, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout.addWidget(self.label_72, 14, 4, 1, 1)
        self.NumReps8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps8.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps8.setFont(font)
        self.NumReps8.setText("")
        self.NumReps8.setReadOnly(True)
        self.NumReps8.setObjectName("NumReps8")
        self.gridLayout.addWidget(self.NumReps8, 15, 1, 1, 1)
        self.Population_8 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_8.setFont(font)
        self.Population_8.setText("")
        self.Population_8.setObjectName("Population_8")
        self.gridLayout.addWidget(self.Population_8, 15, 0, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.gridLayout.addWidget(self.label_58, 12, 1, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.gridLayout.addWidget(self.label_53, 10, 2, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 2, 0, 1, 1)
        self.Min_Dev2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev2.setFont(font)
        self.Min_Dev2.setText("")
        self.Min_Dev2.setReadOnly(True)
        self.Min_Dev2.setObjectName("Min_Dev2")
        self.gridLayout.addWidget(self.Min_Dev2, 3, 2, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 8, 1, 1, 1)
        self.Min_Dev3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev3.setFont(font)
        self.Min_Dev3.setText("")
        self.Min_Dev3.setReadOnly(True)
        self.Min_Dev3.setObjectName("Min_Dev3")
        self.gridLayout.addWidget(self.Min_Dev3, 5, 2, 1, 1)
        self.NumReps2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps2.setFont(font)
        self.NumReps2.setText("")
        self.NumReps2.setReadOnly(True)
        self.NumReps2.setObjectName("NumReps2")
        self.gridLayout.addWidget(self.NumReps2, 3, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 6, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 6, 1, 1, 1)
        self.Min_Dev5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev5.setFont(font)
        self.Min_Dev5.setText("")
        self.Min_Dev5.setReadOnly(True)
        self.Min_Dev5.setObjectName("Min_Dev5")
        self.gridLayout.addWidget(self.Min_Dev5, 9, 2, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.gridLayout.addWidget(self.label_52, 10, 1, 1, 1)
        self.NumReps5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps5.setFont(font)
        self.NumReps5.setText("")
        self.NumReps5.setReadOnly(True)
        self.NumReps5.setObjectName("NumReps5")
        self.gridLayout.addWidget(self.NumReps5, 9, 1, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.gridLayout.addWidget(self.label_54, 10, 0, 1, 1)
        self.NumReps1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps1.setFont(font)
        self.NumReps1.setText("")
        self.NumReps1.setReadOnly(True)
        self.NumReps1.setObjectName("NumReps1")
        self.gridLayout.addWidget(self.NumReps1, 1, 1, 1, 1)
        self.Population_4 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_4.setFont(font)
        self.Population_4.setText("")
        self.Population_4.setObjectName("Population_4")
        self.gridLayout.addWidget(self.Population_4, 7, 0, 1, 1)
        self.NumReps3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps3.setFont(font)
        self.NumReps3.setText("")
        self.NumReps3.setReadOnly(True)
        self.NumReps3.setObjectName("NumReps3")
        self.gridLayout.addWidget(self.NumReps3, 5, 1, 1, 1)
        self.Population_5 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_5.setFont(font)
        self.Population_5.setText("")
        self.Population_5.setObjectName("Population_5")
        self.gridLayout.addWidget(self.Population_5, 9, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 8, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 0, 2, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 2, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 0, 0, 1, 1)
        self.NumReps4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps4.setFont(font)
        self.NumReps4.setText("")
        self.NumReps4.setReadOnly(True)
        self.NumReps4.setObjectName("NumReps4")
        self.gridLayout.addWidget(self.NumReps4, 7, 1, 1, 1)
        self.Population_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_2.setFont(font)
        self.Population_2.setText("")
        self.Population_2.setObjectName("Population_2")
        self.gridLayout.addWidget(self.Population_2, 3, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 4, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 6, 2, 1, 1)
        self.Population_1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_1.setFont(font)
        self.Population_1.setText("")
        self.Population_1.setObjectName("Population_1")
        self.gridLayout.addWidget(self.Population_1, 1, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 8, 2, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 4, 2, 1, 1)
        self.Min_Dev1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev1.setFont(font)
        self.Min_Dev1.setText("")
        self.Min_Dev1.setReadOnly(True)
        self.Min_Dev1.setObjectName("Min_Dev1")
        self.gridLayout.addWidget(self.Min_Dev1, 1, 2, 1, 1)
        self.Min_Dev4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev4.setFont(font)
        self.Min_Dev4.setText("")
        self.Min_Dev4.setReadOnly(True)
        self.Min_Dev4.setObjectName("Min_Dev4")
        self.gridLayout.addWidget(self.Min_Dev4, 7, 2, 1, 1)
        self.Population_3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_3.setFont(font)
        self.Population_3.setText("")
        self.Population_3.setObjectName("Population_3")
        self.gridLayout.addWidget(self.Population_3, 5, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 2, 1, 1, 1)
        self.Min_Dev8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev8.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev8.setFont(font)
        self.Min_Dev8.setText("")
        self.Min_Dev8.setReadOnly(True)
        self.Min_Dev8.setObjectName("Min_Dev8")
        self.gridLayout.addWidget(self.Min_Dev8, 15, 2, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.gridLayout.addWidget(self.label_59, 12, 2, 1, 1)
        self.Min_Dev7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev7.setFont(font)
        self.Min_Dev7.setText("")
        self.Min_Dev7.setReadOnly(True)
        self.Min_Dev7.setObjectName("Min_Dev7")
        self.gridLayout.addWidget(self.Min_Dev7, 13, 2, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.gridLayout.addWidget(self.label_61, 14, 1, 1, 1)
        self.NumReps7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps7.setFont(font)
        self.NumReps7.setText("")
        self.NumReps7.setReadOnly(True)
        self.NumReps7.setObjectName("NumReps7")
        self.gridLayout.addWidget(self.NumReps7, 13, 1, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.gridLayout.addWidget(self.label_62, 14, 2, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.gridLayout.addWidget(self.label_60, 14, 0, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 12, 0, 1, 1)
        self.Population_6 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_6.setFont(font)
        self.Population_6.setText("")
        self.Population_6.setObjectName("Population_6")
        self.gridLayout.addWidget(self.Population_6, 11, 0, 1, 1)
        self.Population_7 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Population_7.setFont(font)
        self.Population_7.setText("")
        self.Population_7.setObjectName("Population_7")
        self.gridLayout.addWidget(self.Population_7, 13, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 4, 0, 1, 1)
        self.NumReps6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NumReps6.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NumReps6.setFont(font)
        self.NumReps6.setText("")
        self.NumReps6.setReadOnly(True)
        self.NumReps6.setObjectName("NumReps6")
        self.gridLayout.addWidget(self.NumReps6, 11, 1, 1, 1)
        self.Min_Dev6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Min_Dev6.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Min_Dev6.setFont(font)
        self.Min_Dev6.setText("")
        self.Min_Dev6.setReadOnly(True)
        self.Min_Dev6.setObjectName("Min_Dev6")
        self.gridLayout.addWidget(self.Min_Dev6, 11, 2, 1, 1)
        self.Dev1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Dev1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev1.setFont(font)
        self.Dev1.setText("")
        self.Dev1.setReadOnly(True)
        self.Dev1.setObjectName("Dev1")
        self.gridLayout.addWidget(self.Dev1, 1, 3, 1, 1)
        self.Total_Min_Dev = QtWidgets.QLineEdit(self.centralwidget)
        self.Total_Min_Dev.setEnabled(True)
        self.Total_Min_Dev.setGeometry(QtCore.QRect(640, 400, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Total_Min_Dev.setFont(font)
        self.Total_Min_Dev.setText("")
        self.Total_Min_Dev.setReadOnly(True)
        self.Total_Min_Dev.setObjectName("Total_Min_Dev")
        self.label_76 = QtWidgets.QLabel(self.centralwidget)
        self.label_76.setGeometry(QtCore.QRect(490, 400, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(640, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(520, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.Dev_Target_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Dev_Target_2.setEnabled(True)
        self.Dev_Target_2.setGeometry(QtCore.QRect(640, 320, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Dev_Target_2.setFont(font)
        self.Dev_Target_2.setText("")
        self.Dev_Target_2.setObjectName("Dev_Target_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget.raise_()
        self.splitter_4.raise_()
        self.County_comboBox.raise_()
        self.Population_comboBox.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.splitter_5.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.NumOfReps_3.raise_()
        self.splitter_3.raise_()
        self.splitter.raise_()
        self.splitter_2.raise_()
        self.splitter_6.raise_()
        self.tableWidget.raise_()
        self.label_13.raise_()
        self.Dev_Target.raise_()
        self.label_50.raise_()
        self.Total_Min_Dev.raise_()
        self.label_76.raise_()
        self.label_14.raise_()
        self.label_51.raise_()
        self.Dev_Target_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Population.setText('0')
        self.Population_1.setText('0')
        self.NumReps1.setText('0')
        self.Min_Dev1.setText('0')
        self.Dev1.setText('0')
        self.Max_Dev1.setText('0')
        self.Population_2.setText('0')
        self.NumReps2.setText('0')
        self.Min_Dev2.setText('0')
        self.Dev2.setText('0')
        self.Max_Dev2.setText('0')
        self.Population_3.setText('0')
        self.NumReps3.setText('0')
        self.Min_Dev3.setText('0')
        self.Dev3.setText('0')
        self.Max_Dev3.setText('0')
        self.Population_4.setText('0')
        self.NumReps4.setText('0')
        self.Min_Dev4.setText('0')
        self.Dev4.setText('0')
        self.Max_Dev4.setText('0')
        self.Population_5.setText('0')
        self.NumReps5.setText('0')
        self.Min_Dev5.setText('0')
        self.Dev5.setText('0')
        self.Max_Dev5.setText('0')
        self.Population_6.setText('0')
        self.NumReps6.setText('0')
        self.Min_Dev6.setText('0')
        self.Dev6.setText('0')
        self.Max_Dev6.setText('0')
        self.Population_7.setText('0')
        self.NumReps7.setText('0')
        self.Min_Dev7.setText('0')
        self.Dev7.setText('0')
        self.Max_Dev7.setText('0')
        self.Population_8.setText('0')
        self.NumReps8.setText('0')
        self.Min_Dev8.setText('0')
        self.Dev8.setText('0')
        self.Max_Dev8.setText('0')
        self.Dev_Target_2.setText('0')
        self.Dev_Target.setText('0')
        self.Total_Min_Dev.setText('0')

        self.NumOfReps.setText('0')
        self.NumOfReps_3.setPlainText('18')
        self.state_target_pop.setPlainText(('3291'))
        self.county_target_pop.setPlainText('3338')
        self.state_target_onerep.setPlainText('3291')
        self.county_target_onerep.setPlainText('3338')

        self.NumOfReps_3.setStyleSheet('background-color: lightgrey;')
        self.Population.setStyleSheet('background-color: lightgrey;')
        self.state_target_pop.setStyleSheet('background-color: lightgrey;')
        self.county_target_pop.setStyleSheet('background-color: lightgrey;')
        self.state_deviation_per.setStyleSheet('background-color: lightgrey;')
        self.county_deviation_per.setStyleSheet('background-color: lightgrey;')
        self.state_deviation_pop.setStyleSheet('background-color: lightgrey;')
        self.county_deviation_pop.setStyleSheet('background-color: lightgrey;')
        self.state_deviation_pop_2.setStyleSheet('background-color: lightgrey;')
        self.county_deviation_pop_2.setStyleSheet('background-color: lightgrey;')
        self.state_target_onerep.setStyleSheet('background-color: lightgrey;')
        self.county_target_onerep.setStyleSheet('background-color: lightgrey;')
        self.NumReps1.setStyleSheet('background-color: lightgrey;')
        self.NumReps2.setStyleSheet('background-color: lightgrey;')
        self.NumReps3.setStyleSheet('background-color: lightgrey;')
        self.NumReps4.setStyleSheet('background-color: lightgrey;')
        self.NumReps5.setStyleSheet('background-color: lightgrey;')
        self.NumReps6.setStyleSheet('background-color: lightgrey;')
        self.NumReps7.setStyleSheet('background-color: lightgrey;')
        self.NumReps8.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev1.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev2.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev3.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev4.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev5.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev6.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev7.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev8.setStyleSheet('background-color: lightgrey;')
        self.Dev1.setStyleSheet('background-color: lightgrey;')
        self.Dev2.setStyleSheet('background-color: lightgrey;')
        self.Dev3.setStyleSheet('background-color: lightgrey;')
        self.Dev4.setStyleSheet('background-color: lightgrey;')
        self.Dev5.setStyleSheet('background-color: lightgrey;')
        self.Dev6.setStyleSheet('background-color: lightgrey;')
        self.Dev7.setStyleSheet('background-color: lightgrey;')
        self.Dev8.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev1.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev2.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev3.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev4.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev5.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev6.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev7.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev8.setStyleSheet('background-color: lightgrey;')
        self.Dev_Target_2.setStyleSheet('background-color: lightgrey;')
        self.Dev_Target.setStyleSheet('background-color: lightgrey;')
        self.Total_Min_Dev.setStyleSheet('background-color: lightgrey;')




        self.County_comboBox.activated.connect(self.County_Change)
        self.County_comboBox.activated.connect(self.Reset)
        self.Population_comboBox.activated.connect(self.Pop_Change)
        self.Population_comboBox.activated.connect(self.Reset)
        self.Population_1.returnPressed.connect(self.PopulationChange)
        self.Population_2.returnPressed.connect(self.PopulationChange)
        self.Population_3.returnPressed.connect(self.PopulationChange)
        self.Population_4.returnPressed.connect(self.PopulationChange)
        self.Population_5.returnPressed.connect(self.PopulationChange)
        self.Population_6.returnPressed.connect(self.PopulationChange)
        self.Population_7.returnPressed.connect(self.PopulationChange)
        self.Population_8.returnPressed.connect(self.PopulationChange)
        self.NumOfReps.returnPressed.connect(self.PopulationChange)
        self.pushButton.pressed.connect(self.Reset)

        self.state_deviation_pop_2.setPlainText('+/- 165')

        pop = [3291, 6582, 9873, 13164, 16455, 19746, 23037, 26328, 29619, 32910, 36201, 39492, 42783, 46074, 49365,
               52656,
               55947, 59238, 62529, 65820, 69111, 72402, 75693, 78984, 82275, 85566, 88857, 92148, 95439, 98730, 102021,
               105312, 108603, 111894, 115185, 118476, 121767, 125058, 128349, 131640, 134931, 138222, 141513, 144804,
               148095, 151386, 154677, 157968, 161259, 164550]

        for i in range(0, 50):
            row_pop = pop[i]
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(row_pop)))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Dev Pop"))
        self.label_11.setText(_translate("MainWindow", "State"))
        self.state_deviation_pop.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "County"))
        self.County_comboBox.setItemText(0, _translate("MainWindow", "Belknap"))
        self.County_comboBox.setItemText(1, _translate("MainWindow", "Carroll"))
        self.County_comboBox.setItemText(2, _translate("MainWindow", "Cheshire"))
        self.County_comboBox.setItemText(3, _translate("MainWindow", "Coos"))
        self.County_comboBox.setItemText(4, _translate("MainWindow", "Grafton"))
        self.County_comboBox.setItemText(5, _translate("MainWindow", "Hillsborough"))
        self.County_comboBox.setItemText(6, _translate("MainWindow", "Merrimack"))
        self.County_comboBox.setItemText(7, _translate("MainWindow", "Rockingham"))
        self.County_comboBox.setItemText(8, _translate("MainWindow", "Strafford"))
        self.County_comboBox.setItemText(9, _translate("MainWindow", "Sullivan"))
        self.Population_comboBox.setItemText(0, _translate("MainWindow", "2010 Census"))
        self.Population_comboBox.setItemText(1, _translate("MainWindow", "2020 Census"))
        self.label_16.setText(_translate("MainWindow", "County"))
        self.label_17.setText(_translate("MainWindow", "Population"))
        self.label_18.setText(_translate("MainWindow", "Dev %"))
        self.label_19.setText(_translate("MainWindow", "State"))
        self.label_20.setText(_translate("MainWindow", "County"))
        self.label_3.setText(_translate("MainWindow", "NH Floterial Tool"))
        self.label_8.setText(_translate("MainWindow", "# of County Reps"))
        self.label_7.setText(_translate("MainWindow", "Per Rep"))
        self.label_9.setText(_translate("MainWindow", "State"))
        self.label_21.setText(_translate("MainWindow", "County"))
        self.label.setText(_translate("MainWindow", "# of Reps"))
        self.checkBox.setText(_translate("MainWindow", "Calculate"))
        self.label_2.setText(_translate("MainWindow", "Total Pop"))
        self.label_4.setText(_translate("MainWindow", "Target Pop"))
        self.label_6.setText(_translate("MainWindow", "State"))
        self.label_5.setText(_translate("MainWindow", "County"))
        self.label_15.setText(_translate("MainWindow", "Dev Target"))
        self.label_22.setText(_translate("MainWindow", "State"))
        self.state_deviation_pop_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "County"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Population"))
        self.label_50.setText(_translate("MainWindow", "Component Dev"))
        self.label_41.setText(_translate("MainWindow", "Dev %"))
        self.label_55.setText(_translate("MainWindow", "High Dev %"))
        self.label_63.setText(_translate("MainWindow", "Dev %"))
        self.label_56.setText(_translate("MainWindow", "Dev %"))
        self.label_64.setText(_translate("MainWindow", "Dev %"))
        self.label_65.setText(_translate("MainWindow", "Dev %"))
        self.label_66.setText(_translate("MainWindow", "Dev %"))
        self.label_69.setText(_translate("MainWindow", "High Dev %"))
        self.label_75.setText(_translate("MainWindow", "High Dev %"))
        self.label_74.setText(_translate("MainWindow", "High Dev %"))
        self.label_71.setText(_translate("MainWindow", "High Dev %"))
        self.label_67.setText(_translate("MainWindow", "Dev %"))
        self.label_68.setText(_translate("MainWindow", "Dev %"))
        self.label_70.setText(_translate("MainWindow", "High Dev %"))
        self.label_73.setText(_translate("MainWindow", "High Dev %"))
        self.label_72.setText(_translate("MainWindow", "High Dev %"))
        self.label_58.setText(_translate("MainWindow", "# of Reps"))
        self.label_53.setText(_translate("MainWindow", "Low Dev %"))
        self.label_39.setText(_translate("MainWindow", "District 2"))
        self.label_49.setText(_translate("MainWindow", "# of Reps"))
        self.label_40.setText(_translate("MainWindow", "District 4"))
        self.label_48.setText(_translate("MainWindow", "# of Reps"))
        self.label_52.setText(_translate("MainWindow", "# of Reps"))
        self.label_54.setText(_translate("MainWindow", "District 6"))
        self.label_34.setText(_translate("MainWindow", "# of Reps"))
        self.label_38.setText(_translate("MainWindow", "District 5"))
        self.label_36.setText(_translate("MainWindow", "Low Dev %"))
        self.label_42.setText(_translate("MainWindow", "Low Dev %"))
        self.label_35.setText(_translate("MainWindow", "District 1"))
        self.label_47.setText(_translate("MainWindow", "# of Reps"))
        self.label_44.setText(_translate("MainWindow", "Low Dev %"))
        self.label_45.setText(_translate("MainWindow", "Low Dev %"))
        self.label_43.setText(_translate("MainWindow", "Low Dev %"))
        self.label_46.setText(_translate("MainWindow", "# of Reps"))
        self.label_59.setText(_translate("MainWindow", "Low Dev %"))
        self.label_61.setText(_translate("MainWindow", "# of Reps"))
        self.label_62.setText(_translate("MainWindow", "Low Dev %"))
        self.label_60.setText(_translate("MainWindow", "District 8"))
        self.label_57.setText(_translate("MainWindow", "District 7"))
        self.label_37.setText(_translate("MainWindow", "District 3"))
        self.label_76.setText(_translate("MainWindow", "Alt Component Dev"))
        self.label_14.setText(_translate("MainWindow", "Results"))
        self.label_51.setText(_translate("MainWindow", "Aggregate Dev"))
        self.pushButton.setText(_translate("MainWindow", "RESET"))



    def Pop_Change(self, value):
        County_Pop = [[60088, 47698, 77117, 32961, 89118, 400721, 146445, 295223, 123143, 43742],
                      [63705, 50107, 76458, 31268, 91118, 422937, 153808, 314176, 130889, 43063]]
        county_population = County_Pop[value][self.County_comboBox.currentIndex()]
        state_population = sum(County_Pop[value])
        print(state_population)

        pop_levels = [[3291, 6582, 9873, 13164, 16455, 19746, 23037, 26328, 29619, 32910, 36201, 39492, 42783, 46074, 49365,
         52656,
         55947, 59238, 62529, 65820, 69111, 72402, 75693, 78984, 82275, 85566, 88857, 92148, 95439, 98730, 102021,
         105312, 108603, 111894, 115185, 118476, 121767, 125058, 128349, 131640, 134931, 138222, 141513, 144804,
         148095, 151386, 154677, 157968, 161259, 164550],[3444,6888,10332,13776,17220,20664,24108,27552,30996,34440,37884,41328,44772,48216,51660,55104,58548,61992,65436,68880,72324,75768,79212,82656,86100,89544,92988,96432,99876,103320,106764,110208,113652,117096,120540,123984,127428,130872,134316,137760,141204,144648,148092,151536,154980,158424,161868,165312,168756,172200]]

        pop_level = pop_levels[value]
        for i in range(0, 50):
            row_pop = pop_level[i]
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(row_pop)))


        state_pop_rd = round(state_population)
        pop_per_rep_state = (state_population / 400)
        reps_in_county = round(county_population / pop_per_rep_state)
        state_pop_per_rep = round(state_pop_rd / 400)
        county_pop_rd = round(county_population / reps_in_county)
        self.NumOfReps_3.setPlainText(str(reps_in_county))
        self.state_target_onerep.setPlainText(str(state_pop_per_rep))
        self.county_target_onerep.setPlainText(str(county_pop_rd))

        num_rep = int(self.NumOfReps.text())
        if self.checkBox.isChecked() == True:
            num_rep = round(int(self.Population.text()) / ((int(self.state_target_onerep.toPlainText()) + int(
                self.county_target_onerep.toPlainText())) / 2))
            num_rep = max(1, num_rep)
            self.NumOfReps.setText(str(num_rep))

        state_target_pop = round(num_rep * state_pop_per_rep)
        self.state_target_pop.setPlainText(str(state_target_pop))
        county_target_pop = round(num_rep * county_pop_rd)
        self.county_target_pop.setPlainText(str(county_target_pop))

        state_dev_per = 100 * ((int('0' + self.Population.text())) - (
            int('0' + self.state_target_pop.toPlainText()))) / (
                            int('0' + self.state_target_pop.toPlainText()))
        state_dev_per = round(state_dev_per, 2)
        self.state_deviation_per.setPlainText(str(state_dev_per) + '%')

        county_dev_per = 100 * ((int('0' + self.Population.text())) - (
            int('0' + self.county_target_pop.toPlainText()))) / (
                             int('0' + self.county_target_pop.toPlainText()))
        county_dev_per = round(county_dev_per, 2)
        self.county_deviation_per.setPlainText(str(county_dev_per) + '%')

        state_dev_pop = (int(self.Population.text()) - int(self.state_target_pop.toPlainText())) / int(
            self.NumOfReps.text())
        state_dev_pop = round(state_dev_pop, 2)
        self.state_deviation_pop.setPlainText(str(state_dev_pop))

        county_dev_pop = (int(self.Population.text()) - int(self.county_target_pop.toPlainText())) / int(
            self.NumOfReps.text())
        county_dev_pop = round(county_dev_pop, 2)
        self.county_deviation_pop.setPlainText(str(county_dev_pop))

        state_target_dev = round(int(self.state_target_onerep.toPlainText()) * .05)
        self.state_deviation_pop_2.setPlainText('+/- ' + str(state_target_dev))

        county_target_dev = round(int(self.county_target_onerep.toPlainText()) * .05)
        self.county_deviation_pop_2.setPlainText('+/- ' + str(county_target_dev))

        if state_dev_per < 5 and state_dev_per > -5:
            self.state_deviation_per.setStyleSheet('background-color: green;')
        if state_dev_per >= 5 or state_dev_per <= -5:
            self.state_deviation_per.setStyleSheet('background-color: red;')

        if county_dev_per < 5 and county_dev_per > -5:
            self.county_deviation_per.setStyleSheet('background-color: green;')
        if county_dev_per >= 5 or county_dev_per <= -5:
            self.county_deviation_per.setStyleSheet('background-color: red;')

        if abs(state_dev_pop) < state_target_dev:
            self.state_deviation_pop.setStyleSheet('background-color: green;')
        if abs(state_dev_pop) >= state_target_dev:
            self.state_deviation_pop.setStyleSheet('background-color: red;')

        if abs(county_dev_pop) < county_target_dev:
            self.county_deviation_pop.setStyleSheet('background-color: green;')
        if abs(county_dev_pop) >= county_target_dev:
            self.county_deviation_pop.setStyleSheet('background-color: red;')


    def County_Change(self, value):
        County_Pop = [[60088, 47698, 77117, 32961, 89118, 400721, 146445, 295223, 123143, 43742],[63705,50107,76458,31268,91118,422937,153808,314176,130889,43063]]
        county_population = County_Pop[self.Population_comboBox.currentIndex()][value]
        state_population = sum(County_Pop[self.Population_comboBox.currentIndex()])
        print(state_population)
        state_pop_rd = round(state_population)
        pop_per_rep_state = (state_population/400)
        reps_in_county = round(county_population/pop_per_rep_state)
        state_pop_per_rep = round(state_pop_rd / 400)
        county_pop_rd = round(county_population/reps_in_county)
        self.NumOfReps_3.setPlainText(str(reps_in_county))
        self.state_target_onerep.setPlainText(str(state_pop_per_rep))
        self.county_target_onerep.setPlainText(str(county_pop_rd))

        num_rep = int(self.NumOfReps.text())
        if self.checkBox.isChecked() == True:
            num_rep = round(int(self.Population.text())/((int(self.state_target_onerep.toPlainText()) + int(self.county_target_onerep.toPlainText()))/2))
            num_rep = max(1, num_rep)
            self.NumOfReps.setText(str(num_rep))



        state_target_pop = round(num_rep * state_pop_per_rep)
        self.state_target_pop.setPlainText(str(state_target_pop))
        county_target_pop = round(num_rep * county_pop_rd)
        self.county_target_pop.setPlainText(str(county_target_pop))

        state_dev_per = 100 * ((int('0' + self.Population.text())) - (
                    int('0' + self.state_target_pop.toPlainText()))) / (
                            int('0' + self.state_target_pop.toPlainText()))
        state_dev_per = round(state_dev_per, 2)
        self.state_deviation_per.setPlainText(str(state_dev_per)+'%')

        county_dev_per = 100 * ((int('0' + self.Population.text())) - (
                    int('0' + self.county_target_pop.toPlainText()))) / (
                            int('0' + self.county_target_pop.toPlainText()))
        county_dev_per = round(county_dev_per, 2)
        self.county_deviation_per.setPlainText(str(county_dev_per)+'%')

        state_dev_pop = (int(self.Population.text()) - int(self.state_target_pop.toPlainText())) / int(self.NumOfReps.text())
        state_dev_pop = round(state_dev_pop, 2)
        self.state_deviation_pop.setPlainText(str(state_dev_pop))


        county_dev_pop = (int(self.Population.text()) - int(self.county_target_pop.toPlainText())) / int(
            self.NumOfReps.text())
        county_dev_pop = round(county_dev_pop, 2)
        self.county_deviation_pop.setPlainText(str(county_dev_pop))

        state_target_dev = round(int(self.state_target_onerep.toPlainText()) * .05)
        self.state_deviation_pop_2.setPlainText('+/- ' + str(state_target_dev))

        county_target_dev = round(int(self.county_target_onerep.toPlainText()) * .05)
        self.county_deviation_pop_2.setPlainText('+/- ' + str(county_target_dev))

        if state_dev_per < 5 and state_dev_per > -5:
            self.state_deviation_per.setStyleSheet('background-color: green;')
        if state_dev_per >= 5 or state_dev_per <=-5:
            self.state_deviation_per.setStyleSheet('background-color: red;')


        if county_dev_per < 5 and county_dev_per > -5:
            self.county_deviation_per.setStyleSheet('background-color: green;')
        if county_dev_per >= 5 or county_dev_per <=-5:
            self.county_deviation_per.setStyleSheet('background-color: red;')

        if abs(state_dev_pop) < state_target_dev:
            self.state_deviation_pop.setStyleSheet('background-color: green;')
        if abs(state_dev_pop) >= state_target_dev:
            self.state_deviation_pop.setStyleSheet('background-color: red;')

        if abs(county_dev_pop) < county_target_dev:
            self.county_deviation_pop.setStyleSheet('background-color: green;')
        if abs(county_dev_pop) >= county_target_dev:
            self.county_deviation_pop.setStyleSheet('background-color: red;')


    def PopulationChange(self):

        total_pop = int('0'+self.Population_1.text())+int('0'+self.Population_2.text())+int('0'+self.Population_3.text())+int('0'+self.Population_4.text())+int('0'+self.Population_5.text())+int('0'+self.Population_6.text())+int('0'+self.Population_7.text())+int('0'+self.Population_8.text())
        self.Population.setText(str(total_pop))

        if self.checkBox.isChecked() == True:
            num_rep = round(int('0'+self.Population.text()) / int(self.state_target_onerep.toPlainText()))
            num_rep = max(1, num_rep)
            self.NumOfReps.setText(str(num_rep))

        num_rep = int(self.NumOfReps.text())

        num_rep_1 = math.floor(int('0' + self.Population_1.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps1.setText(str(num_rep_1))

        num_rep_2 = math.floor(int('0' + self.Population_2.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps2.setText(str(num_rep_2))

        num_rep_3 = math.floor(int('0' + self.Population_3.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps3.setText(str(num_rep_3))

        num_rep_4 = math.floor(int('0' + self.Population_4.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps4.setText(str(num_rep_4))

        num_rep_5 = math.floor(int('0' + self.Population_5.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps5.setText(str(num_rep_5))

        num_rep_6 = math.floor(int('0' + self.Population_6.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps6.setText(str(num_rep_6))

        num_rep_7 = math.floor(int('0' + self.Population_7.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps7.setText(str(num_rep_7))

        num_rep_8 = math.floor(int('0' + self.Population_8.text()) / int(self.state_target_onerep.toPlainText()))
        self.NumReps8.setText(str(num_rep_8))


        print('test')

        num_float_reps = int(self.NumOfReps.text()) - (int(self.NumReps1.text()) + int(self.NumReps2.text()) + int(self.NumReps3.text()) + int(self.NumReps4.text()) + int(self.NumReps5.text())+int(self.NumReps6.text())+int(self.NumReps7.text())+int(self.NumReps8.text()))


        DA_1 = 0
        DA_2 = 0
        DA_3 = 0
        DA_4 = 0
        DA_5 = 0
        DA_6 = 0
        DA_7 = 0
        DA_8 = 0
        DA_Low_1 = 0
        DA_Low_2 = 0
        DA_Low_3 = 0
        DA_Low_4 = 0
        DA_Low_5 = 0
        DA_Low_6 = 0
        DA_Low_7 = 0
        DA_Low_8 = 0
        DA_High_1 = 0
        DA_High_2 = 0
        DA_High_3 = 0
        DA_High_4 = 0
        DA_High_5 = 0
        DA_High_6 = 0
        DA_High_7 = 0
        DA_High_8 = 0


        ASA_1 = (num_rep_1 + ((int('0' + self.Population_1.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_1 != 0:
            DA_1 = (((int('0' + self.Population_1.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_1) / ASA_1) * 100
            self.Dev1.setText(str(round(DA_1, 2)) + '%')

            if abs(DA_1) < 5:
                self.Dev1.setStyleSheet('background-color: green;')
            if abs(DA_1) >= 5:
                self.Dev1.setStyleSheet('background-color: red;')

        elif ASA_1 == 0:
            self.Dev1.setText('  -----  ')
            self.Dev1.setStyleSheet('background-color: lightgrey;')

        ASA_2 = (num_rep_2 + ((int('0' + self.Population_2.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_2 != 0:
            DA_2 = (((int('0' + self.Population_2.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_2) / ASA_2) * 100
            self.Dev2.setText(str(round(DA_2, 2)) + '%')

            if abs(DA_2) < 5:
                self.Dev2.setStyleSheet('background-color: green;')
            if abs(DA_2) >= 5:
                self.Dev2.setStyleSheet('background-color: red;')

        elif ASA_2 == 0:
            self.Dev2.setText('  -----  ')
            self.Dev2.setStyleSheet('background-color: lightgrey;')

        ASA_3 = (num_rep_3 + ((int('0' + self.Population_3.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_3 != 0:
            DA_3 = (((int('0' + self.Population_3.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_3) / ASA_3) * 100
            self.Dev3.setText(str(round(DA_3, 2)) + '%')

            if abs(DA_3) < 5:
                self.Dev3.setStyleSheet('background-color: green;')
            if abs(DA_3) >= 5:
                self.Dev3.setStyleSheet('background-color: red;')

        elif ASA_3 == 0:
            self.Dev3.setText('  -----  ')
            self.Dev3.setStyleSheet('background-color: lightgrey;')

        ASA_4 = (num_rep_4 + ((int('0' + self.Population_4.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_4 != 0:
            DA_4 = (((int('0' + self.Population_4.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_4) / ASA_4) * 100
            self.Dev4.setText(str(round(DA_4, 2)) + '%')

            if abs(DA_4) < 5:
                self.Dev4.setStyleSheet('background-color: green;')
            if abs(DA_4) >= 5:
                self.Dev4.setStyleSheet('background-color: red;')

        elif ASA_4 == 0:
            self.Dev4.setText('  -----  ')
            self.Dev4.setStyleSheet('background-color: lightgrey;')

        ASA_5 = (num_rep_5 + ((int('0' + self.Population_5.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_5 != 0:
            DA_5 = (((int('0' + self.Population_5.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_5) / ASA_5) * 100
            self.Dev5.setText(str(round(DA_5, 2)) + '%')

            if abs(DA_5) < 5:
                self.Dev5.setStyleSheet('background-color: green;')
            if abs(DA_5) >= 5:
                self.Dev5.setStyleSheet('background-color: red;')

        elif ASA_5 == 0:
            self.Dev5.setText('  -----  ')
            self.Dev5.setStyleSheet('background-color: lightgrey;')

        ASA_6 = (num_rep_6 + ((int('0' + self.Population_6.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_6 != 0:
            DA_6 = (((int('0' + self.Population_6.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_6) / ASA_6) * 100
            self.Dev6.setText(str(round(DA_6, 2)) + '%')

            if abs(DA_6) < 5:
                self.Dev6.setStyleSheet('background-color: green;')
            if abs(DA_6) >= 5:
                self.Dev6.setStyleSheet('background-color: red;')

        elif ASA_6 == 0:
            self.Dev6.setText('  -----  ')
            self.Dev6.setStyleSheet('background-color: lightgrey;')

        ASA_7 = (num_rep_7 + ((int('0' + self.Population_7.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_7 != 0:
            DA_7 = (((int('0' + self.Population_7.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_7) / ASA_7) * 100
            self.Dev7.setText(str(round(DA_7, 2)) + '%')

            if abs(DA_7) < 5:
                self.Dev7.setStyleSheet('background-color: green;')
            if abs(DA_7) >= 5:
                self.Dev7.setStyleSheet('background-color: red;')

        elif ASA_7 == 0:
            self.Dev7.setText('  -----  ')
            self.Dev7.setStyleSheet('background-color: lightgrey;')

        ASA_8 = (num_rep_8 + ((int('0' + self.Population_8.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_8 != 0:
            DA_8 = (((int('0' + self.Population_8.text()) / int(
                self.state_target_onerep.toPlainText())) - ASA_8) / ASA_8) * 100
            self.Dev8.setText(str(round(DA_8, 2)) + '%')

            if abs(DA_8) < 5:
                self.Dev8.setStyleSheet('background-color: green;')
            if abs(DA_8) >= 5:
                self.Dev8.setStyleSheet('background-color: red;')

        elif ASA_8 == 0:
            self.Dev8.setText('  -----  ')
            self.Dev8.setStyleSheet('background-color: lightgrey;')

        a_string = self.state_deviation_pop_2.toPlainText()
        num_dev = a_string.partition("- ")[2]
        num_dev = int(num_dev)

        ASA_Low_1 = (num_rep_1 + ((int('0' + self.Population_1.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_1 != 0:
            DA_Low_1 = (((int('0' + self.Population_1.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_1) / ASA_Low_1) * 100
            self.Min_Dev1.setText(str(round(DA_Low_1, 2)) + '%')

            if abs(DA_Low_1) < 5:
                self.Min_Dev1.setStyleSheet('background-color: green;')
            if abs(DA_Low_1) >= 5:
                self.Min_Dev1.setStyleSheet('background-color: red;')

        elif ASA_Low_1 == 0:
            self.Min_Dev1.setText('  -----  ')
            self.Min_Dev1.setStyleSheet('background-color: lightgrey;')

        ASA_Low_2 = (num_rep_2 + ((int('0' + self.Population_2.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_2 != 0:
            DA_Low_2 = (((int('0' + self.Population_2.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_2) / ASA_Low_2) * 100
            self.Min_Dev2.setText(str(round(DA_Low_2, 2)) + '%')

            if abs(DA_Low_2) < 5:
                self.Min_Dev2.setStyleSheet('background-color: green;')
            if abs(DA_Low_2) >= 5:
                self.Min_Dev2.setStyleSheet('background-color: red;')

        elif ASA_Low_2 == 0:
            self.Min_Dev2.setText('  -----  ')
            self.Min_Dev2.setStyleSheet('background-color: lightgrey;')

        ASA_Low_3 = (num_rep_3 + ((int('0' + self.Population_3.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_3 != 0:
            DA_Low_3 = (((int('0' + self.Population_3.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_3) / ASA_Low_3) * 100
            self.Min_Dev3.setText(str(round(DA_Low_3, 2)) + '%')

            if abs(DA_Low_3) < 5:
                self.Min_Dev3.setStyleSheet('background-color: green;')
            if abs(DA_Low_3) >= 5:
                self.Min_Dev3.setStyleSheet('background-color: red;')

        elif ASA_Low_3 == 0:
            self.Min_Dev3.setText('  -----  ')
            self.Min_Dev3.setStyleSheet('background-color: lightgrey;')

        ASA_Low_4 = (num_rep_4 + ((int('0' + self.Population_4.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_4 != 0:
            DA_Low_4 = (((int('0' + self.Population_4.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_4) / ASA_Low_4) * 100
            self.Min_Dev4.setText(str(round(DA_Low_4, 2)) + '%')

            if abs(DA_Low_4) < 5:
                self.Min_Dev4.setStyleSheet('background-color: green;')
            if abs(DA_Low_4) >= 5:
                self.Min_Dev4.setStyleSheet('background-color: red;')

        elif ASA_Low_4 == 0:
            self.Min_Dev4.setText('  -----  ')
            self.Min_Dev4.setStyleSheet('background-color: lightgrey;')

        ASA_Low_5 = (num_rep_5 + ((int('0' + self.Population_5.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_5 != 0:
            DA_Low_5 = (((int('0' + self.Population_5.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_5) / ASA_Low_5) * 100
            self.Min_Dev5.setText(str(round(DA_Low_5, 2)) + '%')

            if abs(DA_Low_5) < 5:
                self.Min_Dev5.setStyleSheet('background-color: green;')
            if abs(DA_Low_5) >= 5:
                self.Min_Dev5.setStyleSheet('background-color: red;')

        elif ASA_Low_5 == 0:
            self.Min_Dev5.setText('  -----  ')
            self.Min_Dev5.setStyleSheet('background-color: lightgrey;')

        ASA_Low_6 = (num_rep_6 + ((int('0' + self.Population_6.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_6 != 0:
            DA_Low_6 = (((int('0' + self.Population_6.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_6) / ASA_Low_6) * 100
            self.Min_Dev6.setText(str(round(DA_Low_6, 2)) + '%')

            if abs(DA_Low_6) < 5:
                self.Min_Dev6.setStyleSheet('background-color: green;')
            if abs(DA_Low_6) >= 5:
                self.Min_Dev6.setStyleSheet('background-color: red;')

        elif ASA_Low_6 == 0:
            self.Min_Dev6.setText('  -----  ')
            self.Min_Dev6.setStyleSheet('background-color: lightgrey;')

        ASA_Low_7 = (num_rep_7 + ((int('0' + self.Population_7.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_7 != 0:
            DA_Low_7 = (((int('0' + self.Population_7.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_7) / ASA_Low_7) * 100
            self.Min_Dev7.setText(str(round(DA_Low_7, 2)) + '%')

            if abs(DA_Low_7) < 5:
                self.Min_Dev7.setStyleSheet('background-color: green;')
            if abs(DA_Low_7) >= 5:
                self.Min_Dev7.setStyleSheet('background-color: red;')

        elif ASA_Low_7 == 0:
            self.Min_Dev7.setText('  -----  ')
            self.Min_Dev7.setStyleSheet('background-color: lightgrey;')

        ASA_Low_8 = (num_rep_8 + ((int('0' + self.Population_8.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_Low_8 != 0:
            DA_Low_8 = (((int('0' + self.Population_8.text())) / ((int(
                self.state_target_onerep.toPlainText())) - num_dev) - ASA_Low_8) / ASA_Low_8) * 100
            self.Min_Dev8.setText(str(round(DA_Low_8, 2)) + '%')

            if abs(DA_Low_8) < 5:
                self.Min_Dev8.setStyleSheet('background-color: green;')
            if abs(DA_Low_8) >= 5:
                self.Min_Dev8.setStyleSheet('background-color: red;')

        elif ASA_Low_8 == 0:
            self.Min_Dev8.setText('  -----  ')
            self.Min_Dev8.setStyleSheet('background-color: lightgrey;')

        ASA_High_1 = (num_rep_1 + ((int('0' + self.Population_1.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_1 != 0:
            DA_High_1 = (((int('0' + self.Population_1.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_1) / ASA_Low_1) * 100
            self.Max_Dev1.setText(str(round(DA_High_1, 2)) + '%')

            if abs(DA_High_1) < 5:
                self.Max_Dev1.setStyleSheet('background-color: green;')
            if abs(DA_High_1) >= 5:
                self.Max_Dev1.setStyleSheet('background-color: red;')

        elif ASA_High_1 == 0:
            self.Max_Dev1.setText('  -----  ')
            self.Max_Dev1.setStyleSheet('background-color: lightgrey;')

        ASA_High_2 = (num_rep_2 + ((int('0' + self.Population_2.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_2 != 0:
            DA_High_2 = (((int('0' + self.Population_2.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_2) / ASA_Low_2) * 100
            self.Max_Dev2.setText(str(round(DA_High_2, 2)) + '%')

            if abs(DA_High_2) < 5:
                self.Max_Dev2.setStyleSheet('background-color: green;')
            if abs(DA_High_2) >= 5:
                self.Max_Dev2.setStyleSheet('background-color: red;')

        elif ASA_High_2 == 0:
            self.Max_Dev2.setText('  -----  ')
            self.Max_Dev2.setStyleSheet('background-color: lightgrey;')



        ASA_High_3 = (num_rep_3 + ((int('0' + self.Population_3.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_3 != 0:
            DA_High_3 = (((int('0' + self.Population_3.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_3) / ASA_Low_3) * 100
            self.Max_Dev3.setText(str(round(DA_High_3, 2)) + '%')

            if abs(DA_High_3) < 5:
                self.Max_Dev3.setStyleSheet('background-color: green;')
            if abs(DA_High_3) >= 5:
                self.Max_Dev3.setStyleSheet('background-color: red;')

        elif ASA_High_3 == 0:
            self.Max_Dev3.setText('  -----  ')
            self.Max_Dev3.setStyleSheet('background-color: lightgrey;')



        ASA_High_4 = (num_rep_4 + ((int('0' + self.Population_4.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_4 != 0:
            DA_High_4 = (((int('0' + self.Population_4.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_4) / ASA_Low_4) * 100
            self.Max_Dev4.setText(str(round(DA_High_4, 2)) + '%')

            if abs(DA_High_4) < 5:
                self.Max_Dev4.setStyleSheet('background-color: green;')
            if abs(DA_High_4) >= 5:
                self.Max_Dev4.setStyleSheet('background-color: red;')

        elif ASA_High_4 == 0:
            self.Max_Dev4.setText('  -----  ')
            self.Max_Dev4.setStyleSheet('background-color: lightgrey;')



        ASA_High_5 = (num_rep_5 + ((int('0' + self.Population_5.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_5 != 0:
            DA_High_5 = (((int('0' + self.Population_5.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_5) / ASA_Low_5) * 100
            self.Max_Dev5.setText(str(round(DA_High_5, 2)) + '%')

            if abs(DA_High_5) < 5:
                self.Max_Dev5.setStyleSheet('background-color: green;')
            if abs(DA_High_5) >= 5:
                self.Max_Dev5.setStyleSheet('background-color: red;')

        elif ASA_High_5 == 0:
            self.Max_Dev5.setText('  -----  ')
            self.Max_Dev5.setStyleSheet('background-color: lightgrey;')



        ASA_High_6 = (num_rep_6 + ((int('0' + self.Population_6.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_6 != 0:
            DA_High_6 = (((int('0' + self.Population_6.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_6) / ASA_Low_6) * 100
            self.Max_Dev6.setText(str(round(DA_High_6, 2)) + '%')

            if abs(DA_High_6) < 5:
                self.Max_Dev6.setStyleSheet('background-color: green;')
            if abs(DA_High_6) >= 5:
                self.Max_Dev6.setStyleSheet('background-color: red;')

        elif ASA_High_6 == 0:
            self.Max_Dev6.setText('  -----  ')
            self.Max_Dev6.setStyleSheet('background-color: lightgrey;')



        ASA_High_7 = (num_rep_7 + ((int('0' + self.Population_7.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_7 != 0:
            DA_High_7 = (((int('0' + self.Population_7.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_7) / ASA_Low_7) * 100
            self.Max_Dev7.setText(str(round(DA_High_7, 2)) + '%')

            if abs(DA_High_7) < 5:
                self.Max_Dev7.setStyleSheet('background-color: green;')
            if abs(DA_High_7) >= 5:
                self.Max_Dev7.setStyleSheet('background-color: red;')

        elif ASA_High_7 == 0:
            self.Max_Dev7.setText('  -----  ')
            self.Max_Dev7.setStyleSheet('background-color: lightgrey;')



        ASA_High_8 = (num_rep_8 + ((int('0' + self.Population_8.text()) / int(self.Population.text())) * num_float_reps))
        if ASA_High_8 != 0:
            DA_High_8 = (((int('0' + self.Population_8.text())) / ((int(
                self.state_target_onerep.toPlainText())) + num_dev) - ASA_Low_8) / ASA_Low_8) * 100
            self.Max_Dev8.setText(str(round(DA_High_8, 2)) + '%')

            if abs(DA_High_8) < 5:
                self.Max_Dev8.setStyleSheet('background-color: green;')
            if abs(DA_High_8) >= 5:
                self.Max_Dev8.setStyleSheet('background-color: red;')

        elif ASA_High_8 == 0:
            self.Max_Dev8.setText('  -----  ')
            self.Max_Dev8.setStyleSheet('background-color: lightgrey;')




        state_pop_per_rep = int(self.state_target_onerep.toPlainText())
        county_pop_rd = int(self.county_target_onerep.toPlainText())

        state_target_pop = round(num_rep * state_pop_per_rep)
        self.state_target_pop.setPlainText(str(state_target_pop))

        county_target_pop = round(num_rep * county_pop_rd)
        self.county_target_pop.setPlainText(str(county_target_pop))

        state_dev_per = 100 * ((int('0' + self.Population.text())) - (
            int('0' + self.state_target_pop.toPlainText()))) / (
                            int('0' + self.state_target_pop.toPlainText()))
        state_dev_per = round(state_dev_per, 2)
        self.state_deviation_per.setPlainText(str(state_dev_per) + '%')
        if state_dev_per < 5 and state_dev_per > -5:
            self.state_deviation_per.setStyleSheet('background-color: green;')
        if state_dev_per >= 5 or state_dev_per <=-5:
            self.state_deviation_per.setStyleSheet('background-color: red;')

        county_dev_per = 100 * ((int('0' + self.Population.text())) - (
            int('0' + self.county_target_pop.toPlainText()))) / (
                             int('0' + self.county_target_pop.toPlainText()))
        county_dev_per = round(county_dev_per, 2)
        self.county_deviation_per.setPlainText(str(county_dev_per) + '%')

        if county_dev_per < 5 and county_dev_per > -5:
            self.county_deviation_per.setStyleSheet('background-color: green;')
        if county_dev_per >= 5 or county_dev_per <=-5:
            self.county_deviation_per.setStyleSheet('background-color: red;')

        state_dev_pop = (int(self.Population.text()) - int(self.state_target_pop.toPlainText())) / int(
            self.NumOfReps.text())
        state_dev_pop = round(state_dev_pop, 2)
        self.state_deviation_pop.setPlainText(str(state_dev_pop))

        state_target_dev = round(int(self.state_target_onerep.toPlainText()) * .05)
        self.state_deviation_pop_2.setPlainText('+/- ' + str(state_target_dev))

        if abs(state_dev_pop) < state_target_dev:
            self.state_deviation_pop.setStyleSheet('background-color: green;')
        if abs(state_dev_pop) >= state_target_dev:
            self.state_deviation_pop.setStyleSheet('background-color: red;')



        county_dev_pop = (int(self.Population.text()) - int(self.county_target_pop.toPlainText())) / int(
            self.NumOfReps.text())
        county_dev_pop = round(county_dev_pop, 2)
        self.county_deviation_pop.setPlainText(str(county_dev_pop))

        county_dev_pop_5 = county_dev_pop * .05
        if county_dev_pop_5 < 5 and county_dev_pop_5 > -5:
            self.county_deviation_pop.setStyleSheet('background-color: green;')
        if county_dev_pop_5 >= 5 or county_dev_pop_5 <=-5:
            self.county_deviation_pop.setStyleSheet('background-color: red;')

        county_target_dev = round(int(self.county_target_onerep.toPlainText()) * .05)
        self.county_deviation_pop_2.setPlainText('+/- ' + str(county_target_dev))

        if abs(county_dev_pop) < county_target_dev:
            self.county_deviation_pop.setStyleSheet('background-color: green;')
        if abs(county_dev_pop) >= county_target_dev:
            self.county_deviation_pop.setStyleSheet('background-color: red;')



        if abs(state_dev_per) < 5:
            self.Dev_Target_2.setText('TRUE')
            self.Dev_Target_2.setStyleSheet('background-color: green;')

        if abs(state_dev_per) >= 5:
            self.Dev_Target_2.setText('FALSE')
            self.Dev_Target_2.setStyleSheet('background-color: red;')

        Max_Comp = max(DA_1,DA_2,DA_3,DA_4,DA_5,DA_6,DA_7,DA_8)
        Min_Comp = min(DA_1,DA_2,DA_3,DA_4,DA_5,DA_6,DA_7,DA_8)

        if Max_Comp < 5 and Min_Comp > -5 and abs(state_dev_per) < 5:
            self.Dev_Target.setText('TRUE')
            self.Dev_Target.setStyleSheet('background-color: green;')

        elif Max_Comp > 5 or Min_Comp < -5 or abs(state_dev_per) > 5:
            self.Dev_Target.setText('FALSE')
            self.Dev_Target.setStyleSheet('background-color: red;')


        Alt_Comp_1 = min(abs(DA_Low_1),abs(DA_1),abs(DA_High_1))
        Alt_Comp_2 = min(abs(DA_Low_2), abs(DA_2), abs(DA_High_2))
        Alt_Comp_3 = min(abs(DA_Low_3), abs(DA_3), abs(DA_High_3))
        Alt_Comp_4 = min(abs(DA_Low_4), abs(DA_4), abs(DA_High_4))
        Alt_Comp_5 = min(abs(DA_Low_5), abs(DA_5), abs(DA_High_5))
        Alt_Comp_6 = min(abs(DA_Low_6), abs(DA_6), abs(DA_High_6))
        Alt_Comp_7 = min(abs(DA_Low_7), abs(DA_7), abs(DA_High_7))
        Alt_Comp_8 = min(abs(DA_Low_8), abs(DA_8), abs(DA_High_8))



        if Alt_Comp_1 < 5 and Alt_Comp_2 < 5 and Alt_Comp_3 < 5 and Alt_Comp_4 < 5 and Alt_Comp_5 < 5 and Alt_Comp_6 < 5 and Alt_Comp_7 < 5 and Alt_Comp_8 < 5 and abs(state_dev_per) < 5:
            self.Total_Min_Dev.setText('TRUE')
            self.Total_Min_Dev.setStyleSheet('background-color: green;')

        if Alt_Comp_1 > 5 or Alt_Comp_2 > 5 or Alt_Comp_3 > 5 or Alt_Comp_4 > 5 or Alt_Comp_5 > 5 or Alt_Comp_6 > 5 or Alt_Comp_7 > 5 or Alt_Comp_8 > 5 or abs(state_dev_per) > 5:
            self.Total_Min_Dev.setText('FALSE')
            self.Total_Min_Dev.setStyleSheet('background-color: red;')






    def Reset(self):
        self.Population.setText('0')
        self.Population_1.setText('0')
        self.NumReps1.setText('0')
        self.Min_Dev1.setText('0')
        self.Dev1.setText('0')
        self.Max_Dev1.setText('0')
        self.Population_2.setText('0')
        self.NumReps2.setText('0')
        self.Min_Dev2.setText('0')
        self.Dev2.setText('0')
        self.Max_Dev2.setText('0')
        self.Population_3.setText('0')
        self.NumReps3.setText('0')
        self.Min_Dev3.setText('0')
        self.Dev3.setText('0')
        self.Max_Dev3.setText('0')
        self.Population_4.setText('0')
        self.NumReps4.setText('0')
        self.Min_Dev4.setText('0')
        self.Dev4.setText('0')
        self.Max_Dev4.setText('0')
        self.Population_5.setText('0')
        self.NumReps5.setText('0')
        self.Min_Dev5.setText('0')
        self.Dev5.setText('0')
        self.Max_Dev5.setText('0')
        self.Population_6.setText('0')
        self.NumReps6.setText('0')
        self.Min_Dev6.setText('0')
        self.Dev6.setText('0')
        self.Max_Dev6.setText('0')
        self.Population_7.setText('0')
        self.NumReps7.setText('0')
        self.Min_Dev7.setText('0')
        self.Dev7.setText('0')
        self.Max_Dev7.setText('0')
        self.Population_8.setText('0')
        self.NumReps8.setText('0')
        self.Min_Dev8.setText('0')
        self.Dev8.setText('0')
        self.Max_Dev8.setText('0')
        self.Dev_Target_2.setText('0')
        self.Dev_Target.setText('0')
        self.Total_Min_Dev.setText('0')

        self.NumOfReps.setText('0')
        self.state_target_pop.setText(self.state_target_onerep.toPlainText())
        self.county_target_pop.setText(self.county_target_onerep.toPlainText())
        self.state_deviation_per.setPlainText('0 %')
        self.county_deviation_per.setPlainText('0 %')
        self.state_deviation_pop.setPlainText('0 %')
        self.county_deviation_pop.setPlainText('0 %')


        self.NumOfReps_3.setStyleSheet('background-color: lightgrey;')
        self.Population.setStyleSheet('background-color: lightgrey;')
        self.state_target_pop.setStyleSheet('background-color: lightgrey;')
        self.county_target_pop.setStyleSheet('background-color: lightgrey;')
        self.state_deviation_per.setStyleSheet('background-color: lightgrey;')
        self.county_deviation_per.setStyleSheet('background-color: lightgrey;')
        self.state_deviation_pop.setStyleSheet('background-color: lightgrey;')
        self.county_deviation_pop.setStyleSheet('background-color: lightgrey;')
        self.state_deviation_pop_2.setStyleSheet('background-color: lightgrey;')
        self.county_deviation_pop_2.setStyleSheet('background-color: lightgrey;')
        self.state_target_onerep.setStyleSheet('background-color: lightgrey;')
        self.county_target_onerep.setStyleSheet('background-color: lightgrey;')
        self.NumReps1.setStyleSheet('background-color: lightgrey;')
        self.NumReps2.setStyleSheet('background-color: lightgrey;')
        self.NumReps3.setStyleSheet('background-color: lightgrey;')
        self.NumReps4.setStyleSheet('background-color: lightgrey;')
        self.NumReps5.setStyleSheet('background-color: lightgrey;')
        self.NumReps6.setStyleSheet('background-color: lightgrey;')
        self.NumReps7.setStyleSheet('background-color: lightgrey;')
        self.NumReps8.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev1.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev2.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev3.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev4.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev5.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev6.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev7.setStyleSheet('background-color: lightgrey;')
        self.Min_Dev8.setStyleSheet('background-color: lightgrey;')
        self.Dev1.setStyleSheet('background-color: lightgrey;')
        self.Dev2.setStyleSheet('background-color: lightgrey;')
        self.Dev3.setStyleSheet('background-color: lightgrey;')
        self.Dev4.setStyleSheet('background-color: lightgrey;')
        self.Dev5.setStyleSheet('background-color: lightgrey;')
        self.Dev6.setStyleSheet('background-color: lightgrey;')
        self.Dev7.setStyleSheet('background-color: lightgrey;')
        self.Dev8.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev1.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev2.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev3.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev4.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev5.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev6.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev7.setStyleSheet('background-color: lightgrey;')
        self.Max_Dev8.setStyleSheet('background-color: lightgrey;')
        self.Dev_Target_2.setStyleSheet('background-color: lightgrey;')
        self.Dev_Target.setStyleSheet('background-color: lightgrey;')
        self.Total_Min_Dev.setStyleSheet('background-color: lightgrey;')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())