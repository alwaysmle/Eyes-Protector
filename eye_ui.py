# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eye.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1345, 677)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("panda.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 471, 31))
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.tabWidget.addTab(self.main, "")
        self.analyze = QtWidgets.QWidget()
        self.analyze.setObjectName("analyze")
        self.tabWidget.addTab(self.analyze, "")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 50, 1321, 631))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setAutoFillBackground(False)
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 1281, 621))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.start_push = QtWidgets.QPushButton(self.frame)
        self.start_push.setEnabled(False)
        self.start_push.setGeometry(QtCore.QRect(310, 390, 171, 51))
        self.start_push.setObjectName("start_push")
        self.initialize_push = QtWidgets.QPushButton(self.frame)
        self.initialize_push.setEnabled(False)
        self.initialize_push.setGeometry(QtCore.QRect(310, 290, 171, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initialize_push.sizePolicy().hasHeightForWidth())
        self.initialize_push.setSizePolicy(sizePolicy)
        self.initialize_push.setObjectName("initialize_push")
        self.add_push = QtWidgets.QPushButton(self.frame)
        self.add_push.setEnabled(True)
        self.add_push.setGeometry(QtCore.QRect(340, 50, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_push.sizePolicy().hasHeightForWidth())
        self.add_push.setSizePolicy(sizePolicy)
        self.add_push.setObjectName("add_push")
        self.working_time = QtWidgets.QDoubleSpinBox(self.frame)
        self.working_time.setEnabled(True)
        self.working_time.setGeometry(QtCore.QRect(170, 290, 64, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.working_time.sizePolicy().hasHeightForWidth())
        self.working_time.setSizePolicy(sizePolicy)
        self.working_time.setDecimals(2)
        self.working_time.setMinimum(0.0)
        self.working_time.setMaximum(60.0)
        self.working_time.setSingleStep(1.0)
        self.working_time.setProperty("value", 25.0)
        self.working_time.setObjectName("working_time")
        self.Time_Minute_lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.Time_Minute_lcdNumber.setGeometry(QtCore.QRect(246, 500, 51, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Minute_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Time_Minute_lcdNumber.setSizePolicy(sizePolicy)
        self.Time_Minute_lcdNumber.setDigitCount(2)
        self.Time_Minute_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Time_Minute_lcdNumber.setObjectName("Time_Minute_lcdNumber")
        self.Velocity_label_4 = QtWidgets.QLabel(self.frame)
        self.Velocity_label_4.setGeometry(QtCore.QRect(20, 430, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Velocity_label_4.sizePolicy().hasHeightForWidth())
        self.Velocity_label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Velocity_label_4.setFont(font)
        self.Velocity_label_4.setObjectName("Velocity_label_4")
        self.Velocity_Unit_label = QtWidgets.QLabel(self.frame)
        self.Velocity_Unit_label.setGeometry(QtCore.QRect(250, 290, 41, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Velocity_Unit_label.sizePolicy().hasHeightForWidth())
        self.Velocity_Unit_label.setSizePolicy(sizePolicy)
        self.Velocity_Unit_label.setObjectName("Velocity_Unit_label")
        self.excerise_count = QtWidgets.QDoubleSpinBox(self.frame)
        self.excerise_count.setEnabled(True)
        self.excerise_count.setGeometry(QtCore.QRect(110, 430, 64, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excerise_count.sizePolicy().hasHeightForWidth())
        self.excerise_count.setSizePolicy(sizePolicy)
        self.excerise_count.setDecimals(0)
        self.excerise_count.setMinimum(0.0)
        self.excerise_count.setMaximum(1000.0)
        self.excerise_count.setSingleStep(0.1)
        self.excerise_count.setProperty("value", 80.0)
        self.excerise_count.setObjectName("excerise_count")
        self.Serial_Port_Lists_label = QtWidgets.QLabel(self.frame)
        self.Serial_Port_Lists_label.setGeometry(QtCore.QRect(30, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Serial_Port_Lists_label.setFont(font)
        self.Serial_Port_Lists_label.setObjectName("Serial_Port_Lists_label")
        self.blink_bar = QtWidgets.QSlider(self.frame)
        self.blink_bar.setGeometry(QtCore.QRect(260, 160, 221, 22))
        self.blink_bar.setMaximum(100)
        self.blink_bar.setSingleStep(1)
        self.blink_bar.setPageStep(10)
        self.blink_bar.setProperty("value", 40)
        self.blink_bar.setOrientation(QtCore.Qt.Horizontal)
        self.blink_bar.setObjectName("blink_bar")
        self.distance_threshold = QtWidgets.QDoubleSpinBox(self.frame)
        self.distance_threshold.setEnabled(True)
        self.distance_threshold.setGeometry(QtCore.QRect(170, 240, 64, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_threshold.sizePolicy().hasHeightForWidth())
        self.distance_threshold.setSizePolicy(sizePolicy)
        self.distance_threshold.setDecimals(2)
        self.distance_threshold.setMinimum(0.0)
        self.distance_threshold.setMaximum(2.0)
        self.distance_threshold.setSingleStep(0.01)
        self.distance_threshold.setProperty("value", 0.0)
        self.distance_threshold.setObjectName("distance_threshold")
        self.Time_Hour_lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.Time_Hour_lcdNumber.setGeometry(QtCore.QRect(136, 500, 51, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Hour_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Time_Hour_lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Time_Hour_lcdNumber.setFont(font)
        self.Time_Hour_lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Time_Hour_lcdNumber.setSmallDecimalPoint(False)
        self.Time_Hour_lcdNumber.setDigitCount(2)
        self.Time_Hour_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Time_Hour_lcdNumber.setProperty("value", 0.0)
        self.Time_Hour_lcdNumber.setObjectName("Time_Hour_lcdNumber")
        self.blink_threshold = QtWidgets.QDoubleSpinBox(self.frame)
        self.blink_threshold.setEnabled(True)
        self.blink_threshold.setGeometry(QtCore.QRect(170, 160, 64, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blink_threshold.sizePolicy().hasHeightForWidth())
        self.blink_threshold.setSizePolicy(sizePolicy)
        self.blink_threshold.setDecimals(1)
        self.blink_threshold.setMinimum(0.0)
        self.blink_threshold.setMaximum(10.0)
        self.blink_threshold.setSingleStep(0.1)
        self.blink_threshold.setProperty("value", 4.0)
        self.blink_threshold.setObjectName("blink_threshold")
        self.Velocity_label = QtWidgets.QLabel(self.frame)
        self.Velocity_label.setGeometry(QtCore.QRect(20, 290, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Velocity_label.sizePolicy().hasHeightForWidth())
        self.Velocity_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Velocity_label.setFont(font)
        self.Velocity_label.setObjectName("Velocity_label")
        self.Position_Platform_label_3 = QtWidgets.QLabel(self.frame)
        self.Position_Platform_label_3.setGeometry(QtCore.QRect(20, 240, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Position_Platform_label_3.setFont(font)
        self.Position_Platform_label_3.setObjectName("Position_Platform_label_3")
        self.Position_Platform_label_2 = QtWidgets.QLabel(self.frame)
        self.Position_Platform_label_2.setGeometry(QtCore.QRect(20, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Position_Platform_label_2.setFont(font)
        self.Position_Platform_label_2.setObjectName("Position_Platform_label_2")
        self.Time_Minute_label_2 = QtWidgets.QLabel(self.frame)
        self.Time_Minute_label_2.setGeometry(QtCore.QRect(440, 500, 91, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Minute_label_2.sizePolicy().hasHeightForWidth())
        self.Time_Minute_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Time_Minute_label_2.setFont(font)
        self.Time_Minute_label_2.setObjectName("Time_Minute_label_2")
        self.Velocity_Unit_label_2 = QtWidgets.QLabel(self.frame)
        self.Velocity_Unit_label_2.setGeometry(QtCore.QRect(250, 330, 41, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Velocity_Unit_label_2.sizePolicy().hasHeightForWidth())
        self.Velocity_Unit_label_2.setSizePolicy(sizePolicy)
        self.Velocity_Unit_label_2.setObjectName("Velocity_Unit_label_2")
        self.Position_Platform_label = QtWidgets.QLabel(self.frame)
        self.Position_Platform_label.setGeometry(QtCore.QRect(20, 160, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Position_Platform_label.setFont(font)
        self.Position_Platform_label.setObjectName("Position_Platform_label")
        self.Progress_progressBar = QtWidgets.QProgressBar(self.frame)
        self.Progress_progressBar.setGeometry(QtCore.QRect(20, 530, 491, 31))
        self.Progress_progressBar.setProperty("value", 0)
        self.Progress_progressBar.setObjectName("Progress_progressBar")
        self.resting_time = QtWidgets.QDoubleSpinBox(self.frame)
        self.resting_time.setEnabled(True)
        self.resting_time.setGeometry(QtCore.QRect(170, 330, 64, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resting_time.sizePolicy().hasHeightForWidth())
        self.resting_time.setSizePolicy(sizePolicy)
        self.resting_time.setDecimals(2)
        self.resting_time.setMinimum(0.0)
        self.resting_time.setMaximum(60.0)
        self.resting_time.setSingleStep(1.0)
        self.resting_time.setProperty("value", 5.0)
        self.resting_time.setObjectName("resting_time")
        self.confirm_push = QtWidgets.QPushButton(self.frame)
        self.confirm_push.setEnabled(True)
        self.confirm_push.setGeometry(QtCore.QRect(340, 10, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_push.sizePolicy().hasHeightForWidth())
        self.confirm_push.setSizePolicy(sizePolicy)
        self.confirm_push.setObjectName("confirm_push")
        self.bright_threshold = QtWidgets.QDoubleSpinBox(self.frame)
        self.bright_threshold.setEnabled(True)
        self.bright_threshold.setGeometry(QtCore.QRect(170, 200, 64, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bright_threshold.sizePolicy().hasHeightForWidth())
        self.bright_threshold.setSizePolicy(sizePolicy)
        self.bright_threshold.setDecimals(0)
        self.bright_threshold.setMinimum(0.0)
        self.bright_threshold.setMaximum(1000.0)
        self.bright_threshold.setSingleStep(0.1)
        self.bright_threshold.setProperty("value", 80.0)
        self.bright_threshold.setObjectName("bright_threshold")
        self.Time_Second_lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.Time_Second_lcdNumber.setGeometry(QtCore.QRect(376, 500, 51, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Second_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Time_Second_lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Time_Second_lcdNumber.setFont(font)
        self.Time_Second_lcdNumber.setDigitCount(2)
        self.Time_Second_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Time_Second_lcdNumber.setObjectName("Time_Second_lcdNumber")
        self.user_list = QtWidgets.QComboBox(self.frame)
        self.user_list.setGeometry(QtCore.QRect(140, 10, 161, 31))
        self.user_list.setObjectName("user_list")
        self.Time_Hour_label = QtWidgets.QLabel(self.frame)
        self.Time_Hour_label.setGeometry(QtCore.QRect(200, 500, 51, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Hour_label.sizePolicy().hasHeightForWidth())
        self.Time_Hour_label.setSizePolicy(sizePolicy)
        self.Time_Hour_label.setObjectName("Time_Hour_label")
        self.bright_bar = QtWidgets.QSlider(self.frame)
        self.bright_bar.setGeometry(QtCore.QRect(260, 200, 221, 22))
        self.bright_bar.setMaximum(255)
        self.bright_bar.setPageStep(10)
        self.bright_bar.setProperty("value", 80)
        self.bright_bar.setSliderPosition(80)
        self.bright_bar.setOrientation(QtCore.Qt.Horizontal)
        self.bright_bar.setObjectName("bright_bar")
        self.Velocity_label_3 = QtWidgets.QLabel(self.frame)
        self.Velocity_label_3.setGeometry(QtCore.QRect(20, 380, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Velocity_label_3.sizePolicy().hasHeightForWidth())
        self.Velocity_label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Velocity_label_3.setFont(font)
        self.Velocity_label_3.setObjectName("Velocity_label_3")
        self.add_user = QtWidgets.QLineEdit(self.frame)
        self.add_user.setGeometry(QtCore.QRect(140, 50, 161, 31))
        self.add_user.setObjectName("add_user")
        self.Serial_Port_Lists_label_2 = QtWidgets.QLabel(self.frame)
        self.Serial_Port_Lists_label_2.setGeometry(QtCore.QRect(30, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Serial_Port_Lists_label_2.setFont(font)
        self.Serial_Port_Lists_label_2.setObjectName("Serial_Port_Lists_label_2")
        self.Velocity_label_2 = QtWidgets.QLabel(self.frame)
        self.Velocity_label_2.setGeometry(QtCore.QRect(20, 330, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Velocity_label_2.sizePolicy().hasHeightForWidth())
        self.Velocity_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Velocity_label_2.setFont(font)
        self.Velocity_label_2.setObjectName("Velocity_label_2")
        self.exercise = QtWidgets.QComboBox(self.frame)
        self.exercise.setEnabled(True)
        self.exercise.setGeometry(QtCore.QRect(110, 380, 161, 31))
        self.exercise.setObjectName("exercise")
        self.Time_Minute_label = QtWidgets.QLabel(self.frame)
        self.Time_Minute_label.setGeometry(QtCore.QRect(310, 500, 81, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Minute_label.sizePolicy().hasHeightForWidth())
        self.Time_Minute_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Time_Minute_label.setFont(font)
        self.Time_Minute_label.setObjectName("Time_Minute_label")
        self.Time_Title_label = QtWidgets.QLabel(self.frame)
        self.Time_Title_label.setGeometry(QtCore.QRect(20, 500, 101, 16))
        self.Time_Title_label.setObjectName("Time_Title_label")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 470, 471, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.distance_bar = QtWidgets.QSlider(self.frame)
        self.distance_bar.setGeometry(QtCore.QRect(260, 240, 221, 22))
        self.distance_bar.setMaximum(200)
        self.distance_bar.setPageStep(10)
        self.distance_bar.setOrientation(QtCore.Qt.Horizontal)
        self.distance_bar.setObjectName("distance_bar")
        self.camera_label = QtWidgets.QLabel(self.frame)
        self.camera_label.setGeometry(QtCore.QRect(520, 0, 800, 600))
        self.camera_label.setText("")
        self.camera_label.setObjectName("camera_label")
        self.line_token = QtWidgets.QLineEdit(self.frame)
        self.line_token.setEnabled(False)
        self.line_token.setGeometry(QtCore.QRect(140, 90, 301, 31))
        self.line_token.setObjectName("line_token")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(10, 130, 471, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.want_line = QtWidgets.QCheckBox(self.frame)
        self.want_line.setEnabled(True)
        self.want_line.setGeometry(QtCore.QRect(110, 100, 91, 16))
        self.want_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.want_line.setText("")
        self.want_line.setChecked(False)
        self.want_line.setObjectName("want_line")
        self.Serial_Port_Lists_label_5 = QtWidgets.QLabel(self.frame)
        self.Serial_Port_Lists_label_5.setGeometry(QtCore.QRect(30, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Serial_Port_Lists_label_5.setFont(font)
        self.Serial_Port_Lists_label_5.setObjectName("Serial_Port_Lists_label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 560, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(390, 570, 58, 41))
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.use_time_graph = QtWidgets.QLabel(self.page_2)
        self.use_time_graph.setGeometry(QtCore.QRect(380, 10, 400, 270))
        self.use_time_graph.setText("")
        self.use_time_graph.setObjectName("use_time_graph")
        self.distance_graph = QtWidgets.QLabel(self.page_2)
        self.distance_graph.setGeometry(QtCore.QRect(380, 330, 400, 270))
        self.distance_graph.setText("")
        self.distance_graph.setObjectName("distance_graph")
        self.blink_graph = QtWidgets.QLabel(self.page_2)
        self.blink_graph.setGeometry(QtCore.QRect(820, 10, 400, 270))
        self.blink_graph.setText("")
        self.blink_graph.setObjectName("blink_graph")
        self.brightness_graph = QtWidgets.QLabel(self.page_2)
        self.brightness_graph.setGeometry(QtCore.QRect(820, 330, 400, 270))
        self.brightness_graph.setText("")
        self.brightness_graph.setObjectName("brightness_graph")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_2)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 140, 321, 229))
        self.calendarWidget.setObjectName("calendarWidget")
        self.select_range = QtWidgets.QComboBox(self.page_2)
        self.select_range.setGeometry(QtCore.QRect(120, 10, 191, 31))
        self.select_range.setObjectName("select_range")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_4.setObjectName("label_4")
        self.user_list_2 = QtWidgets.QComboBox(self.page_2)
        self.user_list_2.setGeometry(QtCore.QRect(140, 60, 171, 31))
        self.user_list_2.setObjectName("user_list_2")
        self.Serial_Port_Lists_label_3 = QtWidgets.QLabel(self.page_2)
        self.Serial_Port_Lists_label_3.setGeometry(QtCore.QRect(10, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Serial_Port_Lists_label_3.setFont(font)
        self.Serial_Port_Lists_label_3.setObjectName("Serial_Port_Lists_label_3")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Eye protector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("Dialog", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyze), _translate("Dialog", "Analyze"))
        self.start_push.setText(_translate("Dialog", "Start"))
        self.initialize_push.setText(_translate("Dialog", "Initialize"))
        self.add_push.setText(_translate("Dialog", "Add"))
        self.Velocity_label_4.setText(_translate("Dialog", "Number : "))
        self.Velocity_Unit_label.setText(_translate("Dialog", "min"))
        self.Serial_Port_Lists_label.setText(_translate("Dialog", "Choose User"))
        self.Velocity_label.setText(_translate("Dialog", "Working Time"))
        self.Position_Platform_label_3.setText(_translate("Dialog", "Distance Threshold"))
        self.Position_Platform_label_2.setText(_translate("Dialog", "Brightness Threshold"))
        self.Time_Minute_label_2.setText(_translate("Dialog", "second"))
        self.Velocity_Unit_label_2.setText(_translate("Dialog", "min"))
        self.Position_Platform_label.setText(_translate("Dialog", "Blink Threshold"))
        self.confirm_push.setText(_translate("Dialog", "Confirm"))
        self.Time_Hour_label.setText(_translate("Dialog", "hour"))
        self.Velocity_label_3.setText(_translate("Dialog", "Exercise :"))
        self.Serial_Port_Lists_label_2.setText(_translate("Dialog", "Add User"))
        self.Velocity_label_2.setText(_translate("Dialog", "Resting Time"))
        self.Time_Minute_label.setText(_translate("Dialog", "minute"))
        self.Time_Title_label.setText(_translate("Dialog", "Time remain:"))
        self.Serial_Port_Lists_label_5.setText(_translate("Dialog", "Use Line "))
        self.label_2.setText(_translate("Dialog", "Your donation can help me keep improving the program :"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.buymeacoffee.com/eye_protector\"><span style=\" text-decoration: underline; color:#0000ff;\">Link</span></a></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Plot Range :"))
        self.Serial_Port_Lists_label_3.setText(_translate("Dialog", "Choose User :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

