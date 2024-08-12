# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_mainAzIUvJ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(1100, 625)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_main.sizePolicy().hasHeightForWidth())
        frm_main.setSizePolicy(sizePolicy)
        frm_main.setMinimumSize(QSize(1100, 625))
        frm_main.setMaximumSize(QSize(3000, 1000))
        self.actionTest = QAction(frm_main)
        self.actionTest.setObjectName(u"actionTest")
        self.actionEinstellungen = QAction(frm_main)
        self.actionEinstellungen.setObjectName(u"actionEinstellungen")
        self.main_widget = QWidget(frm_main)
        self.main_widget.setObjectName(u"main_widget")
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy)
        self.main_widget.setMinimumSize(QSize(1100, 476))
        self.gridLayout_6 = QGridLayout(self.main_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(50000, 50000))
        self.pg_settings = QWidget()
        self.pg_settings.setObjectName(u"pg_settings")
        self.gridLayout_4 = QGridLayout(self.pg_settings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_OtherOrdner = QLabel(self.pg_settings)
        self.lb_OtherOrdner.setObjectName(u"lb_OtherOrdner")

        self.gridLayout_4.addWidget(self.lb_OtherOrdner, 12, 1, 1, 2)

        self.lb_emptylower = QLabel(self.pg_settings)
        self.lb_emptylower.setObjectName(u"lb_emptylower")

        self.gridLayout_4.addWidget(self.lb_emptylower, 22, 0, 1, 3)

        self.df_pathHS = QLabel(self.pg_settings)
        self.df_pathHS.setObjectName(u"df_pathHS")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.df_pathHS.sizePolicy().hasHeightForWidth())
        self.df_pathHS.setSizePolicy(sizePolicy1)
        self.df_pathHS.setMinimumSize(QSize(0, 25))
        self.df_pathHS.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.df_pathHS, 16, 0, 1, 4)

        self.lb_CC = QLabel(self.pg_settings)
        self.lb_CC.setObjectName(u"lb_CC")
        self.lb_CC.setMinimumSize(QSize(0, 25))
        self.lb_CC.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_CC, 4, 0, 1, 3)

        self.lb_emptyline_2 = QLabel(self.pg_settings)
        self.lb_emptyline_2.setObjectName(u"lb_emptyline_2")
        sizePolicy1.setHeightForWidth(self.lb_emptyline_2.sizePolicy().hasHeightForWidth())
        self.lb_emptyline_2.setSizePolicy(sizePolicy1)
        self.lb_emptyline_2.setMinimumSize(QSize(0, 15))
        self.lb_emptyline_2.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.lb_emptyline_2, 14, 0, 1, 3)

        self.label_6 = QLabel(self.pg_settings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 15, 1, 1, 2)

        self.lb_emptyline_5 = QLabel(self.pg_settings)
        self.lb_emptyline_5.setObjectName(u"lb_emptyline_5")
        sizePolicy1.setHeightForWidth(self.lb_emptyline_5.sizePolicy().hasHeightForWidth())
        self.lb_emptyline_5.setSizePolicy(sizePolicy1)
        self.lb_emptyline_5.setMinimumSize(QSize(0, 15))
        self.lb_emptyline_5.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.lb_emptyline_5, 18, 0, 1, 3)

        self.lb_emptyline_3 = QLabel(self.pg_settings)
        self.lb_emptyline_3.setObjectName(u"lb_emptyline_3")
        sizePolicy1.setHeightForWidth(self.lb_emptyline_3.sizePolicy().hasHeightForWidth())
        self.lb_emptyline_3.setSizePolicy(sizePolicy1)
        self.lb_emptyline_3.setMinimumSize(QSize(0, 15))
        self.lb_emptyline_3.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.lb_emptyline_3, 8, 0, 1, 2)

        self.btn_pathdf = QPushButton(self.pg_settings)
        self.btn_pathdf.setObjectName(u"btn_pathdf")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_pathdf.sizePolicy().hasHeightForWidth())
        self.btn_pathdf.setSizePolicy(sizePolicy2)
        self.btn_pathdf.setMinimumSize(QSize(120, 25))
        self.btn_pathdf.setMaximumSize(QSize(120, 25))

        self.gridLayout_4.addWidget(self.btn_pathdf, 12, 0, 1, 1)

        self.btn_pathhs = QPushButton(self.pg_settings)
        self.btn_pathhs.setObjectName(u"btn_pathhs")
        sizePolicy2.setHeightForWidth(self.btn_pathhs.sizePolicy().hasHeightForWidth())
        self.btn_pathhs.setSizePolicy(sizePolicy2)
        self.btn_pathhs.setMinimumSize(QSize(120, 25))
        self.btn_pathhs.setMaximumSize(QSize(120, 25))

        self.gridLayout_4.addWidget(self.btn_pathhs, 15, 0, 1, 1)

        self.df_CC = QLineEdit(self.pg_settings)
        self.df_CC.setObjectName(u"df_CC")
        self.df_CC.setMinimumSize(QSize(0, 25))
        self.df_CC.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.df_CC, 5, 0, 1, 3)

        self.lb_emptyline = QLabel(self.pg_settings)
        self.lb_emptyline.setObjectName(u"lb_emptyline")
        self.lb_emptyline.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lb_emptyline.sizePolicy().hasHeightForWidth())
        self.lb_emptyline.setSizePolicy(sizePolicy1)
        self.lb_emptyline.setMinimumSize(QSize(0, 15))
        self.lb_emptyline.setMaximumSize(QSize(5000, 15))

        self.gridLayout_4.addWidget(self.lb_emptyline, 3, 0, 1, 3)

        self.btn_pathma = QPushButton(self.pg_settings)
        self.btn_pathma.setObjectName(u"btn_pathma")
        sizePolicy2.setHeightForWidth(self.btn_pathma.sizePolicy().hasHeightForWidth())
        self.btn_pathma.setSizePolicy(sizePolicy2)
        self.btn_pathma.setMinimumSize(QSize(120, 25))
        self.btn_pathma.setMaximumSize(QSize(120, 25))

        self.gridLayout_4.addWidget(self.btn_pathma, 9, 0, 1, 1)

        self.df_pathDF = QLabel(self.pg_settings)
        self.df_pathDF.setObjectName(u"df_pathDF")
        sizePolicy1.setHeightForWidth(self.df_pathDF.sizePolicy().hasHeightForWidth())
        self.df_pathDF.setSizePolicy(sizePolicy1)
        self.df_pathDF.setMinimumSize(QSize(0, 25))
        self.df_pathDF.setAutoFillBackground(False)

        self.gridLayout_4.addWidget(self.df_pathDF, 13, 0, 1, 3)

        self.df_weeks = QSpinBox(self.pg_settings)
        self.df_weeks.setObjectName(u"df_weeks")
        sizePolicy2.setHeightForWidth(self.df_weeks.sizePolicy().hasHeightForWidth())
        self.df_weeks.setSizePolicy(sizePolicy2)
        self.df_weeks.setMinimumSize(QSize(120, 25))
        self.df_weeks.setMaximumSize(QSize(120, 25))

        self.gridLayout_4.addWidget(self.df_weeks, 7, 0, 1, 1)

        self.lb_empty_8 = QLabel(self.pg_settings)
        self.lb_empty_8.setObjectName(u"lb_empty_8")
        sizePolicy2.setHeightForWidth(self.lb_empty_8.sizePolicy().hasHeightForWidth())
        self.lb_empty_8.setSizePolicy(sizePolicy2)
        self.lb_empty_8.setMinimumSize(QSize(0, 15))
        self.lb_empty_8.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.lb_empty_8, 6, 0, 1, 3)

        self.btn_svchange = QPushButton(self.pg_settings)
        self.btn_svchange.setObjectName(u"btn_svchange")
        sizePolicy2.setHeightForWidth(self.btn_svchange.sizePolicy().hasHeightForWidth())
        self.btn_svchange.setSizePolicy(sizePolicy2)
        self.btn_svchange.setMinimumSize(QSize(120, 25))
        self.btn_svchange.setMaximumSize(QSize(120, 25))

        self.gridLayout_4.addWidget(self.btn_svchange, 1, 0, 1, 1)

        self.lb_empty_2 = QLabel(self.pg_settings)
        self.lb_empty_2.setObjectName(u"lb_empty_2")

        self.gridLayout_4.addWidget(self.lb_empty_2, 15, 3, 1, 1)

        self.lb_Weeks = QLabel(self.pg_settings)
        self.lb_Weeks.setObjectName(u"lb_Weeks")
        self.lb_Weeks.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_Weeks, 7, 1, 1, 2)

        self.lb_emptyline_4 = QLabel(self.pg_settings)
        self.lb_emptyline_4.setObjectName(u"lb_emptyline_4")
        sizePolicy1.setHeightForWidth(self.lb_emptyline_4.sizePolicy().hasHeightForWidth())
        self.lb_emptyline_4.setSizePolicy(sizePolicy1)
        self.lb_emptyline_4.setMinimumSize(QSize(0, 15))
        self.lb_emptyline_4.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.lb_emptyline_4, 11, 0, 1, 2)

        self.df_pathIM = QLabel(self.pg_settings)
        self.df_pathIM.setObjectName(u"df_pathIM")
        sizePolicy1.setHeightForWidth(self.df_pathIM.sizePolicy().hasHeightForWidth())
        self.df_pathIM.setSizePolicy(sizePolicy1)
        self.df_pathIM.setMinimumSize(QSize(0, 25))
        self.df_pathIM.setMaximumSize(QSize(16777215, 25))
        self.df_pathIM.setAutoFillBackground(False)

        self.gridLayout_4.addWidget(self.df_pathIM, 10, 0, 1, 3)

        self.lb_maOrdner = QLabel(self.pg_settings)
        self.lb_maOrdner.setObjectName(u"lb_maOrdner")
        sizePolicy1.setHeightForWidth(self.lb_maOrdner.sizePolicy().hasHeightForWidth())
        self.lb_maOrdner.setSizePolicy(sizePolicy1)
        self.lb_maOrdner.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.lb_maOrdner, 9, 1, 1, 2)

        self.stackedWidget.addWidget(self.pg_settings)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.gridLayout_3 = QGridLayout(self.pg_home)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(400, 50))
        self.label.setMaximumSize(QSize(50, 400))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pg_home)
        self.pg_createHS = QWidget()
        self.pg_createHS.setObjectName(u"pg_createHS")
        self.gridLayout_8 = QGridLayout(self.pg_createHS)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lb_empty_19 = QLabel(self.pg_createHS)
        self.lb_empty_19.setObjectName(u"lb_empty_19")

        self.gridLayout_8.addWidget(self.lb_empty_19, 2, 4, 1, 1)

        self.label_7 = QLabel(self.pg_createHS)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(200)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(200, 0))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_8.addWidget(self.label_7, 2, 0, 1, 1)

        self.lb_DatumHS = QDateEdit(self.pg_createHS)
        self.lb_DatumHS.setObjectName(u"lb_DatumHS")
        sizePolicy2.setHeightForWidth(self.lb_DatumHS.sizePolicy().hasHeightForWidth())
        self.lb_DatumHS.setSizePolicy(sizePolicy2)
        self.lb_DatumHS.setMinimumSize(QSize(300, 30))
        self.lb_DatumHS.setMaximumSize(QSize(300, 30))
        self.lb_DatumHS.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.lb_DatumHS, 1, 1, 1, 1)

        self.btn_generateHS = QPushButton(self.pg_createHS)
        self.btn_generateHS.setObjectName(u"btn_generateHS")
        self.btn_generateHS.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_generateHS.sizePolicy().hasHeightForWidth())
        self.btn_generateHS.setSizePolicy(sizePolicy2)
        self.btn_generateHS.setMinimumSize(QSize(250, 30))
        self.btn_generateHS.setMaximumSize(QSize(250, 30))

        self.gridLayout_8.addWidget(self.btn_generateHS, 2, 3, 1, 1)

        self.lb_empty_18 = QLabel(self.pg_createHS)
        self.lb_empty_18.setObjectName(u"lb_empty_18")

        self.gridLayout_8.addWidget(self.lb_empty_18, 3, 3, 1, 1)

        self.lb_empty_16 = QLabel(self.pg_createHS)
        self.lb_empty_16.setObjectName(u"lb_empty_16")

        self.gridLayout_8.addWidget(self.lb_empty_16, 1, 3, 1, 1)

        self.lb_empty_15 = QLabel(self.pg_createHS)
        self.lb_empty_15.setObjectName(u"lb_empty_15")
        sizePolicy1.setHeightForWidth(self.lb_empty_15.sizePolicy().hasHeightForWidth())
        self.lb_empty_15.setSizePolicy(sizePolicy1)
        self.lb_empty_15.setMinimumSize(QSize(0, 25))
        self.lb_empty_15.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_8.addWidget(self.lb_empty_15, 0, 1, 1, 1)

        self.list_Hochschulen = QListWidget(self.pg_createHS)
        self.list_Hochschulen.setObjectName(u"list_Hochschulen")
        self.list_Hochschulen.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.list_Hochschulen.sizePolicy().hasHeightForWidth())
        self.list_Hochschulen.setSizePolicy(sizePolicy4)
        self.list_Hochschulen.setMinimumSize(QSize(300, 0))
        self.list_Hochschulen.setMaximumSize(QSize(300, 16777215))
        self.list_Hochschulen.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.gridLayout_8.addWidget(self.list_Hochschulen, 2, 1, 2, 1)

        self.label_5 = QLabel(self.pg_createHS)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(200, 30))
        self.label_5.setMaximumSize(QSize(200, 30))

        self.gridLayout_8.addWidget(self.label_5, 1, 0, 1, 1)

        self.lb_empty_17 = QLabel(self.pg_createHS)
        self.lb_empty_17.setObjectName(u"lb_empty_17")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_empty_17.sizePolicy().hasHeightForWidth())
        self.lb_empty_17.setSizePolicy(sizePolicy5)
        self.lb_empty_17.setMinimumSize(QSize(70, 0))
        self.lb_empty_17.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_8.addWidget(self.lb_empty_17, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.pg_createHS)
        self.pg_mail = QWidget()
        self.pg_mail.setObjectName(u"pg_mail")
        self.gridLayout_2 = QGridLayout(self.pg_mail)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_subject = QLineEdit(self.pg_mail)
        self.txt_subject.setObjectName(u"txt_subject")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(40)
        sizePolicy6.setHeightForWidth(self.txt_subject.sizePolicy().hasHeightForWidth())
        self.txt_subject.setSizePolicy(sizePolicy6)
        self.txt_subject.setMaximumSize(QSize(16777215, 40))
        self.txt_subject.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.txt_subject, 2, 1, 1, 1)

        self.txt_content = QPlainTextEdit(self.pg_mail)
        self.txt_content.setObjectName(u"txt_content")

        self.gridLayout_2.addWidget(self.txt_content, 3, 1, 1, 1)

        self.lb_content = QLabel(self.pg_mail)
        self.lb_content.setObjectName(u"lb_content")
        sizePolicy5.setHeightForWidth(self.lb_content.sizePolicy().hasHeightForWidth())
        self.lb_content.setSizePolicy(sizePolicy5)
        self.lb_content.setMinimumSize(QSize(200, 0))
        self.lb_content.setMaximumSize(QSize(200, 16777215))
        self.lb_content.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_content.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_content, 3, 0, 1, 1)

        self.btn_save = QPushButton(self.pg_mail)
        self.btn_save.setObjectName(u"btn_save")

        self.gridLayout_2.addWidget(self.btn_save, 0, 0, 1, 1)

        self.lb_Sub = QLabel(self.pg_mail)
        self.lb_Sub.setObjectName(u"lb_Sub")
        sizePolicy2.setHeightForWidth(self.lb_Sub.sizePolicy().hasHeightForWidth())
        self.lb_Sub.setSizePolicy(sizePolicy2)
        self.lb_Sub.setMinimumSize(QSize(200, 40))
        self.lb_Sub.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.lb_Sub, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.pg_mail)
        self.pg_create = QWidget()
        self.pg_create.setObjectName(u"pg_create")
        self.gridLayout = QGridLayout(self.pg_create)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_Fristenliste = QLabel(self.pg_create)
        self.lb_Fristenliste.setObjectName(u"lb_Fristenliste")
        sizePolicy2.setHeightForWidth(self.lb_Fristenliste.sizePolicy().hasHeightForWidth())
        self.lb_Fristenliste.setSizePolicy(sizePolicy2)
        self.lb_Fristenliste.setMinimumSize(QSize(250, 30))
        self.lb_Fristenliste.setMaximumSize(QSize(250, 30))

        self.gridLayout.addWidget(self.lb_Fristenliste, 1, 0, 1, 1)

        self.lb_empty_4 = QLabel(self.pg_create)
        self.lb_empty_4.setObjectName(u"lb_empty_4")

        self.gridLayout.addWidget(self.lb_empty_4, 9, 0, 1, 1)

        self.cb_Mail = QCheckBox(self.pg_create)
        self.cb_Mail.setObjectName(u"cb_Mail")
        self.cb_Mail.setChecked(True)

        self.gridLayout.addWidget(self.cb_Mail, 4, 0, 1, 1)

        self.pb_BackOffice = QProgressBar(self.pg_create)
        self.pb_BackOffice.setObjectName(u"pb_BackOffice")
        sizePolicy2.setHeightForWidth(self.pb_BackOffice.sizePolicy().hasHeightForWidth())
        self.pb_BackOffice.setSizePolicy(sizePolicy2)
        self.pb_BackOffice.setMinimumSize(QSize(250, 30))
        self.pb_BackOffice.setMaximumSize(QSize(250, 30))
        self.pb_BackOffice.setValue(0)

        self.gridLayout.addWidget(self.pb_BackOffice, 3, 1, 1, 1)

        self.cb_InnoMgr = QCheckBox(self.pg_create)
        self.cb_InnoMgr.setObjectName(u"cb_InnoMgr")
        sizePolicy2.setHeightForWidth(self.cb_InnoMgr.sizePolicy().hasHeightForWidth())
        self.cb_InnoMgr.setSizePolicy(sizePolicy2)
        self.cb_InnoMgr.setMinimumSize(QSize(250, 30))
        self.cb_InnoMgr.setMaximumSize(QSize(250, 30))
        self.cb_InnoMgr.setChecked(True)

        self.gridLayout.addWidget(self.cb_InnoMgr, 2, 0, 1, 1)

        self.lb_empty_3 = QLabel(self.pg_create)
        self.lb_empty_3.setObjectName(u"lb_empty_3")
        sizePolicy1.setHeightForWidth(self.lb_empty_3.sizePolicy().hasHeightForWidth())
        self.lb_empty_3.setSizePolicy(sizePolicy1)
        self.lb_empty_3.setMinimumSize(QSize(0, 25))
        self.lb_empty_3.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lb_empty_3, 0, 0, 1, 1)

        self.pb_Inno = QProgressBar(self.pg_create)
        self.pb_Inno.setObjectName(u"pb_Inno")
        sizePolicy2.setHeightForWidth(self.pb_Inno.sizePolicy().hasHeightForWidth())
        self.pb_Inno.setSizePolicy(sizePolicy2)
        self.pb_Inno.setMinimumSize(QSize(250, 30))
        self.pb_Inno.setMaximumSize(QSize(250, 30))
        self.pb_Inno.setValue(0)

        self.gridLayout.addWidget(self.pb_Inno, 2, 1, 1, 1)

        self.lb_empty_7 = QLabel(self.pg_create)
        self.lb_empty_7.setObjectName(u"lb_empty_7")

        self.gridLayout.addWidget(self.lb_empty_7, 3, 2, 1, 1)

        self.lb_Datum = QDateEdit(self.pg_create)
        self.lb_Datum.setObjectName(u"lb_Datum")
        self.lb_Datum.setMinimumSize(QSize(0, 30))
        self.lb_Datum.setMaximumSize(QSize(16777215, 30))
        self.lb_Datum.setCalendarPopup(True)

        self.gridLayout.addWidget(self.lb_Datum, 1, 1, 1, 1)

        self.lb_empty_6 = QLabel(self.pg_create)
        self.lb_empty_6.setObjectName(u"lb_empty_6")
        sizePolicy1.setHeightForWidth(self.lb_empty_6.sizePolicy().hasHeightForWidth())
        self.lb_empty_6.setSizePolicy(sizePolicy1)
        self.lb_empty_6.setMinimumSize(QSize(0, 25))
        self.lb_empty_6.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lb_empty_6, 5, 0, 1, 1)

        self.btn_generate = QPushButton(self.pg_create)
        self.btn_generate.setObjectName(u"btn_generate")
        sizePolicy2.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy2)
        self.btn_generate.setMinimumSize(QSize(250, 30))
        self.btn_generate.setMaximumSize(QSize(250, 30))

        self.gridLayout.addWidget(self.btn_generate, 4, 1, 1, 1)

        self.cb_BackOffice = QCheckBox(self.pg_create)
        self.cb_BackOffice.setObjectName(u"cb_BackOffice")
        sizePolicy2.setHeightForWidth(self.cb_BackOffice.sizePolicy().hasHeightForWidth())
        self.cb_BackOffice.setSizePolicy(sizePolicy2)
        self.cb_BackOffice.setMinimumSize(QSize(250, 30))
        self.cb_BackOffice.setMaximumSize(QSize(250, 30))
        self.cb_BackOffice.setChecked(True)

        self.gridLayout.addWidget(self.cb_BackOffice, 3, 0, 1, 1)

        self.lb_empty_5 = QLabel(self.pg_create)
        self.lb_empty_5.setObjectName(u"lb_empty_5")

        self.gridLayout.addWidget(self.lb_empty_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.pg_create)
        self.pg_createMA = QWidget()
        self.pg_createMA.setObjectName(u"pg_createMA")
        self.gridLayout_7 = QGridLayout(self.pg_createMA)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btn_generateMA = QPushButton(self.pg_createMA)
        self.btn_generateMA.setObjectName(u"btn_generateMA")
        self.btn_generateMA.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_generateMA.sizePolicy().hasHeightForWidth())
        self.btn_generateMA.setSizePolicy(sizePolicy2)
        self.btn_generateMA.setMinimumSize(QSize(250, 30))
        self.btn_generateMA.setMaximumSize(QSize(250, 30))

        self.gridLayout_7.addWidget(self.btn_generateMA, 5, 3, 1, 1)

        self.lb_DatumMA = QDateEdit(self.pg_createMA)
        self.lb_DatumMA.setObjectName(u"lb_DatumMA")
        sizePolicy2.setHeightForWidth(self.lb_DatumMA.sizePolicy().hasHeightForWidth())
        self.lb_DatumMA.setSizePolicy(sizePolicy2)
        self.lb_DatumMA.setMinimumSize(QSize(250, 30))
        self.lb_DatumMA.setMaximumSize(QSize(250, 30))
        self.lb_DatumMA.setCalendarPopup(True)

        self.gridLayout_7.addWidget(self.lb_DatumMA, 1, 1, 1, 1)

        self.label_3 = QLabel(self.pg_createMA)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(200, 30))
        self.label_3.setMaximumSize(QSize(200, 30))

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)

        self.rb_InnoMgr = QRadioButton(self.pg_createMA)
        self.rb_InnoMgr.setObjectName(u"rb_InnoMgr")
        sizePolicy2.setHeightForWidth(self.rb_InnoMgr.sizePolicy().hasHeightForWidth())
        self.rb_InnoMgr.setSizePolicy(sizePolicy2)
        self.rb_InnoMgr.setMinimumSize(QSize(250, 30))
        self.rb_InnoMgr.setMaximumSize(QSize(250, 30))

        self.gridLayout_7.addWidget(self.rb_InnoMgr, 2, 1, 1, 1)

        self.label_2 = QLabel(self.pg_createMA)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(200, 30))
        self.label_2.setMaximumSize(QSize(200, 30))

        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)

        self.list_Mitarbeiter = QListWidget(self.pg_createMA)
        self.list_Mitarbeiter.setObjectName(u"list_Mitarbeiter")
        self.list_Mitarbeiter.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.list_Mitarbeiter.sizePolicy().hasHeightForWidth())
        self.list_Mitarbeiter.setSizePolicy(sizePolicy4)
        self.list_Mitarbeiter.setMinimumSize(QSize(250, 0))
        self.list_Mitarbeiter.setMaximumSize(QSize(250, 16777215))
        self.list_Mitarbeiter.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.gridLayout_7.addWidget(self.list_Mitarbeiter, 4, 1, 3, 1)

        self.label_4 = QLabel(self.pg_createMA)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_7.addWidget(self.label_4, 4, 0, 1, 1)

        self.rb_weitereMA = QRadioButton(self.pg_createMA)
        self.rb_weitereMA.setObjectName(u"rb_weitereMA")
        sizePolicy2.setHeightForWidth(self.rb_weitereMA.sizePolicy().hasHeightForWidth())
        self.rb_weitereMA.setSizePolicy(sizePolicy2)
        self.rb_weitereMA.setMinimumSize(QSize(250, 30))
        self.rb_weitereMA.setMaximumSize(QSize(250, 30))

        self.gridLayout_7.addWidget(self.rb_weitereMA, 3, 1, 1, 1)

        self.cb_MailMA = QCheckBox(self.pg_createMA)
        self.cb_MailMA.setObjectName(u"cb_MailMA")
        self.cb_MailMA.setEnabled(False)

        self.gridLayout_7.addWidget(self.cb_MailMA, 4, 3, 1, 1)

        self.lb_empty_12 = QLabel(self.pg_createMA)
        self.lb_empty_12.setObjectName(u"lb_empty_12")

        self.gridLayout_7.addWidget(self.lb_empty_12, 6, 3, 1, 1)

        self.lb_empty_10 = QLabel(self.pg_createMA)
        self.lb_empty_10.setObjectName(u"lb_empty_10")
        sizePolicy1.setHeightForWidth(self.lb_empty_10.sizePolicy().hasHeightForWidth())
        self.lb_empty_10.setSizePolicy(sizePolicy1)
        self.lb_empty_10.setMinimumSize(QSize(0, 25))
        self.lb_empty_10.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_7.addWidget(self.lb_empty_10, 0, 0, 1, 2)

        self.lb_empty_13 = QLabel(self.pg_createMA)
        self.lb_empty_13.setObjectName(u"lb_empty_13")
        sizePolicy5.setHeightForWidth(self.lb_empty_13.sizePolicy().hasHeightForWidth())
        self.lb_empty_13.setSizePolicy(sizePolicy5)
        self.lb_empty_13.setMinimumSize(QSize(70, 0))
        self.lb_empty_13.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_7.addWidget(self.lb_empty_13, 4, 2, 1, 1)

        self.lb_empty_9 = QLabel(self.pg_createMA)
        self.lb_empty_9.setObjectName(u"lb_empty_9")

        self.gridLayout_7.addWidget(self.lb_empty_9, 1, 3, 1, 1)

        self.lb_empty_14 = QLabel(self.pg_createMA)
        self.lb_empty_14.setObjectName(u"lb_empty_14")

        self.gridLayout_7.addWidget(self.lb_empty_14, 5, 4, 1, 1)

        self.stackedWidget.addWidget(self.pg_createMA)
        self.pg_doku = QWidget()
        self.pg_doku.setObjectName(u"pg_doku")
        self.gridLayout_5 = QGridLayout(self.pg_doku)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tb_doku = QTableView(self.pg_doku)
        self.tb_doku.setObjectName(u"tb_doku")
        self.tb_doku.setSortingEnabled(True)

        self.gridLayout_5.addWidget(self.tb_doku, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pg_doku)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.layout_menu = QVBoxLayout()
        self.layout_menu.setObjectName(u"layout_menu")
        self.lb_menu = QLabel(self.main_widget)
        self.lb_menu.setObjectName(u"lb_menu")
        sizePolicy2.setHeightForWidth(self.lb_menu.sizePolicy().hasHeightForWidth())
        self.lb_menu.setSizePolicy(sizePolicy2)
        self.lb_menu.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_menu.setFont(font)

        self.layout_menu.addWidget(self.lb_menu)

        self.btn_home = QPushButton(self.main_widget)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(120, 30))
        self.btn_home.setMaximumSize(QSize(120, 30))
        self.btn_home.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_home)

        self.btn_create = QPushButton(self.main_widget)
        self.btn_create.setObjectName(u"btn_create")
        sizePolicy2.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy2)
        self.btn_create.setMinimumSize(QSize(120, 30))
        self.btn_create.setMaximumSize(QSize(120, 30))
        self.btn_create.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_create)

        self.btn_createMA = QPushButton(self.main_widget)
        self.btn_createMA.setObjectName(u"btn_createMA")
        sizePolicy2.setHeightForWidth(self.btn_createMA.sizePolicy().hasHeightForWidth())
        self.btn_createMA.setSizePolicy(sizePolicy2)
        self.btn_createMA.setMinimumSize(QSize(120, 30))
        self.btn_createMA.setMaximumSize(QSize(120, 30))
        self.btn_createMA.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_createMA)

        self.btn_createHS = QPushButton(self.main_widget)
        self.btn_createHS.setObjectName(u"btn_createHS")
        sizePolicy2.setHeightForWidth(self.btn_createHS.sizePolicy().hasHeightForWidth())
        self.btn_createHS.setSizePolicy(sizePolicy2)
        self.btn_createHS.setMinimumSize(QSize(120, 30))
        self.btn_createHS.setMaximumSize(QSize(120, 30))
        self.btn_createHS.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_createHS.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.btn_createHS.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_createHS)

        self.lb_empty = QLabel(self.main_widget)
        self.lb_empty.setObjectName(u"lb_empty")

        self.layout_menu.addWidget(self.lb_empty)

        self.btn_doku = QPushButton(self.main_widget)
        self.btn_doku.setObjectName(u"btn_doku")
        self.btn_doku.setMaximumSize(QSize(120, 30))
        self.btn_doku.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_doku)

        self.btn_mail = QPushButton(self.main_widget)
        self.btn_mail.setObjectName(u"btn_mail")
        self.btn_mail.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_mail.sizePolicy().hasHeightForWidth())
        self.btn_mail.setSizePolicy(sizePolicy2)
        self.btn_mail.setMinimumSize(QSize(120, 30))
        self.btn_mail.setMaximumSize(QSize(120, 30))
        self.btn_mail.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_mail)

        self.btn_settings = QPushButton(self.main_widget)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy2.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy2)
        self.btn_settings.setMinimumSize(QSize(120, 30))
        self.btn_settings.setMaximumSize(QSize(120, 30))
        self.btn_settings.setStyleSheet(u"text-align: left;")

        self.layout_menu.addWidget(self.btn_settings)


        self.gridLayout_6.addLayout(self.layout_menu, 0, 0, 1, 1)

        self.lb_empty_11 = QLabel(self.main_widget)
        self.lb_empty_11.setObjectName(u"lb_empty_11")

        self.gridLayout_6.addWidget(self.lb_empty_11, 1, 1, 1, 1)

        frm_main.setCentralWidget(self.main_widget)

        self.retranslateUi(frm_main)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"auto Fristen", None))
        self.actionTest.setText(QCoreApplication.translate("frm_main", u"Test", None))
        self.actionEinstellungen.setText(QCoreApplication.translate("frm_main", u"Einstellungen", None))
        self.lb_OtherOrdner.setText(QCoreApplication.translate("frm_main", u"Welches ist der Default-Ordner, wenn der MA-Ordner fehlt?", None))
        self.lb_emptylower.setText("")
        self.df_pathHS.setText("")
        self.lb_CC.setText(QCoreApplication.translate("frm_main", u"Empf\u00e4nger f\u00fcr Mail in CC (Mehrere Empf\u00e4nger mittels ; trennen )", None))
        self.lb_emptyline_2.setText("")
        self.label_6.setText(QCoreApplication.translate("frm_main", u"Welches ist der Default-Ordner f\u00fcr die Stakeholder?", None))
        self.lb_emptyline_5.setText("")
        self.lb_emptyline_3.setText("")
        self.btn_pathdf.setText(QCoreApplication.translate("frm_main", u"Change", None))
        self.btn_pathhs.setText(QCoreApplication.translate("frm_main", u"Change", None))
        self.lb_emptyline.setText("")
        self.btn_pathma.setText(QCoreApplication.translate("frm_main", u"Change", None))
        self.df_pathDF.setText("")
        self.lb_empty_8.setText("")
        self.btn_svchange.setText(QCoreApplication.translate("frm_main", u"Save Changes", None))
        self.lb_empty_2.setText("")
        self.lb_Weeks.setText(QCoreApplication.translate("frm_main", u"Wie viele Wochen sollen berechnet werden?", None))
        self.lb_emptyline_4.setText("")
        self.df_pathIM.setText("")
        self.lb_maOrdner.setText(QCoreApplication.translate("frm_main", u"In welchem Ordner befinden sich die Mitarbeiterordner?", None))
        self.label.setText("")
        self.lb_empty_19.setText("")
        self.label_7.setText(QCoreApplication.translate("frm_main", u"F\u00fcr welche/n Stakeholder:", None))
        self.btn_generateHS.setText(QCoreApplication.translate("frm_main", u"Fristenlisten generieren", None))
        self.lb_empty_18.setText("")
        self.lb_empty_16.setText("")
        self.lb_empty_15.setText("")
        self.label_5.setText(QCoreApplication.translate("frm_main", u"Fristenliste bis einschlie\u00dflich: ", None))
        self.lb_empty_17.setText("")
        self.lb_content.setText(QCoreApplication.translate("frm_main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Content [HTML]: </span></p>\n"
"<p style=\" margin-top:3px; margin-bottom:3px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#6b6b6b;\">[@Next] = Montag akt.KW + 14 Tage</span></p></body></html>\n"
"<p style=\" margin-top:3px; margin-bottom:3px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#6b6b6b;\">[@Bearbeitung] = @Next - 5 Tage</span></p></body></html>", None))
        self.btn_save.setText(QCoreApplication.translate("frm_main", u"Save Changes", None))
        self.lb_Sub.setText(QCoreApplication.translate("frm_main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Betreff: </span></p>\n"
"<p style=\" margin-top:3px; margin-bottom:3px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#6b6b6b;\">[@KW] = Woche bis Ende FL</span></p></body></html>", None))
        self.lb_Fristenliste.setText(QCoreApplication.translate("frm_main", u"Fristenliste bis einschlie\u00dflich: ", None))
        self.lb_empty_4.setText("")
        self.cb_Mail.setText(QCoreApplication.translate("frm_main", u"E-Mails versenden", None))
        self.cb_InnoMgr.setText(QCoreApplication.translate("frm_main", u"Liste Responsible-Source1", None))
        self.lb_empty_3.setText("")
        self.lb_empty_7.setText("")
        self.lb_empty_6.setText("")
        self.btn_generate.setText(QCoreApplication.translate("frm_main", u"Liste generieren", None))
        self.cb_BackOffice.setText(QCoreApplication.translate("frm_main", u"Liste Responsible-Source2", None))
        self.lb_empty_5.setText("")
        self.btn_generateMA.setText(QCoreApplication.translate("frm_main", u"Liste generieren", None))
        self.label_3.setText(QCoreApplication.translate("frm_main", u"F\u00fcr Fristenliste:", None))
        self.rb_InnoMgr.setText(QCoreApplication.translate("frm_main", u"Responsible Source1", None))
        self.label_2.setText(QCoreApplication.translate("frm_main", u"Fristenliste bis einschlie\u00dflich: ", None))
        self.label_4.setText(QCoreApplication.translate("frm_main", u"F\u00fcr welche/n Mitarbeiter:", None))
        self.rb_weitereMA.setText(QCoreApplication.translate("frm_main", u"Responsible Source2", None))
        self.cb_MailMA.setText(QCoreApplication.translate("frm_main", u"E-Mails versenden", None))
        self.lb_empty_12.setText("")
        self.lb_empty_10.setText("")
        self.lb_empty_13.setText("")
        self.lb_empty_9.setText("")
        self.lb_empty_14.setText("")
        self.lb_menu.setText(QCoreApplication.translate("frm_main", u"Men\u00fc", None))
        self.btn_home.setText(QCoreApplication.translate("frm_main", u"Home", None))
        self.btn_create.setText(QCoreApplication.translate("frm_main", u"Fristenlisten", None))
        self.btn_createMA.setText(QCoreApplication.translate("frm_main", u"FL f/ MItarbeiter", None))
        self.btn_createHS.setText(QCoreApplication.translate("frm_main", u"FL f/ Stakeholder", None))
        self.lb_empty.setText("")
        self.btn_doku.setText(QCoreApplication.translate("frm_main", u"Dokumentation", None))
        self.btn_mail.setText(QCoreApplication.translate("frm_main", u"E-Mail Content", None))
        self.btn_settings.setText(QCoreApplication.translate("frm_main", u"Einstellungen", None))
        self.lb_empty_11.setText("")
    # retranslateUi

