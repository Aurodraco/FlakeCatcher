# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (QHBoxLayout, QTextEdit, QWidget)
from ShadowStacker import ShadowStacker


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 630)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.hboxLayout = QHBoxLayout(self.widget)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        self.hboxLayout.addWidget(self.textEdit)

        # 将右侧框设置为 ShadowStacker
        self.shadowStacker = ShadowStacker(self.widget)
        self.shadowStacker.setObjectName(u"shadowStacker")

        self.hboxLayout.addWidget(self.shadowStacker)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow",
                                       u"\u96ea\u82b1\u6355\u624b", None))

    # retranslateUi
