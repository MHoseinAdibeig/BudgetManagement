# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AccuntingApp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(712, 606)
        MainWindow.setMinimumSize(QSize(712, 606))
        MainWindow.setMaximumSize(QSize(712, 606))
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 250, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop:0 rgba(245, 240, 235, 255), stop:1 rgba(255, 255, 255, 255));")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(550, 50, 160, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_dashboard = QPushButton(self.verticalLayoutWidget)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dashboard.sizePolicy().hasHeightForWidth())
        self.btn_dashboard.setSizePolicy(sizePolicy)
        self.btn_dashboard.setStyleSheet(u"border-radius: 50px;")

        self.verticalLayout.addWidget(self.btn_dashboard)

        self.btn_person = QPushButton(self.verticalLayoutWidget)
        self.btn_person.setObjectName(u"btn_person")
        sizePolicy.setHeightForWidth(self.btn_person.sizePolicy().hasHeightForWidth())
        self.btn_person.setSizePolicy(sizePolicy)
        self.btn_person.setLayoutDirection(Qt.RightToLeft)
        self.btn_person.setStyleSheet(u"border-radius: 50px;\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")

        self.verticalLayout.addWidget(self.btn_person)

        self.btn_data = QPushButton(self.verticalLayoutWidget)
        self.btn_data.setObjectName(u"btn_data")
        sizePolicy.setHeightForWidth(self.btn_data.sizePolicy().hasHeightForWidth())
        self.btn_data.setSizePolicy(sizePolicy)
        self.btn_data.setStyleSheet(u"border-radius: 50px;")

        self.verticalLayout.addWidget(self.btn_data)

        self.btn_tafazol = QPushButton(self.verticalLayoutWidget)
        self.btn_tafazol.setObjectName(u"btn_tafazol")
        self.btn_tafazol.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_tafazol.sizePolicy().hasHeightForWidth())
        self.btn_tafazol.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"N02Jeyran"])
        self.btn_tafazol.setFont(font)
        self.btn_tafazol.setStyleSheet(u"border-radius: 50px;")
        self.btn_tafazol.setFlat(False)

        self.verticalLayout.addWidget(self.btn_tafazol)

        self.btn_manage = QPushButton(self.verticalLayoutWidget)
        self.btn_manage.setObjectName(u"btn_manage")
        sizePolicy.setHeightForWidth(self.btn_manage.sizePolicy().hasHeightForWidth())
        self.btn_manage.setSizePolicy(sizePolicy)
        self.btn_manage.setStyleSheet(u"border-radius: 50px;")

        self.verticalLayout.addWidget(self.btn_manage)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"B Nazanin"])
        self.pushButton_8.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.btn_call = QPushButton(self.verticalLayoutWidget)
        self.btn_call.setObjectName(u"btn_call")
        sizePolicy2.setHeightForWidth(self.btn_call.sizePolicy().hasHeightForWidth())
        self.btn_call.setSizePolicy(sizePolicy2)
        self.btn_call.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_call)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(-2, 0, 711, 51))
        self.groupBox.setMinimumSize(QSize(711, 51))
        self.groupBox.setMaximumSize(QSize(711, 51))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(740, 0, 61, 49))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(50, 0))
        font2 = QFont()
        font2.setFamilies([u"B Titr"])
        font2.setPointSize(17)
        self.label.setFont(font2)
        self.lbl_calender_2 = QLabel(self.groupBox)
        self.lbl_calender_2.setObjectName(u"lbl_calender_2")
        self.lbl_calender_2.setGeometry(QRect(550, 16, 71, 20))
        font3 = QFont()
        font3.setPointSize(9)
        self.lbl_calender_2.setFont(font3)
        self.lbl_calender_2.setStyleSheet(u"")
        self.lbl_0 = QLabel(self.groupBox)
        self.lbl_0.setObjectName(u"lbl_0")
        self.lbl_0.setGeometry(QRect(520, 15, 21, 21))
        font4 = QFont()
        font4.setPointSize(7)
        self.lbl_0.setFont(font4)
        self.lbl_0.setStyleSheet(u"image: url(:/icons/calendar.png);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 20, 51, 21))
        self.label_2.setStyleSheet(u"image: url(:/icons/profile.png);")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 20, 41, 21))
        self.label_3.setStyleSheet(u"image: url(:/icons/refresh.png);")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(636, 13, 61, 21))
        self.label_6.setStyleSheet(u"image: url(:/icons/logo-no-background.png);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(4, 50, 540, 531))
        self.tableWidget.setMinimumSize(QSize(540, 531))
        self.tableWidget.setMaximumSize(QSize(540, 531))
        font5 = QFont()
        font5.setFamilies([u"B Nazanin"])
        font5.setPointSize(10)
        self.tableWidget.setFont(font5)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(37)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-12, 50, 581, 531))
        self.label_4.setStyleSheet(u"image: url(:/icons/dash.jpg);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(568, 442, 141, 141))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(:/icons/inno-tech.png);\n"
"\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_4.raise_()
        self.tableWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.groupBox.raise_()
        self.label_5.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0627\u0634\u0628\u0648\u0631\u062f", None))
        self.btn_person.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0634\u062e\u0627\u0635", None))
        self.btn_data.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u0644\u06cc\u0644 \u062f\u0627\u062f\u0647", None))
        self.btn_tafazol.setText(QCoreApplication.translate("MainWindow", u"\u0645\u063a\u0627\u06cc\u0631\u062a \u06af\u06cc\u0631\u06cc", None))
        self.btn_manage.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u0628\u0648\u062f\u062c\u0647 \u0631\u06cc\u0632\u06cc", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0634\u062a\u06cc\u0628\u0627\u0646\u06cc", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0644\u0627\u06af", None))
        self.btn_call.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0645\u0627\u0633 \u0628\u0627 \u0645\u0627", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0622\u0628\u0627\u06a9", None))
        self.lbl_calender_2.setText(QCoreApplication.translate("MainWindow", u"1402-07-18", None))
        self.lbl_0.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_6.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"dafter", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"bank", None));
        self.label_4.setText("")
        self.label_5.setText("")
    # retranslateUi

